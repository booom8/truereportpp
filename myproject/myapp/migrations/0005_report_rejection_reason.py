# Generated by Django 5.1.4 on 2025-02-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_report_resolved_photo_report_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
