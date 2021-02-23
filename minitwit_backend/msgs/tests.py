import base64
import json
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.core.serializers import serialize
from rest_framework.test import APIClient, APITestCase
from users.models import User
from msgs.models import Message

# Create your tests here.
def create_user(username, email, password):
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def create_message(text, user):
    message = Message(
        text = text,
        author = user
    )
    message.save()
    return message

class GetMessagesTestCase(APITestCase):
    def setUp(self):
        user0 = create_user('test0', 'test0@test.test', 'test')
        user1 = create_user('test1', 'test1@test.test', 'test')
        user2 = create_user('test2', 'test2@test.test', 'test')

        create_message('the user \'test0\' is making its first post', user0)
        create_message('the user \'test0\' is making its first post', user0)
        create_message('the user \'test0\' is making its third post', user0)
        create_message('the user \'test0\' is making its fourth post', user0)
        create_message('the user \'test0\' is making its fifth post', user0)
        create_message('the user \'test0\' is making its sixth post', user0)

        create_message('the user \'test1\' is making its first post', user1)
        create_message('the user \'test1\' is making its second post', user1)
        
        create_message('the user \'test2\' is making its first post', user2)


    def compareMessageDictToModel(self, dictionary, modelObj):
        dt = datetime.datetime.strptime(dictionary['pub_date'] + "+0000", '%Y-%m-%dT%H:%M:%S.%fZ%z')
        return dictionary['text'] == modelObj.text and \
                dictionary['author'] == modelObj.author.id and \
                dictionary['flagged'] == modelObj.flagged and \
                dt == modelObj.pub_date


    def test_count_all_messages(self):
        # query the server
        url = reverse('all_messages')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # check the number of messages received
        data = json.loads(response.content)
        self.assertEqual(len(Message.objects.all()), len(data))


    def test_count_messages_per_user(self):
        # query the server
        url = reverse('messages_per_user', args=['test0'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # check the number of messages received
        data = json.loads(response.content)
        user = User.objects.get(username='test0')
        self.assertEqual(len(Message.objects.filter(author=user)), len(data))
        

    def test_messages_per_invalid_user(self):
        # query the server
        url = reverse('messages_per_user', args=['test'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)


    def test_messages_content(self):
        # query the server for all_messages and messages_per_user
        url = reverse('all_messages')
        response_all = self.client.get(url)
        url = reverse('messages_per_user', args=['test0'])
        response_per_user = self.client.get(url)
        self.assertEqual(response_all.status_code, 200)
        self.assertEqual(response_per_user.status_code, 200)

        # arrange the data
        data_all = json.loads(response_all.content)
        expected_values_all = Message.objects.all().order_by('-pub_date')

        data_per_user = json.loads(response_per_user.content)
        user = User.objects.get(username='test0')
        expected_values_per_user = Message.objects.filter(author=user).order_by('-pub_date')

        # check the contents of the received messages 
        for i in range(len(expected_values_all)):
            self.assertTrue(self.compareMessageDictToModel(data_all[i], expected_values_all[i]))

        for i in range(len(expected_values_per_user)):
            self.assertTrue(self.compareMessageDictToModel(data_per_user[i], expected_values_per_user[i]))


    def test_limit_number_of_messages(self):
        # query the server for all_messages and messages_per_user
        number_of_responses_all = 6
        number_of_responses_per_user = 3
        url = reverse('all_messages')
        response_all = self.client.get(url, data={'no': number_of_responses_all})
        url = reverse('messages_per_user', args=['test0'])
        response_per_user = self.client.get(url, data={'no': number_of_responses_per_user} )
        self.assertEqual(response_all.status_code, 200)
        self.assertEqual(response_per_user.status_code, 200)

        # arrange the data
        data_all = json.loads(response_all.content)
        data_per_user = json.loads(response_per_user.content)

        # check the number of messages received
        self.assertEqual(number_of_responses_all, len(data_all))
        self.assertEqual(number_of_responses_per_user, len(data_per_user))


    def test_add_message_increments_count(self):
        # query the server
        oldMessageCount = Message.objects.count()		
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode('test0:test'.encode('ascii')).decode()))
        url = reverse('add_message', args=['test0'])
        response = self.client.post(url, { 'text': 'this is a test message' })
        self.assertEqual(response.status_code, 204)

        # check that the message count has increased
        self.assertEqual(oldMessageCount + 1, len(Message.objects.all()))


    def test_add_message_and_get_message(self):
        # query the server
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(base64.b64encode('test0:test'.encode('ascii')).decode()))
        url = reverse('add_message', args=['test0'])
        response_post = self.client.post(url, { 'text': 'this is another very cool test message' })
        # the response object returns a datetime object in the pub_date field. replace it with a string
        response_post.data['pub_date'] = response_post.data['pub_date'].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        print(self.compareMessageDictToModel(response_post.data, Message.objects.latest('pub_date')))
        self.assertEqual(response_post.status_code, 204)

        # query the server again for the posted message
        url = reverse('messages_per_user', args=['test0'])
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        # check the values of the messages
        self.assertTrue(self.compareMessageDictToModel(response_post.data, Message.objects.latest('pub_date')))
        self.assertJSONEqual(json.dumps(response_post.data), json.loads(response_get.content)[0])


    def test_add_message_no_auth(self):
        pass
