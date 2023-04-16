from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerPage, name = 'register'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
    path('delete-new/<str:pk>', views.deleteNew, name = 'delete-new'),
    path('edit-new/<str:pk>', views.editNew, name = 'edit-new'),
    path('edit-about/', views.editAbout, name = 'edit-about'),
    path('about/', views.about, name = 'about'),
    path('preview/', views.preview, name = 'preview'),
    path('teacher-list/', views.teachers, name = 'teacher-list'),
    path('music-library', views.musicLib, name = 'music-library'),
    path('upload/', views.file_upload, name = 'file-upload'),
    path('download/<str:pk>', views.download_file, name = 'file-download'),
    path('rewards/', views.rewards, name = 'rewards'),
    path('teachers-info/', views.teachersInfo, name = 'teachers-info'),

    path('', views.home, name = 'home'),
    path('new/<str:pk>/', views.new, name = 'new'),
    path('create-new/', views.createNew, name = 'create-new'),
    path('news/', views.newsPage, name = 'news'),
]
