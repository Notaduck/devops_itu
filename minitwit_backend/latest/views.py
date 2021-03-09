from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

@api_view(['get'])
def latest(request):
	return Response({'latest':settings.LATEST}, content_type='application/json')
