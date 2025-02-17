from django.contrib.auth.models import User
from django.db import models

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=100, verbose_name="Категория")
    photo = models.ImageField(upload_to='reports/', verbose_name="Фотография", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
