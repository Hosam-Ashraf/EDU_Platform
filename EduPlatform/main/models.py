
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Custom fields and methods for your user model
    
    groups = models.ManyToManyField(
        Group,
        related_name='hosam',  # Update related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='younus',  # Update related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.'
    )

# Teacher Model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    RANK_CHOICES = (
        ('fwd', 'FWD Method'),
        ('mini_group', 'Mini Group'),
        ('personal', 'Personal Education'),
    )
    rank = models.CharField(max_length=20, choices=RANK_CHOICES, default='fwd')

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_type = models.CharField(max_length=50, choices=(('personal', 'Personal Education'), ('mini_group', 'Mini Group'), ('fwd', 'FWD Method')))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

# Lesson Model
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(max_length=500, blank=True, null=True)  # YouTube link
    drive_link = models.URLField(max_length=500, blank=True, null=True)  # Google Drive link
    week_number = models.PositiveIntegerField()

# Exam Model
class Exam(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    exam_content = models.TextField()
    passing_score = models.IntegerField()

# Payment Model
class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='earnings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    platform_fee = models.DecimalField(max_digits=5, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
