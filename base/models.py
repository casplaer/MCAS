from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
import os
from django.core.validators import RegexValidator

# Create your models here.

class GroupNumber(models.Model):
    number = models.CharField(max_length=25, blank=False, null=False, default='Номер группы')

    def __str__(self):
        return self.number


class Subject(models.Model):
    group = models.BooleanField(null=False, blank=False, default=False, verbose_name="Групповое")
    name = models.CharField(max_length=50, null=False, default='Предмет', verbose_name="Название предмета")
    teacher = models.CharField(max_length=100, null=True, verbose_name="Учитель")

    def __str__(self):
        return self.name


class User(AbstractUser):
    STATUS_CHOICES = (
        ('admin', 'Администратор'),
        ('student', 'Ученик'),
        ('concertmaster', 'Концертмейстер'),
        ('editor', 'Редактор'),
        ('teacher', 'Учитель'),
    )

    f = models.CharField(max_length=200, null = False, default='Фамилия', verbose_name="Фамилия")
    i = models.CharField(max_length=200, null = False, default='Имя', verbose_name='Имя')
    o = models.CharField(max_length=200, null = False, default='Отчество', verbose_name='Отчество')
    department_name = models.CharField(max_length=200, null = False, default='Департамент', verbose_name='Департамент')
    teacher_name = models.CharField(max_length=200, null = False, default='Учитель', verbose_name='Учитель')
    instrument_name = models.CharField(max_length=200, null = False, default='Инструмент', verbose_name='Инструмент')
    teacher_number = PhoneNumberField(null=False, default='+375293123123', verbose_name='Номер учителя')
    years = models.CharField(max_length=
                             3, null=False, default='0', verbose_name='Продолжительность обучения')
    start_year = models.DateField(null=False, default= '2000-12-12', verbose_name='Дата начала обучения')
    user_number = PhoneNumberField(null=False, default='+375293123123', verbose_name='Телефон учащегося')
    parent_first_name = models.CharField(max_length=200, null=False, default='Имя представителя 1', verbose_name='ФИО Представителя 1')
    parent_first_number = PhoneNumberField(null=False, default='+375293123123', verbose_name='Телефон Представителя 1')
    parent_second_name = models.CharField(max_length=200, null=False, default='Имя представителя 2', verbose_name='Имя Представителя 2')
    parent_second_number = PhoneNumberField(null=False, default='+375293123123', verbose_name='Телефон Представителя 2')
    rewards = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, default='student')
    avatar = models.ImageField(upload_to='images/', null=True,
                               default="images/profile-pictures/default.jpg",
                               verbose_name="Загрузите аватар для профиля")
    groups = models.ManyToManyField(GroupNumber, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



class New(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название статьи")
    description = RichTextField(null = False, blank = False, max_length = 100000, verbose_name="Подробное описание статьи")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    description = RichTextField(null = False, blank=False, verbose_name="Общая информация")
    rewards = RichTextField(null=False, blank = False, verbose_name="Заслуги школы", default="Временно недоступно")
    teachers = RichTextField(null=False, blank = False, verbose_name="Информация об учителях", default="Временно недоступно")

    def __str__(self):
        return self.description

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class File(models.Model):
    file_name = models.CharField(max_length=75, default='default_name')
    file_upload = models.FileField(upload_to='library')

    def __str__(self):
        return self.file_name


class UserFiles(File):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name


class Event(models.Model):
    DEPARTMENT_CHOICES = (
        ('piano', 'Фортепианное'),
        ('strings', 'Струнно-смычковое'),
        ('folk', 'Народное'),
        ('string-folk', 'Струнно-народное'),
        ('choir', 'Хоровое'),
        ('theory', 'Теоретическое'),
    )

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    date = models.DateField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, null=False, default='piano')


class Task(models.Model):
    grouped = models.BooleanField(default=False)
    groups = models.ManyToManyField(GroupNumber, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True)
    date = models.DateField(null=False, default='2020-8-9', verbose_name='Дата')
    subject_number = models.IntegerField(blank=False, default=1, verbose_name='Номер урока')
    sub = models.ForeignKey(Subject, verbose_name="Название урока", null=True, on_delete=models.CASCADE)
    student_name = models.ForeignKey(User, verbose_name='Учащийся', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.description
