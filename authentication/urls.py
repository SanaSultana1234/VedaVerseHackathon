from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('learn', views.learn, name="learn"),
    path('about', views.about, name="about"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('game', views.game, name="game"),
]

