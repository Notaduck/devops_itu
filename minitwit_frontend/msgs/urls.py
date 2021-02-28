from django.urls import path
from msgs.views import AddMessageView

urlpatterns = [
	path('add_message/', AddMessageView.as_view(), name='add_message'),
]
