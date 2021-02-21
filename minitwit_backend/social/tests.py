from django.test import TestCase

# Create your tests here.
import base64
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from requests.auth import HTTPBasicAuth
from users.models import User


def create_user(username, email, password):
	user = User.objects.create(username=username, email=email)
	user.set_password(password)
	user.save()

class FollowTestCase(APITestCase):
	def setUp(self):
		create_user('who', 'test@test.test', 'test')
        create_user('whom', 'tf@test.test', 'test')

    def test_follow(self):
        url = reverse('follow/whom')
        self.
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

	def test_user_authentication(self):
		url = reverse('getcurrentuser')
		self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode('test:test'.encode('ascii')).decode()))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)