from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, Lesson, Payment
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.conf import settings
from django.views.static import serve as static_serve

# main/views.py
from django.shortcuts import render

# EduPlatform/main/views.py

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def form_valid(self, form):
        role = form.cleaned_data.get('role')
        
        # Redirect based on role
        if role == 'teacher':
            return redirect('teacher_dashboard')  # Replace with your teacher dashboard URL
        elif role == 'student':
            return redirect('student_dashboard')  # Replace with your student dashboard URL

        return super().form_valid(form)

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def home(request):
    return render(request, 'home.html')

def serve_media(request, path):
    return static_serve(request, path, document_root=settings.MEDIA_ROOT)

# Course List View
@login_required
def course_list(request, program_type):
    courses = Course.objects.filter(course_type=program_type)
    return render(request, 'main/course_list.html', {'courses': courses})

# Teacher Suggestion View
@login_required
def suggest_teachers(request, program_type):
    teachers = Teacher.objects.filter(rank=program_type)
    return render(request, 'main/teacher_suggestions.html', {'teachers': teachers})
