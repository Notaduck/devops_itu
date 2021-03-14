from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    http_responses_total = Counter('frontend_http_responses_total', 'The total number of HTTP responses sent to the frontend.')
    cpu_load_percent = Gauge("frontend_cpu_load_percent", "The current load of the CPU as a percent.")