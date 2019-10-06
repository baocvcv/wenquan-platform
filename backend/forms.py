# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models.user_base import Student

class StudentCreationForm(UserCreationForm):
    
    class Meta:
        model = Student
        fields = ('username', 'email', 'password')

class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = UserChangeForm.Meta.fields
