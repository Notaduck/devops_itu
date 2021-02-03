from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import CustomUserCreationForm, CustomAuthenticationForm
from users.models import User

def login_context(request):
	return {'user': request.user if request.user.is_authenticated else False}


class RegisterView(FormView):
	form_class = CustomUserCreationForm
	template_name = 'register.html'
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class LoginView(LoginView):
	form_class = CustomAuthenticationForm
	template_name = 'login.html'
	redirect_authenticated_user = True
	success_url = '/timeline/'


class LogoutView(LogoutView):
	next_page = '/'
