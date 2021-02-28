from django.urls import path
from social.views import FollowView, UnFollowView

urlpatterns = [
	path('follow/<str:username>/', FollowView.as_view(), name='follow'),
	path('unfollow/<str:username>/', UnFollowView.as_view(), name='unfollow')
]
