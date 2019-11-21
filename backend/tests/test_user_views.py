"""test module for users_views"""
from copy import copy

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models import User

from backend.tests.utils import reset_database_permissions
from backend.tests.utils import activate_all_users

class UserListViewTest(APITestCase):
    """ test for user views """
    profile_data = {
        'school_name': 'THU',
    }
    user_data = {
        'email': 'kb@goat.com',
        'username': 'Kobe',
        'password': '11111111',
        'user_group': 'Admin',
    }

    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_create_student_without_profile(self):
        """ test creating an user account"""
        url = reverse('user-list')
        data = copy(self.user_data)
        response = self.client.post(url, data, format='json')
        user = User.objects.get(username='Kobe')
        user.user_group = 'Admin'
        user.save()
        user = User.objects.all()[0]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'Kobe')
        self.client.force_authenticate(user=user) #pylint: disable=no-member
        data['username'] = 'Byant'
        response = self.client.post(url, data, format='json')
        url = reverse('verification')
        self.client.get(url, {'username':'Byant'})
        url = reverse('password')
        self.client.put(url, {'password':'asdf'})

    def test_create_student_with_profile(self):
        """ test creating an user account"""
        url = reverse('user-list')
        data = copy(self.user_data)
        data['profile'] = self.profile_data

        response = self.client.post(url, data, format='json')

        user = User.objects.all()[0]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'Kobe')

    def test_get_user_list(self):
        """ test getting a list of students """
        url = reverse('user-list')
        data = copy(self.user_data)
        self.client.post(url, data, format='json')
        data['username'] = 'Lebron'
        self.client.post(url, data, format='json')
        user = User.objects.get(username='Lebron')
        user.user_group = 'Admin'
        user.save()
        self.client.force_authenticate(user=user) # pylint: disable=no-member
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class UserDetailTest(APITestCase):
    """ test for user detail views """
    user_data = {
        'email': 'kb@goat.com',
        'username': 'Kobe',
        'password': 'notagod',
        'user_group': 'Admin',
    }
    profile_data = {'school_name': 'THU', }

    @classmethod
    def setUpTestData(cls):
        reset_database_permissions()

    def test_retrieve(self):
        """ test retrieve user """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, self.user_data, format='json')
        # set user to be active
        activate_all_users()
        # auth
        url2 = reverse('account-auth')
        data = {
            'username': 'Kobe',
            'password': 'notagod'
        }
        response2 = self.client.post(url2, data, format='json')
        # get student detail
        user_id = response2.data['user']['id']
        url3 = reverse('user-detail', args=[user_id])
        user = User.objects.get(username='Kobe')
        self.client.force_authenticate(user=user) # pylint: disable=no-member
        response3 = self.client.get(url3)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.data['username'], response2.data['user']['username'])

    def test_update(self):
        """ test update user """
        # add user
        url1 = reverse('user-list')
        self.client.post(url1, self.user_data, format='json')
        # set user to be active
        activate_all_users()
        user = User.objects.get()
        # update user
        user_id = user.id
        url2 = reverse('user-detail', args=[user_id])
        data = {
            'username': 'Bryant',
            'email': 'c@d.com',
            'is_banned': True,
            'profile': {
                'school_name': 'PKU',
            }
        }
        # response = self.client.put(url2, data, format='json')
        user = User.objects.get(username='Kobe')
        self.client.force_authenticate(user=user) # pylint: disable=no-member
        response = self.client.put(url2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'Bryant')
        self.assertEqual(response.data['email'], 'c@d.com')
        self.assertEqual(response.data['is_banned'], True)
        self.assertEqual(response.data['profile']['school_name'], 'PKU')
