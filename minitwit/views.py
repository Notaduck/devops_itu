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
    # Insert
    return render(request, "timeline.html")


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
    # Insert
    return render(request, "login.html")


def register(request):
    # Insert
    return render(request, "register.html")


def logout(request):
    pass
