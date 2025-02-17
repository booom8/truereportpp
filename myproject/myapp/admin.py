from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')  # Какие поля показывать в списке
    search_fields = ('title', 'category')  # Поиск по этим полям
    list_filter = ('category', 'created_at')  # Фильтры справа
