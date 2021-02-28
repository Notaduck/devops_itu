from rest_framework.serializers import Serializer
from msgs.models import Message
from rest_framework import serializers
from users.models import User
import datetime

class MessagesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Message
        fields = ('text', 'author', 'pub_date', 'flagged')

    def create(self, validated_data): 
        message = Message(
            text = validated_data['text'],
            author = validated_data['author']
        )
        message.save()

        return message