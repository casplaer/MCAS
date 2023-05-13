# Generated by Django 4.2.1 on 2023-05-13 16:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_user_parent_first_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='department_name',
            field=models.CharField(default='Департамент', max_length=200, verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='f',
            field=models.CharField(default='Фамилия', max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='i',
            field=models.CharField(default='Имя', max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instrument_name',
            field=models.CharField(default='Инструмент', max_length=200, verbose_name='Инструмент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='o',
            field=models.CharField(default='Отчество', max_length=200, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_first_name',
            field=models.CharField(default='Имя представителя 1', max_length=200, verbose_name='ФИО Представителя 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_first_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+375123123123', max_length=128, region=None, verbose_name='Телефон Представителя 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_second_name',
            field=models.CharField(default='Имя представителя 2', max_length=200, verbose_name='Имя Представителя 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_second_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+375123123123', max_length=128, region=None, verbose_name='Телефон Представителя 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rewards',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_year',
            field=models.DateField(default='2000-12-12', verbose_name='Дата начала обучения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='teacher_name',
            field=models.CharField(default='Учитель', max_length=200, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='teacher_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+375123123123', max_length=128, region=None, verbose_name='Номер учителя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+375123123123', max_length=128, region=None, verbose_name='Телефон учащегося'),
        ),
        migrations.AlterField(
            model_name='user',
            name='years',
            field=models.CharField(default='0', max_length=3, verbose_name='Продолжительность обучения'),
        ),
    ]