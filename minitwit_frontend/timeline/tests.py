import base64
from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from users.tests import create_user, login_user

class UserAuthenticationTestCase(TestCase):
	def setUp(self):
		create_user('test', 'test@test.test', 'test')
		create_user('test2', 'test2@test.test', 'test')


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


	def test_nav_bar_logged_in(self):
		html1 = '<a href="/timeline/">my timeline</a>'
		html2 = '<a href="/">public timeline</a>'
		html3 = '<a href="/logout">sign out</a>'

		html4 = '<a href="/register">sign up</a>'
		html5 = '<a href="/login">sign in</a>'
		
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)

		url = reverse('public_timeline')
		response = self.client.get(url)
		
		self.assertContains(response, html1)
		self.assertContains(response, html2)
		self.assertContains(response, html3)
		self.assertNotContains(response, html4)
		self.assertNotContains(response, html5)


	def test_nav_bar_without_login(self):
		html1 = '<a href="/">public timeline</a>'
		html2 = '<a href="/register">sign up</a>'
		html3 = '<a href="/login">sign in</a>'

		html4 = '<a href="/timeline/">my timeline</a>'
		html5 = '<a href="/logout">sign out</a>'
		
		url = reverse('public_timeline')
		response = self.client.get(url)
		
		self.assertContains(response, html1)
		self.assertContains(response, html2)
		self.assertContains(response, html3)
		self.assertNotContains(response, html4)
		self.assertNotContains(response, html5)
	
	
	def test_nav_bar_after_logged_out(self):
		html1 = '<a href="/">public timeline</a>'
		html2 = '<a href="/register">sign up</a>'
		html3 = '<a href="/login">sign in</a>'
		
		#LogIn
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)

		#LogOut
		url = reverse('logout')
		response = self.client.get(url)
		
		#Test timeline
		url = reverse('public_timeline')
		response = self.client.get(url)
		self.assertContains(response, html1)
		self.assertContains(response, html2)
		self.assertContains(response, html3)
	
	
	def test_nav_bar_logged_in_personal_timeline(self):
		html1 = '<a href="/timeline/">my timeline</a>'
		html2 = '<a href="/">public timeline</a>'
		html3 = '<a href="/logout">sign out</a>'

		html4 = '<a href="/register">sign up</a>'
		html5 = '<a href="/login">sign in</a>'
		
		url = reverse('login')
		data = {
			'username': 'test',
			'password': 'test'
		}
		response = self.client.post(url, data=data)

		url = reverse('personal_timeline')
		response = self.client.get(url)
		
		self.assertContains(response, html1)
		self.assertContains(response, html2)
		self.assertContains(response, html3)
		self.assertNotContains(response, html4)
		self.assertNotContains(response, html5)

	def test_access_timeline_of_known_username(self):
		url = '/timeline/test'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_access_timeline_of_unknown_username(self):
		url = '/timeline/thisuserdoesnotexist'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 400)
		#TODO: Bad request or return to public?