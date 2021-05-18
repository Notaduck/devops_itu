import base64
from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from users.tests import create_user, login_user

class UserAuthenticationTestCase(TestCase):
	def setUp(self):
		create_user('test', 'test@test.test', 'test')


	def test_signin_redirect(self):
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('personal_timeline').rstrip('/'))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('personal_timeline').rstrip('/'))


	def test_anonymous_personal_timeline(self):
		url = reverse('personal_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)


	def test_anonymous_public_timeline(self):
		url = reverse('public_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)


	def test_personal_timeline(self):
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)
		url = reverse('personal_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)


	def test_public_timeline(self):
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)
		url = reverse('public_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)