import ssl
import json
import time
from kafka import KafkaProducer

BOOTSTRAP = "d61itik7ecku8d3si5h0.any.ap-south-1.mpx.prd.cloud.redpanda.com:9092"
USERNAME = "demo-user"
PASSWORD = "DWcGJySAz7HW4mEyLaqKZvIU7boB"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    ssl_context=ssl.create_default_context(),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

event = {
    "event_type": "created",
    "task_id": 101,
    "task_data": {"id": 101, "title": "Cloud Kafka test", "completed": False},
    "user_id": "demo-user",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

producer.send("task-events", event)
producer.flush()

print("✅ SENT TO CLOUD:", event)
