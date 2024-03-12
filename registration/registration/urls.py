"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


  

urlpatterns = [
    path('admin/', views.AdminPage,name='admin'),
    path('',views.IndexPage,name='index'),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('courses/',views.CoursesPage,name='courses'),
    path('add_courses/',views.Add_CoursesPage,name='add_courses'),
    path('read/<int:courses_id>/', views.ReadPage, name='read'),
    path('videos/',views.VideosPage,name='videos'),
    path('add_video/',views.Add_videoPage,name='add_video'),
    path('watch/<int:videos_id>/', views.WatchPage, name='watch'),
    path('projects/',views.ProjectsPage,name='projects'),
    path('quiz/',views.QuizPage,name='quiz'),
    path('add_comment/',views.add_comment,name='add_comment'),
    path('logout/',views.LogoutPage,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
