from django.urls import path
from msgs.views import MessagesListCreateView

urlpatterns = [
    path('msgs', MessagesListCreateView.as_view(), name='all_messages'),
    path('msgs/<str:username>', MessagesListCreateView.as_view(), name='messages_per_user'),
    path('msgs/<str:username>', MessagesListCreateView.as_view(), name='add_message')
]