from django.db import models
from auth.models import User

# Create your models here.
class Message(models.Model):
	message_id = models.AutoField(primary_key=True)
	author_id = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=280)
	pub_date = models.DateTimeField(auto_now_add=True)
	flagged = models.IntegerField(null=True)