from django.urls import path
from latest.views import latest


urlpatterns = [
	path('latest', latest, name='latest')
]
