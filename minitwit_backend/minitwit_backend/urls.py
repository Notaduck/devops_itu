"""minitwit_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from msgs.views import messages
from msgs.views import messages_per_user

router = routers.DefaultRouter()
# router.register('hej', auth.views.loginViewset)
# router.register('hej', get_all_messages)

urlpatterns = [
    # path('', include(router.urls))
	path('msgs/', messages),
	path('msgs/<str:username>/', messages_per_user)
]
