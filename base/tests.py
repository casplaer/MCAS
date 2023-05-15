from datetime import date
from django.test import TestCase, RequestFactory
from .models import GroupNumber
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse, resolve
from .views import *

class TestUrls(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='12345')
        self.client.login(username='tester', password='12345')

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutUser)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registerPage)

    def test_user_profile_url_is_resolved(self):
        url = reverse('user-profile', args=[str(self.user.id)])
        self.assertEqual(resolve(url).func, userProfile)

    def test_delete_new_url_is_resolved(self):
        url = reverse('delete-new', args=[str(1)])
        self.assertEqual(resolve(url).func, deleteNew)

    def test_edit_new_url_is_resolved(self):
        url = reverse('edit-new', args=[str(1)])
        self.assertEqual(resolve(url).func, editNew)

    def test_edit_about_url_is_resolved(self):
        url = reverse('edit-about')
        self.assertEqual(resolve(url).func, editAbout)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_preview_url_is_resolved(self):
        url = reverse('preview')
        self.assertEqual(resolve(url).func, preview)

    def test_teachers_url_is_resolved(self):
        url = reverse('teacher-list')
        self.assertEqual(resolve(url).func, teachers)

    def test_music_library_url_is_resolved(self):
        url = reverse('music-library')
        self.assertEqual(resolve(url).func, musicLib)

    def test_file_upload_url_is_resolved(self):
        url = reverse('file-upload')
        self.assertEqual(resolve(url).func, file_upload)

    def test_file_download_url_is_resolved(self):
        url = reverse('file-download', args=[str(1)])
        self.assertEqual(resolve(url).func, download_file)

    def test_rewards_url_is_resolved(self):
        url = reverse('rewards')
        self.assertEqual(resolve(url).func, rewards)

    def test_teachers_info_url_is_resolved(self):
        url = reverse('teachers-info')
        self.assertEqual(resolve(url).func, teachersInfo)

    def test_piano_dep_url_is_resolved(self):
        url = reverse('piano-dep')
        self.assertEqual(resolve(url).func, pianoDepartment)

    def test_new_event_url_is_resolved(self):
        url = reverse('new-event')
        self.assertEqual(resolve(url).func, new_event)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_new_url_is_resolved(self):
        url = reverse('new', args=[str(1)])
        self.assertEqual(resolve(url).func, new)

    def test_create_new_url_is_resolved(self):
        url = reverse('create-new')
        self.assertEqual(resolve(url).func, createNew)

    def test_news_page_url_is_resolved(self):
        url = reverse('create-new')
        self.assertEqual(resolve(url).func, createNew)


class GroupNumberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        GroupNumber.objects.create(number='Group 1')

    def test_number_label(self):
        group_number = GroupNumber.objects.get(id=1)
        field_label = group_number._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_number_max_length(self):
        group_number = GroupNumber.objects.get(id=1)
        max_length = group_number._meta.get_field('number').max_length
        self.assertEquals(max_length, 25)

    def test_number_default(self):
        group_number = GroupNumber.objects.get(id=1)
        default_value = group_number.number
        self.assertEquals(default_value, 'Group 1')

# models

    class UserTestCase(TestCase):
        def setUp(self):
            self.user = User.objects.create(
                f='Иванов',
                i='Иван',
                o='Иванович',
                department_name='Музыкальный',
                teacher_name='Петров',
                instrument_name='Гитара',
                teacher_number='+375299999999',
                years='3',
                start_year='2020-09-01',
                user_number='+375291111111',
                parent_first_name='Представитель 1',
                parent_first_number='+375293333333',
                parent_second_name='Представитель 2',
                parent_second_number='+375294444444',
                rewards='Высшая степень на конкурсе гитаристов 2021',
                bio='Я занимаюсь гитарой уже 3 года и очень люблю музыку.',
                status='student'
            )

        def test_user_str(self):
            self.assertEqual(str(self.user), 'Иванов Иван Иванович')

        def test_user_full_name(self):
            self.assertEqual(self.user.get_full_name(), 'Иванов Иван Иванович')

        def test_user_department_name(self):
            self.assertEqual(self.user.department_name, 'Музыкальный')

        def test_user_teacher_name(self):
            self.assertEqual(self.user.teacher_name, 'Петров')

        def test_user_instrument_name(self):
            self.assertEqual(self.user.instrument_name, 'Гитара')

        def test_user_teacher_number(self):
            self.assertEqual(self.user.teacher_number, '+375299999999')

        def test_user_years(self):
            self.assertEqual(self.user.years, '3')

        def test_user_user_number(self):
            self.assertEqual(self.user.user_number, '+375291111111')

        def test_user_parent_first_name(self):
            self.assertEqual(self.user.parent_first_name, 'Представитель 1')

        def test_user_parent_first_number(self):
            self.assertEqual(self.user.parent_first_number, '+375293333333')

        def test_user_parent_second_name(self):
            self.assertEqual(self.user.parent_second_name, 'Представитель 2')

        def test_user_parent_second_number(self):
            self.assertEqual(self.user.parent_second_number, '+375294444444')

        def test_user_rewards(self):
            self.assertEqual(self.user.rewards, 'Высшая степень на конкурсе гитаристов 2021')

        def test_user_bio(self):
            self.assertEqual(self.user.bio, 'Я занимаюсь гитарой уже 3 года и очень люблю музыку.')

        def test_user_status(self):
            self.assertEqual(self.user.status, 'student')

        def test_user_avatar(self):
            self.assertEqual(self.user.avatar.url, 'images/profile-pictures/default.jpg')


class NewModelTestCase(TestCase):
    def setUp(self):
        self.new = New.objects.create(
            title="Test title",
            description="Test description"
        )

    def test_new_object_creation(self):
        self.assertEqual(self.new.title, "Test title")
        self.assertEqual(self.new.description, "Test description")

    def test_new_object_string_representation(self):
        self.assertEqual(str(self.new), "Test title")


class AboutModelTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            description="Test description",
            rewards="Test rewards",
            teachers="Test teachers"
        )

    def test_about_object_creation(self):
        self.assertEqual(self.about.description, "Test description")
        self.assertEqual(self.about.rewards, "Test rewards")
        self.assertEqual(self.about.teachers, "Test teachers")

    def test_about_object_string_representation(self):
        self.assertEqual(str(self.about), "Test description")


class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.message = Message.objects.create(
            user=self.user,
            body="Test body"
        )

    def test_message_object_creation(self):
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.body, "Test body")

    def test_message_object_string_representation(self):
        self.assertEqual(str(self.message), "Test body")


class FileModelTestCase(TestCase):
    def setUp(self):
        self.file = File.objects.create(
            file_name="Test file",
            file_upload="test.pdf"
        )

    def test_file_object_creation(self):
        self.assertEqual(self.file.file_name, "Test file")
        self.assertEqual(self.file.file_upload.name, "test.pdf")

    def test_file_object_string_representation(self):
        self.assertEqual(str(self.file), "Test file")


class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=date.today(),
            department="piano"
        )

    def test_event_object_creation(self):
        event = Event.objects.get(title="Test Event")
        self.assertEqual(event.title, "Test Event")
        self.assertEqual(event.description, "Test Description")
        self.assertEqual(event.date, date.today())
        self.assertEqual(event.department, "piano")

    def test_event_department_choices(self):
        event = Event.objects.get(title="Test Event")
        department_label = dict(event.DEPARTMENT_CHOICES)[event.department]
        self.assertEqual(department_label, "Фортепианное")

    def test_event_update(self):
        event = Event.objects.get(title="Test Event")
        event.title = "Updated Event Title"
        event.description = "Updated Description"
        event.date = date(2023, 6, 1)
        event.department = "strings"
        event.save()
        updated_event = Event.objects.get(title="Updated Event Title")
        self.assertEqual(updated_event.title, "Updated Event Title")
        self.assertEqual(updated_event.description, "Updated Description")
        self.assertEqual(updated_event.date, date(2023, 6, 1))
        self.assertEqual(updated_event.department, "strings")

    def test_description_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_date_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_department_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('department').verbose_name
        self.assertEquals(field_label, 'department')

    def test_title_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_department_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('department').max_length
        self.assertEquals(max_length, 20)


class TaskModelTest(TestCase):
    def setUp(self):
        group1 = GroupNumber.objects.create(number='101')
        group2 = GroupNumber.objects.create(number='102')
        self.task = Task.objects.create(description='Task')

    def test_description_field(self):
        description = self.task.description
        self.assertEqual(description, 'Task')



class EditAboutTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.about = About.objects.create(id=1, title='Test Title', content='Test Content')

    def test_edit_about(self):
        request = self.factory.post('/', {'title': 'New Title', 'content': 'New Content'})
        response = editAbout(request)
        self.assertRedirects(response, 'home')
        updated_about = About.objects.get(id=1)
        self.assertEqual(updated_about.title, 'New Title')
        self.assertEqual(updated_about.content, 'New Content')


class EditAboutViewTestCase(TestCase):
    def test_edit_about_view(self):
        # Создаем тестовый запрос GET
        response = self.client.get('/edit_about/')
        self.assertEqual(response.status_code, 200)

        # Создаем тестовый запрос POST
        form_data = {'file_name': 'Test File', 'file_upload': 'path/to/file.txt'}
        response = self.client.post('/edit_about/', data=form_data)
        self.assertRedirects(response, 'home')


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


class NewEventViewTestCase(TestCase):
    def test_new_event_view(self):
        # Создаем тестовый запрос GET
        response = self.client.get('/new-event/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/new_event.html')

        # Создаем тестовый запрос POST
        form_data = {'field1': 'value1', 'field2': 'value2'}
        response = self.client.post('/new_event/', data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/profile.html')

class ContingentViewTestCase(TestCase):
    def test_contingent_view(self):
        response = self.client.get('/contingent/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/contingent.html')

class StudentInfoViewTestCase(TestCase):
    def test_student_info_view(self):
        user = User.objects.create(username='testuser')
        response = self.client.get(reverse('student-info', args=[user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/student_info.html')

class DiaryViewTestCase(TestCase):
    def test_diary_view(self):
        user = User.objects.create(username='testuser')
        self.client.force_login(user)
        response = self.client.get('/diary/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/diary.html')

class HomeworkViewTestCase(TestCase):
    def test_homework_view(self):
        response = self.client.get('/homework/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/homework.html')


class GetPianoViewTestCase(TestCase):
    def test_get_piano_view(self):
        response = self.client.get('/piano-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

class GetStringsViewTestCase(TestCase):
    def test_get_strings_view(self):
        response = self.client.get('/strings-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

class GetFolkViewTestCase(TestCase):
    def test_get_folk_view(self):
        response = self.client.get('/folk-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

class GetStringFolkViewTestCase(TestCase):
    def test_get_string_folk_view(self):
        response = self.client.get('/string-folk-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

class GetChoirViewTestCase(TestCase):
    def test_get_choir_view(self):
        response = self.client.get('/choir-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

class GetTheoryViewTestCase(TestCase):
    def test_get_theory_view(self):
        response = self.client.get('/theory-events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')


class DownloadFileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.file = File.objects.create(file_name='test_file', file_upload=SimpleUploadedFile("test.txt", b"file_content"))

    def test_download_file_view(self):
        request = self.factory.get(reverse('file-download', args=[self.file.pk]))
        response = download_file(request, pk=self.file.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'text/plain')
        self.assertEqual(response['Content-Disposition'], f'attachment; filename="{self.file.file_upload.name}"')

class DownloadUFileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user_file = UserFiles.objects.create(file_name='test_user_file', file_upload=SimpleUploadedFile("test.txt", b"file_content"))

    def test_download_ufile_view(self):
        request = self.factory.get(reverse('ufile-download', args=[self.user_file.pk]))
        response = download_ufile(request, pk=self.user_file.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'text/plain')
        self.assertEqual(response['Content-Disposition'], f'attachment; filename="{self.user_file.file_upload.name}"')

class RewardsViewTestCase(TestCase):
    def test_rewards_view(self):
        response = self.client.get('/rewards/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/rewards.html')

class TeachersInfoViewTestCase(TestCase):
    def test_teachers_info_view(self):
        response = self.client.get('/teachers-info/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/teachers-info.html')

class PianoDepartmentViewTestCase(TestCase):
    def test_piano_department_view(self):
        response = self.client.get('/piano-dep/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/piano_department.html')


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/home.html')

class NewViewTestCase(TestCase):
    def setUp(self):
        self.new = New.objects.create(title='Test News', content='This is a test news')

    def test_new_view(self):
        response = self.client.get(reverse('new', args=[self.new.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/news.html')

class LoginPageViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_page_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/login_register.html')

    def test_login_post(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/home/')
        # Additional assertions to verify login functionality

    def test_login_post_invalid_credentials(self):
        response = self.client.post('/login/', {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'base/login_register.html')