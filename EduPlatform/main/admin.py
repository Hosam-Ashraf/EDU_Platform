from django.contrib import admin
from .models import User, Teacher, Course, Lesson, Exam, Payment

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Exam)
admin.site.register(Payment)
