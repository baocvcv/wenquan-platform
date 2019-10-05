"""define admin models for app 'backend'"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import StudentChangeForm, StudentCreationForm
from .models import Student

class StudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ['email', 'username', 'password']

# Register your models here.
admin.site.register(Student, StudentAdmin)
