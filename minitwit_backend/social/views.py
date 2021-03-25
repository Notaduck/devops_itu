from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from social.models import Follower
from users.models import User
from django.http import HttpResponse, HttpResponseBadRequest, QueryDict
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from social.serializers import FollowerSerializer
from rest_framework import status
from rest_framework.response import Response
from minitwit_backend.metrics import Metrics


class FollowView(CreateAPIView, DestroyAPIView):
	queryset = Follower.objects.all()
	serializer_class = FollowerSerializer
	permission_classes = (IsAuthenticated,)


	def post(self, request, username, *args, **kwargs):
		if User.objects.filter(username = username).exists():
			who = User.objects.get(username=username)

		if request.data.get('follow', False) and User.objects.filter(username=request.data.get('follow')).exists():
			whom = User.objects.get_by_natural_key(request.data.get('follow'))

			if Follower.objects.filter(who = who, whom = whom).exists() or who == whom:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			return self.create(request, username, who, whom, *args, **kwargs)

		if request.data.get('unfollow', False) and User.objects.filter(username=request.data.get('unfollow')).exists():
			whom = User.objects.get(username=request.data.get('unfollow'))

			if Follower.objects.filter(who = who, whom = whom).exists():
				return self.destroy(request, username, who, whom, *args, **kwargs)
			else:
				# return 204 because weird api specifications from helge
				return Response(status=status.HTTP_204_NO_CONTENT)
		else: 
			return Response(status=status.HTTP_400_BAD_REQUEST)
	

	def create(self, request, username, who, whom, *args, **kwargs):
		data = request.data.copy()
		data['who'] = who
		data['whom'] = whom
		serializer = self.get_serializer(data=request.data, context={'data': data})
		serializer.is_valid(raise_exception=False)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		# update metrics
		Metrics.inserts_total.labels("follower").inc()
		return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
	

	def destroy(self, request, username, who, whom, *args, **kwargs):
		instance = Follower.objects.get(who=who, whom=whom)
		self.perform_destroy(instance)
		# update metrics
		Metrics.deletes_total.labels("follower").inc()
		return Response(status=status.HTTP_204_NO_CONTENT)
