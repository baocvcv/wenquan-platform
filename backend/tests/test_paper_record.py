"""test module for users_views"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.tests.utils import reset_database_permissions
from backend.models import User
# import reset_permissions
# from fakeData import createUser

# class TestPaperRecord(APITestCase):
#     """ test for user detail views """
#     @classmethod
#     def setUpTestData(cls):
#         reset_database_permissions()

#     def test_post(self):
#         "test post"
#         url1 = reverse('paper_record_list')
#         self.client.force_authenticate() # pylint: disable=no-member
#         # self.client.post(url1)

#     def test_get(self):
#         "Test get"
#         createUser(username='cyx', user_group='Admin')
#         user = User.objects.get(username='cyx')
#         self.client.force_authenticate(user=user) # pylint: disable=no-member
#         url2 = reverse('paper_record_detail', args=[1])
#         # self.client.get(url2)
#         createUser(username='xq', user_group='Student')
#         user = User.objects.get(username='xq')
#         self.client.force_authenticate(user=user) # pylint: disable=no-member
#         # self.client.get(url2)
