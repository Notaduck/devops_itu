import json
from django.db import models
from users.models import User
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.
class Message(models.Model, ExportModelOperationsMixin("message")):
	message_id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=280)
	pub_date = models.DateTimeField(auto_now_add=True)
	flagged = models.BooleanField(default=False)