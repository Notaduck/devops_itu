import psutil
from minitwit_backend.metrics import Metrics
from latest.models import Latest
import logging
from django.contrib.auth.models import AnonymousUser
request_logger = logging.getLogger('django.request')

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
            # determine the label of the model that was posted to
            if request.path.startswith("/fllws"):
                # if request was given to /fllws, determine whether its follow or unfollow
                if b'unfollow' in request.body:
                    Metrics.delete_requests_total.labels("follower").inc()
                elif b'follow' in request.body:
                    Metrics.insert_requests_total.labels("follower").inc()
            elif request.path.startswith("/msgs"):
                Metrics.insert_requests_total.labels("message").inc()
            elif request.path.startswith("/register"):
                Metrics.insert_requests_total.labels("user").inc()
            # if a post method was not sent to one of the above URLs, then do nothing
            


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


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.log(*self.extract(response, request))
        return response

    def extract(self, response, request):
        content = request.POST if request.method == 'POST' else request.GET
        try:
            user = request.user
        except:
            user = AnonymousUser
        return response.status_code, response.reason_phrase, request.method, content, request.META.get('REMOTE_ADDR'), user, request.path

    def log(self, status_code, reason_phrase, method, content, remote_addr, user, path):
        if status_code >=400:
            log_level = request_logger.warning
        else:
            log_level = request_logger.info

        log_level('\t'.join([str(status_code), reason_phrase, method, path, remote_addr, str(user.username), str(dict(content))]))

        

