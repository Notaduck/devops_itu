import psutil
import logging
from minitwit_frontend.metrics import Metrics
from django.contrib.auth.models import AnonymousUser
request_logger = logging.getLogger(__name__)

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
        return response.status_code, response.reason_phrase, request.method, content, user, request.path

    def log(self, status_code, reason_phrase, method, content, user, path):
        if status_code >=400:
            log_level = request_logger.warning
        else:
            log_level = request_logger.info

        log_level(' '.join([str(status_code), reason_phrase, method, path, str(user.username), str(dict(content))]))
