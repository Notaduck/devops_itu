from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from werkzeug import security # used only for user compatability between old system and new system

from . import models

def index(request):
	return HttpResponse(request.session.get('user_id', False))


def timeline(request, username = None):
	context = {'active_user' : None, 'profile_user': None, 'public': False, 'posts': [], 'followed': False}
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
		context['followed'] = models.Follower.objects.filter(who=context['active_user'], whom=context['profile_user'].user_id).exists()
	else:
		context['posts'] = []
	return render(request, 'timeline.html', context = context)


def follow_user(request, username = False):
	if not request.session.get('user_id', False) or not models.User.objects.filter(username=username).exists():
		if not models.User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, 'The target user does not exist')
		if not request.session.get('user_id', False):
			messages.add_message(request, messages.ERROR, 'You must be logged in to follow a user')
		return redirect(timeline, username=username)

	followedUser = models.User.objects.get(username=username)
	followingUser = models.User.objects.get(user_id=request.session.get('user_id'))

	if followedUser.user_id == request.session.get('user_id'):
		messages.add_message(request, messages.ERROR, 'You cannot follow yourself')
		return redirect(timeline, username=username)

	follower = models.Follower(
		who = followingUser,
		whom = followedUser
	)

	follower.save()
	
	messages.add_message(request, messages.INFO, 'You followed ' + followedUser.username)
	
	return redirect(timeline, username=username)
	

def unfollow_user(request, username = False):
	if not request.session.get('user_id', False) or not models.User.objects.filter(username=username).exists():
		if not models.User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, 'The target user does not exist')
		if not request.session.get('user_id', False):
			messages.add_message(request, messages.ERROR, 'You must be logged in to unfollow a user')
		return redirect(timeline, username=username)

	followedUser = models.User.objects.get(username=username)
	
	if followedUser.user_id == request.session.get('user_id'):
		messages.add_message(request, messages.ERROR, 'You cannot unfollow yourself')
		return redirect(timeline, username=username)

	if not models.Follower.objects.filter(who=request.session.get('user_id'), whom=followedUser.user_id).exists():
		follower = models.Follower.objects.get(who=request.session.get('user_id'), whom=followedUser.user_id)
		follower.delete()
		messages.add_message(request, messages.INFO, 'You unfollowed ' + followedUser.username)
	else: 
		messages.add_message(request, messages.ERROR, 'You cannot unfollow someone whom you are not following')
		
	return redirect(timeline, username=username)


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
