from django.db import models
from users.models import User
from django_prometheus.models import ExportModelOperationsMixin


class Follower(models.Model, ExportModelOperationsMixin('follower')):
	who =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_who')
	whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_whom')
