from latest.models import Latest

class LatestMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        param = request.GET.get('latest', None)

        if param:
            if Latest.objects.all().count() > 0:
                latest = Latest.objects.all().first()

                latest.latest = param
                latest.save(force_update=True)

            else:
                latest = Latest(id=1, latest=param).save(force_insert=True)
            
        

