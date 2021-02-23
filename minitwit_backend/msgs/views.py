from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from msgs.models import Message
from users.models import User
from msgs.serializers import MessagesSerializer
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework import status, permissions, exceptions, pagination
from rest_framework.response import Response
import datetime
                

class IsReadOnlyRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsPostRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST"


class MessagesListCreateView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated|IsReadOnlyRequest]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        if('username' in self.kwargs):
            username = self.kwargs['username']
            if not User.objects.filter(username=username).exists():
                raise exceptions.ValidationError({'error': ['The requested user does not exist']})

            user = User.objects.get(username=username)
            self.queryset = Message.objects.filter(author=user)
        else:
            self.queryset = Message.objects.all()

        if('no' in self.request.GET):    
            # self.pagination_class.default_limit = self.request.query_params['no']
            limit = int(self.request.GET['no'])
            return self.queryset.order_by('-pub_date')[:limit]
        else:
            self.paginate_by = None 
            return self.queryset.order_by('-pub_date')
        

    def create(self, request, username, *args, **kwargs):
        if not User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['author'] = User.objects.get_by_natural_key(username).pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # fields = serializer.get_fields()
        responseData= { 
            'text': instance.text,
            'author': serializer.validated_data['author'].pk,
            'pub_date': instance.pub_date,
            'flagged': instance.flagged
        }
        return Response(status=status.HTTP_204_NO_CONTENT, headers=headers, data=responseData)

    def perform_create(self, serializer):
        return serializer.save()
