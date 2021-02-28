from django.db import models
from users.models import User

class Message(models.Model):
	message_id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=280)
	pub_date = models.DateTimeField(auto_now_add=True)
	flagged = models.BooleanField(default=False)
