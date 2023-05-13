# Generated by Django 4.2.1 on 2023-05-13 16:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_user_bio_alter_user_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='parent_first_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='80123123123', max_length=128, region=None, verbose_name='Телефон Представителя 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_second_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='80123123123', max_length=128, region=None, verbose_name='Телефон Представителя 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='teacher_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='80123123123', max_length=128, region=None, verbose_name='Номер учителя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='80123123123', max_length=128, region=None, verbose_name='Телефон учащегося'),
        ),
    ]
