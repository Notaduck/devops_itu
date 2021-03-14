from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from users.managers import UserManager
from django_prometheus.models import ExportModelOperationsMixin

class User(AbstractBaseUser, PermissionsMixin, ExportModelOperationsMixin("user")):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(unique=True)

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['email']
	# pasword field is inherited with a hashing function defined in the settings file

	objects = UserManager()

	def __str__(self): # makes it easy to display the username
		return self.username
