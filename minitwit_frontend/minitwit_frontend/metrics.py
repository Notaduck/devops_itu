from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    http_responses_total = Counter('frontend_http_responses_total', 'The total number of HTTP responses sent to the frontend.')
    cpu_load_percent = Gauge("frontend_cpu_load_percent", "The current load of the CPU as a percent.")

    insert_requests_total = Counter("frontend_insert_requests_total", "The total number of insert requests sent to the frontend", ["model"])
    update_requests_total = Counter("frontend_update_requests_total", "The total number of update requests sent to the frontend", ["model"])
    delete_requests_total = Counter("frontend_delete_requests_total", "The total number of delete requests sent to the frontend", ["model"])

    inserts_total = Counter("frontend_inserts_total", "The total number of inserts that the frontend performed", ["model"])
    updates_total = Counter("frontend_updates_total", "The total number of updates that the frontend performed", ["model"])
    deletes_total = Counter("frontend_deletes_total", "The total number of deletes that the frontend performed", ["model"])

    # initialize the labels
    labels = ["user", "follower", "message"]
    for label in labels:
        insert_requests_total.labels(label)
        update_requests_total.labels(label)
        delete_requests_total.labels(label)
        inserts_total.labels(label)
        updates_total.labels(label)
        deletes_total.labels(label)