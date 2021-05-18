from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from users.models import User
from msgs.models import Message
from social.models import Follower

class TimelineView(TemplateView):
	template_name = 'timeline.html'

	def get_context_data(self, **kwargs):
		kwargs.setdefault('view', self)
		kwargs.update({'profile_user': None, 'public': False, 'posts': [], 'followed': False})
		kwargs['user'] = self.request.user if self.request.user.is_authenticated else False
		return kwargs

class PublicTimelineView(TimelineView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['public'] = True
		context['posts'] = Message.objects.select_related('author').all().order_by('-pub_date')
		return context


class CustomTimelineView(TimelineView):
	def get_context_data(self, username=False, **kwargs):
		context = super().get_context_data(**kwargs)
		if username:
			context['profile_user'] = User.objects.get(username=username)
			context['posts'] = Message.objects.select_related('author').filter(author=context['profile_user']).order_by('-pub_date')
			if context['user']:
				context['followed'] = Follower.objects.filter(who=context['user'], whom=context['profile_user']).exists()
		elif context['user']:
			users = [follower.whom for follower in Follower.objects.filter(who=context['user'])]
			users.append(context['user'])
			context['posts'] = Message.objects.select_related('author').filter(author_id__in=users).order_by('-pub_date')
		else:
			redirect('public_timeline')
		return context
