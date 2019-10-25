"""test module for users_views"""
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.tests.utils import reset_database_permissions
from backend.tests.utils import activate_all_users

class TestAuthview(APITestCase):
    """ test for user detail views """
    user_data = {
        'email': 'kb@goat.com',
        'username': 'Kobe',
        'password': '1234abcd',
        'user_group': 'Student',
    }
    profile_data = {
        'school_name': 'THU',
    }

    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_authentication(self):
        """ test authentication """
        # add user
        url1 = reverse('user-list')
        response1 = self.client.post(url1, self.user_data, format='json')
        # activate
        activate_all_users()
        # auth
        url2 = reverse('account-auth')
        data = {
            'username': 'Kobe',
            'password': '1234abcd'
        }
        response2 = self.client.post(url2, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.data['token'], response2.data['token'])
