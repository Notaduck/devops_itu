import json
import datetime
from django.test import TestCase, Client
from django.urls import reverse

from users.tests import create_user, login_user
from users.models import User
from msgs.models import Message
from social.models import Follower

def create_message(text, user):
	message = Message(author=user, text=text)
	message.save()
	return message


class GetMessagesTestCase(TestCase):
	def setUp(self):
		user0 = create_user('test0', 'test0@test.test', 'test')
		user1 = create_user('test1', 'test1@test.test', 'test')
		user2 = create_user('test2', 'test2@test.test', 'test')

		message0 = create_message('the user test0 is making its first post', user0)
		message1 = create_message('the user test1 is making its first post', user1)
		message2 = create_message('the user test0 is making its second post', user0)
		message3 = create_message('the user test2 is making its first post', user2)
		message4 = create_message('the user test2 is making its second post', user2)
		message5 = create_message('the user test1 is making its second post', user1)
		message6 = create_message('the user test0 is making its third post', user0)
		self.messages = [message0, message1, message2, message3, message4, message5, message6]


	def test_count_all_messages_on_public_timeline(self):
		url = reverse('public_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'http://www.gravatar.com/avatar', count=len(self.messages))


	def test_count_messages_per_user(self):
		url = reverse('public_timeline')
		response = self.client.get(url)
		counts = {'test0':3, 'test1':2, 'test2':2}
		self.assertEqual(response.status_code, 200)
		for k,v in counts.items():
			self.assertContains(response, k, count=v*3)


	def test_messages_content(self):
		url = reverse('public_timeline')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		for msg in self.messages:
			self.assertContains(response, msg.text, count=1)
