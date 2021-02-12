from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from werkzeug import security # used only for user compatability between old system and new system

from . import models

def index(request):
	return HttpResponse(request.session.get('user_id', False))


def timeline(request, username = None):
	context = {'active_user' : None, 'profile_user': None, 'public': False, 'posts': []}
	if request.session.get('user_id', False):
		context['active_user'] = models.User.objects.get(user_id=request.session.get('user_id'))
	if username is not None:
		if username != context['active_user'].username:
			context['profile_user'] = models.User.objects.get(username=username)
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
	pass


def login(request):
	if request.session.get('user_id', False):
		return redirect(timeline)
	if request.method == 'POST':
		if request.POST.get('username') and request.POST.get('password'):
			if models.User.objects.filter(username=request.POST.get('username')).exists():
				user = models.User.objects.get(username=request.POST.get('username'))
				if user:
					if security.check_password_hash(user.pw_hash, request.POST.get('password')):
						request.session['user_id'] = user.pk
						messages.add_message(request, messages.INFO, 'You were logged in')
						return redirect(timeline)
			messages.add_message(request, messages.ERROR, 'Wrong password or username')
		else:
			messages.add_message(request, messages.ERROR, 'Both fields are required')
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
		elif models.User.objects.filter(username = request.POST.get('username')).exists():
			messages.add_message(request, messages.ERROR, 'The username is already taken')
		else:
			user = models.User(
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
