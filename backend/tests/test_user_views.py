"""test module for users_views"""
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from backend.models.user_base import Student
# from backend.models.user_base import Admin

# class StudentViewTest(APITestCase):
#     """ test for student views """
#     def test_create_student(self):
#         """ test creating a student account"""
#         url = reverse('student-list')
#         data = {
#             'username': 'Kobe Bryant',
#             'password': 'iamagod',
#             'email': 'kb@goat.com'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Student.objects.count(), 1)
#         self.assertEqual(Student.objects.get().user.username, 'Kobe Bryant')

#     def test_get_students(self):
#         """ test getting a list of students """
#         url = reverse('student-list')
#         data = {
#             'username': 'LeBron James',
#             'password': 'iamagod2',
#             'email': 'lj@goat.com'
#         }
#         self.client.post(url, data, format='json')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)


# class StudentDetailTest(APITestCase):
#     """ test for student detail views """
#     def test_retrieve(self):
#         """ test retrieve student """
#         url1 = reverse('student-list')
#         data = {
#             'username': 'LeBron James',
#             'password': 'iamagod2',
#             'email': 'lj@goat.com'
#         }
#         response1 = self.client.post(url1, data, format='json')
#         # auth
#         url2 = reverse('account-auth')
#         data = {
#             'username': 'LeBron James',
#             'password': 'iamagod2'
#         }
#         response2 = self.client.post(url2, data, format='json')
#         self.assertEqual(response2.status_code, status.HTTP_200_OK)
#         self.assertEqual(response1.data['token'], response2.data['token'])
#         # get student detail
#         user_id = response2.data['user_id']
#         url3 = reverse('student-detail', args=[user_id])
#         response3 = self.client.get(url3)
#         self.assertEqual(response3.status_code, status.HTTP_200_OK)
#         self.assertEqual(response3.data['username'], response2.data['username'])

# class AdminListTest(APITestCase):
#     """ test for admin """
#     def test_create_admin(self):
#         """ test create admin """
#         url = reverse('admin-list')
#         data = {
#             'username': 'Kobe Bryant',
#             'password': 'iamagod',
#             'email': 'kb@goat.com'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Admin.objects.count(), 1)
#         self.assertEqual(Admin.objects.get().user.username, 'Kobe Bryant')

#     def test_get_admin(self):
#         """ test getting a list of admins"""
#         url = reverse('admin-list')
#         data = {
#             'username': 'LeBron James',
#             'password': 'iamagod2',
#             'email': 'lj@goat.com'
#         }
#         self.client.post(url, data, format='json')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
