from django.shortcuts import render, redirect
from .forms import ReportForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Report

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
            return redirect("index")  # Перенаправляем на главную
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})  # Используем текущий шаблон

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})  # Используем текущий шаблон

def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def profile(request):
    user_reports = Report.objects.filter(user=request.user)  # Фильтруем заявки пользователя
    return render(request, 'lk.html', {'user': request.user, 'reports': user_reports})