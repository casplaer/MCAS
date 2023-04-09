from django.forms import ModelForm
from django import forms
from .models import New, User
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField


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
            'first_name',
            'last_name',
            'avatar',
            'status',
            'password1',
            'password2',
        ]