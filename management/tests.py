from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from management import views
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group, Permission
import pdb

# Create your tests here.

class UserTestCase(TestCase):

    register_url = reverse('signup')
    obtain_pair_url = reverse('access-token')

    create_user_data = {
    'username': 'Abc123',
    'password': 'DreDre101',
    'email': 'abc@gmail.com',
    'first_name': 'Alice',
    'last_name': 'Bob',
    'role': 'student'
    }

    login_data = {
        'username': 'Abc123',
        'password': 'DreDre101'
    }
    def test_creates_user(self):
        response = self.client.post(self.register_url, self.create_user_data,
        format='json')

        self.assertEqual(response.status_code, 201)
        user = User.objects.get(email = response.data['email'])

        self.assertEqual(user.username, 'Abc123')

    def test_logins_user_successfully(self):
        create_response = self.client.post(self.register_url, self.create_user_data,
        format='json')
        login_response = self.client.post(self.obtain_pair_url, self.login_data,
        format='json')

        self.assertEqual(login_response.status_code, 200)

    def test_checks_usergroup(self):
        response = self.client.post(self.register_url, self.create_user_data,
        format='json')

        user = User.objects.get(email = response.data['email'])


        grp = user.groups.filter(name='student')
        self.assertEqual(user.groups.filter(name='student').exists(), True)
