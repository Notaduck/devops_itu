from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
	pwd = serializers.CharField(source='password')

	class Meta:
		model = User
		fields = ('username', 'email', 'pwd')

	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		user.set_unusable_password()
		return user
