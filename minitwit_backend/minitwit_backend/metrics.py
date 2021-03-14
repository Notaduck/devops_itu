from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    http_responses_total = Counter('backend_http_responses_total', 'The total number of HTTP responses sent to the backend.')
    cpu_load_percent = Gauge("backend_cpu_load_percent", "The current load of the CPU as a percent.")