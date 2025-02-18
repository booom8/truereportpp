from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportForm, RegisterForm, LoginForm, ReportUpdateForm, ReportAdminForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Report
from django.db import connection
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def create_report(request):
    return render(request, 'createreport.html')

def report(request):
    return render(request, 'report.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def lk_view(request):
    return render(request, 'lk.html')

def report_view(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createreport')  # После успешного добавления заявки перенаправляем
    else:
        form = ReportForm()
    
    return render(request, 'report.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Перенаправляем на главную
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})  # Используем текущий шаблон

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})  # Используем текущий шаблон

def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def profile(request):
    user_reports = Report.objects.filter(user=request.user)  # Фильтруем заявки пользователя
    return render(request, 'lk.html', {'user': request.user, 'reports': user_reports})

def home(request):
    latest_reports = Report.objects.order_by('-created_at')[:4]  # Последние 4 заявки
    total_reports = Report.objects.count()  # Всего заявок
    
    return render(request, 'index.html', {
        'latest_reports': latest_reports,
        'total_reports': total_reports
    })

def createreport(request):
    reports = Report.objects.all()  # Загружаем ВСЕ заявки

    status = request.GET.get('status')
    if status in ['new', 'resolved', 'rejected']:
        reports = reports.filter(status=status)  # Фильтрация по статусу

    sort = request.GET.get('sort')
    if sort == 'date':
        reports = reports.order_by('-created_at')

    return render(request, 'createreport.html', {'reports': reports})


def update_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    if request.method == "POST":
        form = ReportUpdateForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('createreport')  # Перенаправляем на страницу всех заявок

    else:
        form = ReportUpdateForm(instance=report)

    return render(request, 'update_report.html', {'form': form, 'report': report})


@login_required
def personal_cabinet(request):
    reports = Report.objects.filter(user=request.user) if not request.user.is_staff else Report.objects.all()
    return render(request, 'lk.html', {'reports': reports})

@login_required
def update_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    # Проверяем, что только админ может редактировать заявки
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для редактирования заявки.")
        return redirect('lk')

    if request.method == "POST":
        form = ReportAdminForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно обновлена!")
            return redirect('lk')
    else:
        form = ReportAdminForm(instance=report)

    return render(request, 'update_report.html', {'form': form, 'report': report})

@login_required
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    # Проверяем, что только админ может удалять заявки
    if not request.user.is_staff:
        messages.error(request, "Вы не можете удалить эту заявку.")
        return redirect('lk')

    report.delete()
    messages.success(request, "Заявка успешно удалена!")
    return redirect('lk')