from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
	def create_user(self, username, email, password):
		if not username:
			raise ValueError('The Username is Required')
		if not email:
			raise ValueError('The Email is Required')
		email = self.normalize_email(email)
		user = self.model(username=username, email=email)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, *args, **kwargs):
		raise NotImplementedError
