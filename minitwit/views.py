from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
	# Testing
	return HttpResponse("Hello World!")


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
	return render(request, "login.html")


def register(request):
	error = None
	if request.method == 'POST':
		if not request.POST.get('username', ''):
			messages.add_message(request, messages.ERROR, 'You have to enter a username')
		elif not request.POST.get('email') or '@' not in request.POST.get('email'):
			messages.add_message(request, messages.ERROR, 'You have to enter a valid email address')
		elif not request.POST.get('password'):
			messages.add_message(request, messages.ERROR, 'You have to enter a password')
		elif request.POST.get('password') != request.POST.get('password2'):
			messages.add_message(request, messages.ERROR, 'The two passwords do not match')
		#elif get_user_id(request.form['username']) is not None:
		#	messages.add_message(request, messages.ERROR, 'The username is already taken')
		else:
			# insert new user
			pass
			return redirect('minitwit.views.login')
	return render(request, "register.html")

def logout(request):
	pass
