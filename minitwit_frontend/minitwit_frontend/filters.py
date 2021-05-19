from django.utils.safestring import mark_safe
from django import template

from hashlib import md5
from datetime import datetime

register = template.Library()

@register.filter
def gravatar(var, size=48):
	return mark_safe('<img src="{}" height="{}" width="{}">'.format(gravatar_url(str(var), size=size), size, size))

def gravatar_url(var, size=48):
	return 'http://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(md5(var.strip().lower().encode('utf-8')).hexdigest(), size)
