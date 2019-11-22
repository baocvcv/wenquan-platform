"""test module for users_views"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models import EmailVerificationRecord
from backend.tests.utils import reset_database_permissions
from backend.tests.utils import USER_DATA

class TestVerificationView(APITestCase):
    """ test for user detail views """
    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_verification(self):
        """ test authentication """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, USER_DATA, format='json')
        # authentication
        url2 = reverse('account-auth')
        response1 = self.client.post(url2, USER_DATA, format='json')
        # not activated
        self.assertEqual(response1.status_code, status.HTTP_403_FORBIDDEN)
        # activate
        url3 = reverse('verification')
        verification_token = EmailVerificationRecord.objects.get().token
        data = {'token': verification_token}
        response2 = self.client.post(url3, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        # auth again
        response3 = self.client.post(url2, USER_DATA, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
