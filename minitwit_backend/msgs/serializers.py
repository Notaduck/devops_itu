from rest_framework.serializers import Serializer
from msgs.models import Message
from rest_framework import serializers

class MessagesSerializer(Serializer): 
    class Meta:
        model = Message
        fields = ('text', 'pub_date', 'flagged')
    
    def create(self, validated_data): 
		message = Message(
            text = validated_data['text'],
            pub_date = validated_data['pub_date'],
            author_id = validated_data['user'].user_id,
            flagged = validated_data['flagged']
		)
		message.save()

