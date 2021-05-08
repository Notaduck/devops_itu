from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    http_responses_total = Counter('backend_http_responses_total', 'The total number of HTTP responses sent to the backend.')
    cpu_load_percent = Gauge("backend_cpu_load_percent", "The current load of the CPU as a percent.")

    insert_requests_total = Counter("backend_insert_requests_total", "The total number of insert requests sent to the backend", ["model"])
    update_requests_total = Counter("backend_update_requests_total", "The total number of update requests sent to the backend", ["model"])
    delete_requests_total = Counter("backend_delete_requests_total", "The total number of delete requests sent to the backend", ["model"])

    inserts_total = Counter("backend_inserts_total", "The total number of inserts that the backend performed", ["model"])
    updates_total = Counter("backend_updates_total", "The total number of updates that the backend performed", ["model"])
    deletes_total = Counter("backend_deletes_total", "The total number of deletes that the backend performed", ["model"])

    # initialize the labels
    labels = ["user", "follower", "message"]
    for label in labels:
        insert_requests_total.labels(label)
        update_requests_total.labels(label)
        delete_requests_total.labels(label)
        inserts_total.labels(label)
        updates_total.labels(label)
        deletes_total.labels(label)