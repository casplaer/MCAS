from datetime import date
from django.test import TestCase
from .models import User, New, About, Message, File, Event, GroupNumber, Task

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
            self.assertEqual(self.user.avatar.url, '/media/images/profile-pictures/default.jpg')


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
