from rest_framework.serializers import Serializer
from social.models import Follower
from rest_framework import serializers

class FollowerSerializer(Serializer): 
    class Meta:
        model = Follower
        fields = ('who', 'whom')
    
    def create(self, validated_data): 
        follow = Follower(
            who = validated_data['user'].user_id,
            whom = validated_data['user'].user_id
        )
        follow.save()