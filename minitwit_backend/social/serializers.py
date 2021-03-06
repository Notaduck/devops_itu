from rest_framework.serializers import Serializer
from social.models import Follower
from rest_framework import serializers
from users.models import User

class FollowerSerializer(Serializer): 
    follow = serializers.CharField(source='whom')

    class Meta:
        model = Follower
        fields = ('who', 'whom')
    
    def create(self, validated_data): 
        follow = Follower(
            who = self.context['data']['who'],
            whom = self.context['data']['whom']
        )
        follow.save()
        return follow
