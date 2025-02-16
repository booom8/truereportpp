from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def create_report(request):
    return render(request, 'createreport.html')

def report(request):
    return render(request, 'report.html')

def login_view(request):
    return render(request, 'login.html')

def auth_view(request):
    return render(request, 'auth.html')

def lk_view(request):
    return render(request, 'lk.html')