from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from msgs.models import Message
from auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer

# Create your views here.
class AddMessageAPIView(CreateApiView):
	# queryset = Message.objects.all()
	serializer_class = MessagesSerializer
	permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, user=request.auth)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

    def perform_create(self, serializer, user, no):
        serializer.save(user=user)

class GetMessagesAPIView(RetrieveAPIView):
	queryset = Message.objects.filter(author_id=request.)
    renderer_classes = [JSONRenderer]
	serializer_class = MessagesSerializer
	permission_classes = (IsAny,)
    

def messages(request):
    message = Message.objects.order_by('pub_date')
    return JsonResponse(list(message.values()), safe=False)

def messages_per_user(request, username):
    user = User.objects.get(username=username)
    messages = Message.objects.filter(author_id=user.user_id).order_by('pub_date')
    return JsonResponse(list(messages.values()), safe=False)
