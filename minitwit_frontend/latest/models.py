from django.db import models

class Latest(models.Model):
	id = models.IntegerField(primary_key=True)

	ID_FIELD = 'id'
	REQUIRED_FIELDS = ['id']