from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app = Flask(__name__)

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

@app.route("/")
def hello():
    start = time.time()
    graphs['c'].inc()
    
    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return "<html><body bgcolor=#33342f><center>Hello World!<br><img src=https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_600/https://shwanoff.ru/wp-content/uploads/2017/12/hello-world.jpg></center></body></html>"

@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

