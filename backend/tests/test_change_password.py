"""test module for users_views"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models import EmailVerificationRecord
from backend.tests.utils import activate_all_users
from backend.tests.utils import reset_database_permissions
from backend.tests.utils import USER_DATA

class TestChangePasswordView(APITestCase):
    """ test for user detail views """
    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_change_password(self):
        """ test authentication """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, USER_DATA, format='json')
        # activate
        activate_all_users()
        # login
        self.client.login(username=USER_DATA['username'], password=USER_DATA['password'])
        # get change password token
        url2 = reverse('password')
        response2 = self.client.get(url2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        # change passwd
        verification_token = EmailVerificationRecord.objects.get(send_type='forget').token
        data = {'token': verification_token, 'password': 'abcd1111'}
        response3 = self.client.post(url2, data, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        # auth again
        USER_DATA['password'] = 'abcd1111'
        url3 = reverse('account-auth')
        response4 = self.client.post(url3, USER_DATA, format='json')
        self.assertEqual(response4.status_code, status.HTTP_200_OK)
        self.client.logout()
