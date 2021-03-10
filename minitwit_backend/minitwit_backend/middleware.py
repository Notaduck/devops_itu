from latest.models import Latest

class LatestMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        param = request.GET.get('latest', 1)


        if Latest.objects.all().count() > 0:
            latest = Latest.objects.all().first()

            if param:
                latest.latest = param
                latest.save(force_update=True)

        else:
            latest = Latest(latest=param).save(force_create=True)
            
        

