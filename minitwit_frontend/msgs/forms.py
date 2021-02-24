from django import forms
from msgs.models import Message


class MessageCreationForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('text',)
