"""
URL configuration for EduPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# EduPlatform/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from main import views as main_views
from main.views import CustomLoginView, teacher_dashboard, student_dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),

    path('courses/<str:program_type>/', main_views.course_list, name='course_list'),
    path('teachers/<str:program_type>/', main_views.suggest_teachers, name='suggest_teachers'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Use built-in LoginView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('media/<path:path>/', main_views.serve_media, name='serve_media'),
    path('', main_views.home, name='home'),  # Root URL
]

