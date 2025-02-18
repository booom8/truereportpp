from django import forms
from .models import Report
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ReportUpdateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status', 'resolved_photo']

    
class ReportAdminForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status', 'resolved_photo']

    def clean_status(self):
        """ Проверяем, можно ли изменить статус на 'Решена' """
        status = self.cleaned_data.get("status")
        resolved_photo = self.cleaned_data.get("resolved_photo") or self.instance.resolved_photo

        if status == "resolved" and not resolved_photo:
            raise forms.ValidationError("Нельзя менять статус на 'Решена' без фото после!")
        return status
