from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from latest.models import Latest

@api_view(['get'])
def latest(request):
	latest = Latest.objects.all().first()
	return Response({'latest': latest.latest})
