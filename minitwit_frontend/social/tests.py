from django.test import TestCase, Client
from django.urls import reverse

from users.tests import create_user, login_user
from users.models import User
from msgs.models import Message
from social.models import Follower
from users.tests import create_user, login_user
from msgs.tests import create_message


def create_follower(who, whom):
	follower = Follower(who=who, whom=whom)
	follower.save()
	return follower


class FollowerTestCase(TestCase):
	def setUp(self):
		user0 = create_user('test0', 'test0@test.test', 'test')
		user1 = create_user('test1', 'test1@test.test', 'test')
		user2 = create_user('test2', 'test2@test.test', 'test')
		user3 = create_user('test3', 'test3@test.test', 'test')
		user4 = create_user('test4', 'test4@test.test', 'test')

		message0 = create_message('the user test0 is making its first post', user0)
		message1 = create_message('the user test1 is making its first post', user1)
		message2 = create_message('the user test0 is making its second post', user0)
		message3 = create_message('the user test2 is making its first post', user2)
		message4 = create_message('the user test2 is making its second post', user2)
		message5 = create_message('the user test1 is making its second post', user1)
		message6 = create_message('the user test0 is making its third post', user0)
		self.messages = {'user0':[message0, message2, message6], 'user1':[message2, message5], 'user2':[message3, message4]}


	def test_follow(self):
		login_user(self.client, 'test0', 'test')
		url = '/timeline/test1'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are not yet following this user.', count=1)
		self.assertFalse(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		response = self.client.get('/follow/test1/')
		self.assertTrue(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		self.assertEqual(response.status_code, 302)
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are currently following this user.', count=1)


	def test_unfollow(self):
		login_user(self.client, 'test0', 'test')
		url = '/timeline/test1'
		self.test_follow()
		response = self.client.get('/unfollow/test1/')
		self.assertFalse(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		self.assertEqual(response.status_code, 302)
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are not yet following this user.', count=1)


	def test_personal_timeline_includes_followed(self):
		url = reverse('personal_timeline')

		def count_messages_per_user(counts):
			response = self.client.get(url)
			self.assertEqual(response.status_code, 200)
			for k,v in counts.items():
				self.assertContains(response, k, count=v)


	def messages_content(msgs):
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		for msg in msgs:
			self.assertContains(response, msg.text, count=1)

		login_user(self.client, 'test0', 'test')
		counts = {'test0':10, 'test1':0, 'test2':0}
		count_messages_per_user(counts)
		self.test_follow()
		counts['test1'] = 6
		count_messages_per_user(counts)
		messages = self.messages['user0']+self.messages['user1']
		messages_content(messages)


	def test_follow_unauthenticated(self):
		url = '/timeline/test1'
		
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are not yet following this user.', count=0)
		self.assertFalse(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		
		response = self.client.get('/follow/test1/')
		self.assertFalse(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		self.assertEqual(response.status_code, 400) # Maybe different error code
		
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are not yet following this user.', count=0)


	def test_unfollow_unauthenticated(self):
		"""NOT FULLY IMPLEMENTED: Need to logout after self.test_follow()"""
		url = '/timeline/test1'
		self.test_follow()
		# Log out here before assertions

		response = self.client.get('/unfollow/test1/')
		self.assertFalse(Follower.objects.filter(who=User.objects.get_by_natural_key('test0'), whom=User.objects.get_by_natural_key('test1')).exists())
		self.assertEqual(response.status_code, 400) # Maybe different error code
		
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are not yet following this user.', count=0)


	def test_follow_invalid_user(self):
		url = '/follow/thisuserdoesnotexist'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 400)


	def test_unfollow_invalid_user(self):
		url = '/unfollow/thisuserdoesnotexist'
		response = self.client.get(url)
		self.assertEqual(response.status_code, 400)


	def test_follow_while_already_following(self):
		login_user(self.client, 'test0', 'test')
		url = '/timeline/test1'
		
		response = self.client.get('/follow/test1/')
		response = self.client.get('/follow/test1/')

		self.assertEqual(response.status_code, 400)

		
	def test_unfollow_while_not_following(self):
		login_user(self.client, 'test0', 'test')
		url = '/timeline/test1'
		
		response = self.client.get('/unfollow/test1/')

		self.assertEqual(response.status_code, 400)
		