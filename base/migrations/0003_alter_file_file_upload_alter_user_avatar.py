# Generated by Django 4.2 on 2023-04-15 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_file_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_upload',
            field=models.FileField(upload_to='midi', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mid', 'mp3'])]),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.jpg', null=True, upload_to='images', verbose_name='Загрузите аватар для профиля'),
        ),
    ]
