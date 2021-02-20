import base64
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from requests.auth import HTTPBasicAuth
from users.models import User

class UserAuthenticationTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		User.objects.create(username='test', email='test@test.test', password='test')

	def test_user_creation(self):
		User.objects.create(username='createTest', email='createTest@test.test', password='test')
		self.assertTrue(User.objects.filter(username='createTest').exists())
		createTest = User.objects.get(username='createTest')
		self.assertEqual(createTest.username, 'createTest')
		self.assertEqual(createTest.email, 'createTest@test.test')
		self.assertEqual(createTest.password, 'test')

	def test_user_registration(self):
		url = reverse('register')
		data = {
			'username': 'RegistrationTest',
			'email': 'RegistrationTest@test.test',
			'pwd': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 204)

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
		data['username'] = 'uniquetest'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 204)
