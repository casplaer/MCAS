from django.forms import ModelForm
from django import forms
from .models import New, User, About, File, Event, Task
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
#from ckeditor.fields import RichTextField


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'description']
        widgets = {
            'description': CKEditorWidget(),
        }


class RegistrationForm(UserCreationForm):
    status = forms.ChoiceField(choices=User.STATUS_CHOICES, required=True, label="Статус")

    class Meta:
        model = User
        fields = [
            'username',
            'f',
            'i',
            'o',
            'department_name',
            'teacher_name',
            'instrument_name',
            'teacher_number',
            'years',
            'start_year',
            'user_number',
            'parent_first_name',
            'parent_first_number',
            'parent_second_name',
            'parent_second_number',
            'avatar',
            'status',
            'password1',
            'password2',
        ]


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = ['description']
        widgets = {
            'description': CKEditorWidget(),
        }


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_upload', 'file_name']


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'department']


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
