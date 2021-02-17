from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from msgs.models import Message
from auth.models import User

# Create your views here.
def messages(request):
    message = Message.objects.order_by('pub_date')
    return JsonResponse(list(message.values()), safe=False)

def messages_per_user(request, username):
    user = User.objects.get(username=username)
    messages = Message.objects.filter(author_id=user.user_id).order_by('pub_date')
    return JsonResponse(list(messages.values()), safe=False)