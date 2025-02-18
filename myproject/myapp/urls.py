from django.urls import path
from . import views
from .views import report_view, register_view, login_view, home, personal_cabinet, update_report, delete_report
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('createreport/', views.createreport, name='createreport'),
    path('report/', report_view, name='report'),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path('lk/', personal_cabinet, name='lk'),
    path('update_report/<int:report_id>/', update_report, name='update_report'),
    path('delete_report/<int:report_id>/', delete_report, name='delete_report'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]