from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .forms import NewForm, RegistrationForm, AboutForm, FileUploadForm, EventCreationForm
from .models import New, User, Event, File, About


class NewFormTest(TestCase):
    def test_new_form_valid_data(self):
        form = NewForm(data={
            'title': 'Test Title',
            'description': 'Test Description'
        })
        self.assertTrue(form.is_valid())

    def test_new_form_empty_data(self):
        form = NewForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class AboutFormTestCase(TestCase):

    def test_about_form_valid(self):
        form_data = {'description': 'Some test description'}
        form = AboutForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_about_form_invalid(self):
        form_data = {'description': ''}
        form = AboutForm(data=form_data)
        self.assertFalse(form.is_valid())


class FileUploadFormTestCase(TestCase):

    def test_file_upload_form_invalid(self):
        # test form without any data
        form = FileUploadForm(data={})
        self.assertFalse(form.is_valid())

    def test_file_upload_form_save(self):
        file = SimpleUploadedFile("file.txt", b"file_content")
        form = FileUploadForm(files={'file_upload': file}, data={'file_name': 'test_file'})
        self.assertTrue(form.is_valid())

    def test_file_upload_form_invalid(self):
        form = FileUploadForm(data={'file_name': 'Test File'})
        self.assertFalse(form.is_valid())


class EventCreationFormTestCase(TestCase):

    def test_event_creation_form_valid(self):
        form_data = {
            'title': 'Test Event',
            'description': 'Some test description',
            'date': '2023-05-12',
            'department': 'piano'
        }
        form = EventCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_event_creation_form_invalid(self):
        form_data = {
            'title': '',
            'description': 'Some test description',
            'date': '2023-05-12',
            'department': 'piano'
        }
        form = EventCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
