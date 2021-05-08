from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email or not username:
            raise ValueError('The Email and Username is Required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, *args, **kwargs):
        raise NotImplementedError

    def get_by_natural_key(self, username):
        return self.get(username=username)
