from django.urls import path
from users.views import RegisterView, GetCurrentUser


urlpatterns = [
	path('register/', RegisterView.as_view(), name='register'),
	path('getcurrentuser/', GetCurrentUser.as_view(), name='getcurrentuser')
]

