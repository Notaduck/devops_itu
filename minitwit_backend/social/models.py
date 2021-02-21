from django.db import models
from users.models import User

class Follower(models.Model):
    follow_id = models.AutoField(primary_key=True)
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_whom')