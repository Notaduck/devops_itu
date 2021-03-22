from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from msgs.models import Message
from msgs.forms import MessageCreationForm
from minitwit_frontend.metrics import Metrics

class AddMessageView(CreateView):
	http_method_names = ['post']
	form_class = MessageCreationForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		Metrics.inserts_total.labels("message").inc()
		return redirect('/')
