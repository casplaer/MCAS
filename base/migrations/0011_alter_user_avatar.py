# Generated by Django 4.2 on 2023-05-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='images/profile-pictures/default.jpg', null=True, upload_to='files/images/profile-pictures', verbose_name='Загрузите аватар для профиля'),
        ),
    ]