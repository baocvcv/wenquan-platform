"""test module for users_views"""
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.tests.utils import reset_database_permissions

class TestVerificationView(APITestCase):
    """ test for user detail views """
    user_data = {
        'email': 'kb@goat.com',
        'username': 'Jack',
        'password': '1234abcd',
        'user_group': 'Student',
    }
    profile_data = {
        'school_name': 'PKU',
    }

    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_verification(self):
        """ test authentication """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, self.user_data, format='json')
        # authentication
        url2 = reverse('account-auth')
        data = {
            'username': 'Jack',
            'password': '1234abcd'
        }
        response1 = self.client.post(url2, data, format='json')
        # not activated
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        # activate
        url3 = reverse('verification')
        verification_token = EmailVerificationRecord.objects.get().token
        data = {'token': verification_token}
        response2 = self.client.put(url3, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        # auth again
        data = {'username': 'Jack', 'password': '1234abcd'}
        response3 = self.client.post(url2, data, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
