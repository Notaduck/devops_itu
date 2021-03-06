from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email')


class CustomAuthenticationForm(AuthenticationForm):
	error_messages = {
		'invalid_login': 'The Username or password is invalid'
	}

	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'password')

	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		self.user_cache = None
		super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

		self.username_field = User._meta.get_field(User.USERNAME_FIELD)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			self.user_cache = authenticate(username=username, password=password)
			if self.user_cache is None:
				raise forms.ValidationError(
					self.error_messages['invalid_login'],
					code='invalid_login'
				)
		return self.cleaned_data

	def get_user_id(self):
		if self.user_cache:
			return self.user_cache.id # will return the declared identifier
		return None

	def get_user(self):
		return self.user_cache
