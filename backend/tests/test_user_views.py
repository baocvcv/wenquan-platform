"""test module for users_views"""
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from backend.models.user_base import *

class StudentViewTest(APITestCase):
    """ test for student views """

    def test_create_student(self):
        """ test creating a student account"""
        url = reverse('student-list')
        data = {
            'username': 'Kobe Bryant',
            'password': 'iamagod',
            'email': 'kb@goat.com',
            
        }
