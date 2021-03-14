import psutil
from minitwit_frontend.metrics import Metrics

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