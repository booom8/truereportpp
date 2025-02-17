from django.urls import path
from . import views
from .views import report_view, register_view, login_view, logout_view, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('createreport/', views.create_report, name='createreport'),
    path('report/', report_view, name='report'),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path('lk/', profile, name='lk'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]