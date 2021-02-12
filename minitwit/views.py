from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction

from werkzeug import security # used only for user compatability between old system and new system

from .models import User, Follower, Message

def index(request):
	return HttpResponse(request.session.get('user_id', False))


def timeline(request, username = None):
	context = {'active_user' : None, 'profile_user': None, 'public': False, 'posts': []}
	if request.session.get('user_id', False):
		context['active_user'] = User.objects.get(user_id=request.session.get('user_id'))
	if username is not None:
		if username != context['active_user'].username:
			context['profile_user'] = User.objects.get(username=username)
		return user_timeline(request, context=context)
	return public_timeline(request, context)

def public_timeline(request, context):
	context['public'] = True
	context['posts'] = []
	return render(request, 'timeline.html', context = context)

def user_timeline(request, context):
	if context['profile_user']:
		context['posts'] = []
	else:
		context['posts'] = []
	return render(request, 'timeline.html', context = context)


def follow_user(request):
	pass


def unfollow_user(request):
	pass


def add_message(request):

	if request.method == 'POST':
		if not request.POST.get('text'):
				messages.add_message(request, messages.ERROR, 'Your message can not be empty')
				return redirect(timeline)

		message = Message(
			author_id = User.objects.get(user_id = request.session.get('user_id')),
			text = request.POST.get('text')
		)

		message.save()
		
		user_name = User.objects.get(pk = request.session.get('user_id')).username

		return redirect(timeline, username = user_name)



def login(request):
	if request.session.get('user_id', False):
		return redirect(timeline)
	if request.method == 'POST':
		user = User.objects.get(username=request.POST.get('username'))
		if user:
			if security.check_password_hash(user.pw_hash, request.POST.get('password')):
				request.session['user_id'] = user.pk
				messages.add_message(request, messages.INFO, 'You were logged in')
				return redirect(timeline)
		messages.add_message(request, messages.ERROR, 'Wrong password or username')
	return render(request, 'login.html')


def register(request):
	if request.session.get('user_id', False):
		return redirect(timeline)
	error = None
	if request.method == 'POST':
		if not request.POST.get('username'):
			messages.add_message(request, messages.ERROR, 'You have to enter a username')
		elif not request.POST.get('email') or '@' not in request.POST.get('email'):
			messages.add_message(request, messages.ERROR, 'You have to enter a valid email address')
		elif not request.POST.get('password'):
			messages.add_message(request, messages.ERROR, 'You have to enter a password')
		elif request.POST.get('password') != request.POST.get('password2'):
			messages.add_message(request, messages.ERROR, 'The two passwords do not match')
		elif User.objects.filter(username = request.POST.get('username')).exists():
			messages.add_message(request, messages.ERROR, 'The username is already taken')
		else:
			user = User(
				username = request.POST.get('username'),
				email = request.POST.get('email'),
				pw_hash = security.generate_password_hash(request.POST.get('password'))
			)
			user.save()
			messages.add_message(request, messages.INFO, 'You were succesfully registered and can login now')
			return redirect(login)
	return render(request, 'register.html')

def logout(request):
	if request.session.get('user_id', False):
		del request.session['user_id']
		messages.add_message(request, messages.INFO, 'You were logged out')
	return redirect(timeline)
