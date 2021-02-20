from django.urls import reverse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer

class RegisterView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

class GetCurrentUser(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,)

	def retrieve(self, request, *args, **kwargs):
		instance = request.user
		serializer = self.get_serializer(instance)
		serializer.data.pop('pwd')
		return Response(serializer.data)
