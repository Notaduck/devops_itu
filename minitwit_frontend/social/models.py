from django.db import models
from users.models import User

class Follower(models.Model):
	who =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_who')
	whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_whom')
