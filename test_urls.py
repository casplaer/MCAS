from django.test import TestCase
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