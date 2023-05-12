# Generated by Django 4.2.1 on 2023-05-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_user_name_user_department_name_user_f_user_i_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='department',
            field=models.CharField(choices=[('piano', 'Фортепианное'), ('strings', 'Струнно-смычковое'), ('folk', 'Народное'), ('string-folk', 'Струнно-народное'), ('choir', 'Хоровое'), ('theory', 'Теоретическое')], default='piano', max_length=20),
        ),
    ]