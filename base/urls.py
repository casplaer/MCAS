from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerPage, name = 'register'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),

    path('', views.home, name = 'home'),
    path('new/<str:pk>/', views.new, name = 'new'),
    path('create-new/', views.createNew, name = 'create-new'),
    path('news/', views.newsPage, name = 'news'),
]
