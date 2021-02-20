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

class UserAuthenticationTestCase(APITestCase):
	def setUp(self):
		create_user('test', 'test@test.test', 'test')

	def test_user_creation(self):
		create_user('createTest', 'createTest@test.test', 'test')
		self.assertTrue(User.objects.filter(username='createTest').exists())
		createTest = User.objects.get(username='createTest')
		self.assertEqual(createTest.username, 'createTest')
		self.assertEqual(createTest.email, 'createTest@test.test')

	def test_user_registration(self):
		url = reverse('register')
		data = {
			'username': 'RegistrationTest',
			'email': 'RegistrationTest@test.test',
			'pwd': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 204)
		self.assertTrue(User.objects.filter(username='RegistrationTest').exists())

	def test_user_uniqueness_on_registration(self):
		url = reverse('register')
		data = {
			'username': 'test',
			'email': 'test@test.test',
			'pwd': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 400)
		data['username'] = 'uniquetest'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 400)
		data['username'] = 'test'
		data['email'] = 'uniquetest@test.test'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 400)
		data['username'] = 'uniquetest'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 204)

	def test_user_authentication(self):
		url = reverse('getcurrentuser')
		self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode('test:test'.encode('ascii')).decode()))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
