from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from management import views
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group, Permission
import pdb

# Create your tests here.

class SchoolTestCase(TestCase):

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

    def test_creates_user(self):
        response = self.client.post(self.register_url, self.create_user_data,
        format='json')

        self.assertEqual(response.status_code, 201)
        user = User.objects.get(email = response.data['email'])

        self.assertEqual(user.username, 'Abc123')
