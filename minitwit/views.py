from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from werkzeug import security # used only for user compatability between old system and new system

from . import models

def index(request):
	return HttpResponse(request.session.get('user_id', False))


def beforeRequest(request):
	pass


def afterRequest(response):
	pass


def TimeLine(request):
	return render(request, "layout.html", )


def publicTimeLine(request):
	pass

def userTimeLine(request):
	pass


def followUser(request):
	pass


def unfollowUser(request):
	pass


def addMessage(request):
	pass


def login(request):
	if request.method == 'POST':
		if request.session.get('user_id', False):
			return redirect(index)
		user = models.User.objects.get(username=request.POST.get('username'))
		if user:
			if security.check_password_hash(user.pw_hash, request.POST.get('password')):
				request.session['user_id'] = user.pk
				messages.add_message(request, messages.INFO, 'You were logged in')
				return redirect(index)
		messages.add_message(request, messages.ERROR, 'Wrong password or username')
	return render(request, 'login.html')


def register(request):
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
	pass
