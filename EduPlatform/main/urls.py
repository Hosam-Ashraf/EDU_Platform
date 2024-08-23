from django.urls import path
from . import views

urlpatterns = [
    path('courses/<str:program_type>/', views.course_list, name='course_list'),
    path('teachers/<str:program_type>/', views.suggest_teachers, name='suggest_teachers'),
]
