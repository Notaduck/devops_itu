import base64
from django.test import TestCase, Client
from django.urls import reverse
from requests.auth import HTTPBasicAuth
from users.models import User


def create_user(username, email, password):
	user = User.objects.create(username=username, email=email)
	user.set_password(password)
	user.save()
	return user


def login_user(client, username, password):
	url = reverse('login')
	data = {
		'username': username,
		'password': password
	}
	return client.post(url, data=data)


class UserAuthenticationTestCase(TestCase):
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
			'password1': 'test',
			'password2': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertTrue(User.objects.filter(username='RegistrationTest').exists())
		self.assertEqual(response.url, reverse('login'))


	def test_user_uniqueness_on_registration(self):
		url = reverse('register')
		data = {
			'username': 'test',
			'email': 'test@test.test',
			'password1': 'test',
			'password2': 'test'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'uniquetest'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'test'
		data['email'] = 'uniquetest@test.test'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'uniquetest'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('login'))


	def test_user_authentication(self):
		url = reverse('login')
		data = {
			'username': 'testWrong',
			'password': 'testWrong'
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'test'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'testWrong'
		data['password'] = 'test'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 200)
		data['username'] = 'test'
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('personal_timeline').rstrip('/'))


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