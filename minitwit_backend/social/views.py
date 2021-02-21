from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from social.models import Follower
from users.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from social.serializers import FollowerSerializer


class FollowView(CreateAPIView):
	serializer_class = FollowerSerializer
	permission_classes = (IsAuthenticated,)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer, user=request.auth)
		headers = self.get_success_headers(serializer.data)
		return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

	def perform_create(self, serializer, user, no):
		serializer.save(user=user)

class UnfollowView(CreateAPIView):
	pass
