from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from social.models import Follower
from users.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from social.serializers import FollowerSerializer
from rest_framework import status
from rest_framework.response import Response


class FollowView(CreateAPIView, DestroyAPIView):
	serializer_class = FollowerSerializer
	permission_classes = (IsAuthenticated,)

	def post(self, request, username, *args, **kwargs):
		if request.POST.get('follow', False):
			whoExists = User.objects.filter(username = username).exists()
			whomExists = User.objects.filter(username = request.POST.get('follow')).exists()

			if not whoExists or not whomExists:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			who = User.objects.get_by_natural_key(username)
			whom = User.objects.get_by_natural_key(request.POST.get('follow'))

			if Follower.objects.filter(who = who, whom = whom).exists() or who == whom:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			return self.create(request, username, *args, **kwargs)
			
		if request.POST.get('unfollow', False):
			whoExists = User.objects.filter(username = username).exists()
			whomExists = User.objects.filter(username = request.POST.get('unfollow')).exists()

			if not whoExists or not whomExists:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			who = User.objects.get_by_natural_key(username)
			whom = User.objects.get_by_natural_key(request.POST.get('unfollow'))

			if Follower.objects.filter(who = who, whom = whom).exists() or who == whom:
				return self.destroy(request, username, *args, **kwargs)
		print("4")
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	def create(self, request, username, *args, **kwargs):
		serializer = self.get_serializer(data=request.data, context={'username': username})
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
	
	def destroy(self, request, username, *args, **kwargs):
		instance = Follower.objects.get(who = User.objects.get_by_natural_key(username), whom = User.objects.get_by_natural_key(request.POST.get('unfollow')))
		self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)

