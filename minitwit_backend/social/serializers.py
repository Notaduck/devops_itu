from rest_framework.serializers import Serializer
from social.models import Follower
from rest_framework import serializers
from users.models import User

class FollowerSerializer(Serializer): 
    follow = serializers.CharField(source='whom')

    class Meta:
        model = Follower
        fields = ('whom')
    
    def create(self, validated_data): 
        follow = Follower(
            who = User.objects.get_by_natural_key(self.context.pop('username')),
            whom = User.objects.get_by_natural_key(validated_data.pop('whom'))
        )
        follow.save()
        return follow
