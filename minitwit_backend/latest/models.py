from django.db import models

class Latest(models.Model):
	id = models.IntegerField(primary_key=True)
	latest = models.IntegerField()

	ID_FIELD = 'id'
	REQUIRED_FIELDS = ['latest']