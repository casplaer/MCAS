# Generated by Django 4.2.1 on 2023-05-14 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_task_groups_task_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Учащийся'),
        ),
    ]