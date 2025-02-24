from django.contrib.auth.models import User
from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('roads', 'Дороги'),
        ('utilities', 'ЖКХ'),
        ('public_places', 'Общественные места'),
    ]

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('resolved', 'Решена'),
        ('rejected', 'Отклонена'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    rejection_reason = models.TextField(blank=True, null=True, verbose_name="Причина отклонения") # Новое поле!
    photo = models.ImageField(upload_to='reports/', blank=True, null=True)
    resolved_photo = models.ImageField(upload_to='reports/resolved/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_be_resolved(self):
        return self.resolved_photo

    def __str__(self):
        return self.title
