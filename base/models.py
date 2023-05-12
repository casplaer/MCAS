from django.db import models
from django.contrib.auth.models import User, AbstractUser
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
# Create your models here.


class User(AbstractUser):
    STATUS_CHOICES = (
        ('admin', 'Администратор'),
        ('student', 'Ученик'),
        ('concertmaster', 'Концертмейстер'),
        ('editor', 'Редактор'),
        ('teacher', 'Учитель'),
    )

    name = models.CharField(max_length=200, null = True)
    bio = models.TextField(null = True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    avatar = models.ImageField(upload_to='images/', null=True,
                               default="images/profile-pictures/default.jpg",
                               verbose_name="Загрузите аватар для профиля")

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


class Event(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    date = models.DateTimeField()