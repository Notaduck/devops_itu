from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	# Testing
	return HttpResponse("Hello World!")


def beforeRequest(request):
	pass


def afterRequest(response):
	pass


def timeline(request):
	return render(request, "layout.html")


def publicTimeline(request):
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
	return render(request, "register.html")


def logout(request):
	pass


def test(request):
	"""Test Purposes only"""
	context = {
		'posts': [
			{
				'author': 'CoreyMS',
				'title': 'Blog Post 1',
				'content': 'First post content',
				'date_posted': 'August 27, 2018'
			},
			{
				'author': 'Jane Doe',
				'title': 'Blog Post 2',
				'content': 'Second post content',
				'date_posted': 'August 28, 2018'
			}
		]
	}
	return render(request, "testTemplate.html", context)
