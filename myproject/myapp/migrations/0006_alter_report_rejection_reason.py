# Generated by Django 5.1.4 on 2025-02-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_report_rejection_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина отклонения'),
        ),
    ]
