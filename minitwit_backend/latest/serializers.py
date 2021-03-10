from rest_framework import serializers
from latest.models import Lates

class LatestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Latest
    
    def update(self, instance, validated_data):
        instance.id = validated_data['latest']
        instance.save()
        return instance


