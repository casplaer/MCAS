# Generated by Django 4.2.1 on 2023-05-14 11:38

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('f', models.CharField(default='Фамилия', max_length=200, verbose_name='Фамилия')),
                ('i', models.CharField(default='Имя', max_length=200, verbose_name='Имя')),
                ('o', models.CharField(default='Отчество', max_length=200, verbose_name='Отчество')),
                ('department_name', models.CharField(default='Департамент', max_length=200, verbose_name='Департамент')),
                ('teacher_name', models.CharField(default='Учитель', max_length=200, verbose_name='Учитель')),
                ('instrument_name', models.CharField(default='Инструмент', max_length=200, verbose_name='Инструмент')),
                ('teacher_number', phonenumber_field.modelfields.PhoneNumberField(default='+375293123123', max_length=128, region=None, verbose_name='Номер учителя')),
                ('years', models.CharField(default='0', max_length=3, verbose_name='Продолжительность обучения')),
                ('start_year', models.DateField(default='2000-12-12', verbose_name='Дата начала обучения')),
                ('user_number', phonenumber_field.modelfields.PhoneNumberField(default='+375293123123', max_length=128, region=None, verbose_name='Телефон учащегося')),
                ('parent_first_name', models.CharField(default='Имя представителя 1', max_length=200, verbose_name='ФИО Представителя 1')),
                ('parent_first_number', phonenumber_field.modelfields.PhoneNumberField(default='+375293123123', max_length=128, region=None, verbose_name='Телефон Представителя 1')),
                ('parent_second_name', models.CharField(default='Имя представителя 2', max_length=200, verbose_name='Имя Представителя 2')),
                ('parent_second_number', phonenumber_field.modelfields.PhoneNumberField(default='+375293123123', max_length=128, region=None, verbose_name='Телефон Представителя 2')),
                ('rewards', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('admin', 'Администратор'), ('student', 'Ученик'), ('concertmaster', 'Концертмейстер'), ('editor', 'Редактор'), ('teacher', 'Учитель')], default='student', max_length=20)),
                ('avatar', models.ImageField(default='images/profile-pictures/default.jpg', null=True, upload_to='images/', verbose_name='Загрузите аватар для профиля')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Общая информация')),
                ('rewards', ckeditor.fields.RichTextField(default='Временно недоступно', verbose_name='Заслуги школы')),
                ('teachers', ckeditor.fields.RichTextField(default='Временно недоступно', verbose_name='Информация об учителях')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('date', models.DateField()),
                ('department', models.CharField(choices=[('piano', 'Фортепианное'), ('strings', 'Струнно-смычковое'), ('folk', 'Народное'), ('string-folk', 'Струнно-народное'), ('choir', 'Хоровое'), ('theory', 'Теоретическое')], default='piano', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='default_name', max_length=75)),
                ('file_upload', models.FileField(upload_to='library')),
            ],
        ),
        migrations.CreateModel(
            name='GroupNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='Номер группы', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название статьи')),
                ('description', ckeditor.fields.RichTextField(max_length=100000, verbose_name='Подробное описание статьи')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField(default=False, verbose_name='Групповое')),
                ('name', models.CharField(default='Предмет', max_length=50, verbose_name='Название предмета')),
                ('teacher', models.CharField(max_length=100, null=True, verbose_name='Учитель')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('date', models.DateField(default='2020-8-9', verbose_name='Дата')),
                ('subject_number', models.IntegerField(default=1, verbose_name='Номер урока')),
                ('groups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.groupnumber')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.subject', verbose_name='Название урока')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='base.subject'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
