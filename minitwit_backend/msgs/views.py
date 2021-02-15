from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from msgs.models import Message
from auth.models import User

# Create your views here.
def get_all_messages(request):
    messages = list(Message.objects.all().values())
    return JsonResponse(messages, safe=False)