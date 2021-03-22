import psutil
from minitwit_backend.metrics import Metrics
from latest.models import Latest

class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # increment number of http responses after any view is called
        Metrics.http_responses_total.inc()

        # record cpu load after any view is called
        Metrics.cpu_load_percent.set(psutil.cpu_percent())

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'POST':
            # increment delete requests if /unfollow was posted to
            if request.path.startswith("/unfollow"):
                Metrics.delete_requests_total.labels("follow").inc()
                return
            
            # determine the label of the model that was posted to
            if request.path.startswith("/msgs"):
                label = "message"
            elif request.path.startswith("/register"):
                label = "user"
            elif request.path.startswith("/follow"):
                label = "follow"
            else: # if a post method was not sent to one of the above URLs, then do nothing
                return
            
            # increment insert requests if a post request was sent to a correct label 
            Metrics.insert_requests_total.labels(label).inc()


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
            
        

