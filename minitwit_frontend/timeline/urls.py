from django.urls import path
from timeline.views import PublicTimelineView, CustomTimelineView


urlpatterns = [
	path('', PublicTimelineView.as_view(), name='public_timeline'),
	path('timeline/', CustomTimelineView.as_view(), name='personal_timeline'),
	path('timeline/<str:username>', CustomTimelineView.as_view(), name='user_timeline'),
]
