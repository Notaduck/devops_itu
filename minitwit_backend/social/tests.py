from django.test import TestCase

import base64
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from requests.auth import HTTPBasicAuth
from users.models import User
from social.models import Follower


def create_user(username, email, password):
	user = User.objects.create(username=username, email=email)
	user.set_password(password)
	user.save()

class FollowTestCase(APITestCase):

    def setUp(self):
        create_user('a', 'a@a.test', 'a')
        create_user('b', 'b@b.test', 'b')
    
    def test_follow_user(self):

        username = 'a'
        password = 'a'

        url = f'/fllws/{username}'
        data = {'follow': 'b'}

        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode(f'{username}:{password}'.encode('ascii')).decode()))
        response = self.client.post(url, data=data)

        
        self.assertEqual(response.status_code, 204)

        who = User.objects.get_by_natural_key(username)
        whom = User.objects.get_by_natural_key('b')
        
        self.assertTrue(Follower.objects.filter(who = who, whom = whom).exists())

    def test_a_unfollow_b(self):
        username = 'a'
        password = 'a'

        url = f'/fllws/{username}'
        data = {'follow': 'b'}

        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode(f'{username}:{password}'.encode('ascii')).decode()))
        response = self.client.post(url, data=data)

        url = f'/fllws/{username}'
        data = {'unfollow': 'b'}

        response = self.client.post(url, data=data)

        
        self.assertEqual(response.status_code, 204)

        who = User.objects.get_by_natural_key(username)
        whom = User.objects.get_by_natural_key('b')
        
        self.assertTrue(not Follower.objects.filter(who = who, whom = whom).exists())
