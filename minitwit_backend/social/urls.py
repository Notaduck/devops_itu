from django.urls import path
from social.views import FollowView


urlpatterns = [
	path('fllws/<str:username>', FollowView.as_view(), name='follow')
]
