from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createreport/', views.create_report, name='createreport'),
    path('report/', views.report, name='report'),
    path('login/', views.login_view, name='login'),
    path('auth/', views.auth_view, name='auth'),
    path('lk/', views.lk_view, name='lk'),
]