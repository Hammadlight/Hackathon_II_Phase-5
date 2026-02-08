import json
import time
from confluent_kafka import Producer

BOOTSTRAP = "d61itik7ecku8d3si5h0.any.ap-south-1.mpx.prd.cloud.redpanda.com:9092"
USERNAME = "demo-user3"
PASSWORD = "MtAzy814nQUyE8jxlDiZ3wa2igRj8G"

conf = {
    "bootstrap.servers": BOOTSTRAP,
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "SCRAM-SHA-256",
    "sasl.username": USERNAME,
    "sasl.password": PASSWORD,
    "client.id": "todo-cloud-producer",
    "socket.timeout.ms": 20000,
    "message.timeout.ms": 20000,
}

p = Producer(conf)

event = {
    "event_type": "created",
    "task_id": 202,
    "task_data": {"id": 202, "title": "Cloud Kafka CK test", "completed": False},
    "user_id": USERNAME,
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

def delivery_report(err, msg):
    if err is not None:
        print("❌ Delivery failed:", err)
    else:
        print(f"✅ Delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

p.produce(
    "task-events",
    value=json.dumps(event).encode("utf-8"),
    callback=delivery_report
)

p.flush(20)
print("✅ SENT TO CLOUD (confluent-kafka):", event)
