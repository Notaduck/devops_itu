from django.conf import settings

class LatestFilterBackend:
	def filter_queryset(self, request, queryset, view): # only reliable function to overwrite
		param = request.query_params.get('latest', '')
		param.replace('\x00', '')
		param.replace(',', ' ')
		try:
			param = int(param)
			settings.LATEST = param
		except:
			pass
			"""invalid latest parameter"""

		return queryset
