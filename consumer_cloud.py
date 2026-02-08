import ssl
import json
from kafka import KafkaConsumer

BOOTSTRAP = "d61itik7ecku8d3si5h0.any.ap-south-1.mpx.prd.cloud.redpanda.com:9092"
USERNAME = "demo-user"
PASSWORD = "DWcGJySAz7HW4mEyLaqKZvIU7boB"

consumer = KafkaConsumer(
    "task-events",
    bootstrap_servers=BOOTSTRAP,
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    ssl_context=ssl.create_default_context(),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="todo-demo-consumer-cloud",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print("✅ Listening on CLOUD topic: task-events ...")
for msg in consumer:
    print("📩 CLOUD EVENT:", msg.value)
