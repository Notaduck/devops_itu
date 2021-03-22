from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView
from social.models import Follower
from users.models import User
from minitwit_frontend.metrics import Metrics

class FollowView(CreateView):
	http_method_names = ['get']
	model = Follower

	def get(self, request, username=None):
		if username is None or username==self.request.user.username: redirect('/timeline')
		follower = Follower(who=request.user, whom=User.objects.get(username=username))
		follower.save()
		Metrics.inserts_total.labels("follower").inc()
		return redirect('/timeline/{}'.format(username))


class UnFollowView(DeleteView):
	http_method_names = ['get']
	model = Follower

	def get(self, request, username=None):
		if username is None or username==self.request.user.username: redirect('/timeline')
		Follower.objects.get(who=request.user, whom=User.objects.get(username=username)).delete()
		Metrics.deletes_total.labels("follower").inc()
		return redirect('/timeline/{}'.format(username))
