"""test module for users_views"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.tests.utils import reset_database_permissions
from backend.tests.utils import activate_all_users
from backend.tests.utils import USER_DATA

class TestAuthview(APITestCase):
    """ test for user detail views """
    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_authentication(self):
        """ test authentication """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, USER_DATA, format='json')
        # activate
        activate_all_users()
        # auth
        url2 = reverse('account-auth')
        response2 = self.client.post(url2, USER_DATA, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
