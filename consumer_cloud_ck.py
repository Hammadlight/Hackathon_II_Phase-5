import json
from confluent_kafka import Consumer

BOOTSTRAP = "d61itik7ecku8d3si5h0.any.ap-south-1.mpx.prd.cloud.redpanda.com:9092"
USERNAME = "demo-user3"
PASSWORD = "MtAzy814nQUyE8jxlDiZ3wa2igRj8G"

conf = {
    "bootstrap.servers": BOOTSTRAP,
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "SCRAM-SHA-256",
    "sasl.username": USERNAME,
    "sasl.password": PASSWORD,
    "group.id": "demo-cloud-group",
    "auto.offset.reset": "earliest",
}

c = Consumer(conf)
c.subscribe(["task-events"])

print("✅ Listening on CLOUD topic: task-events (confluent-kafka) ...")

try:
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Consumer error:", msg.error())
            continue
        data = json.loads(msg.value().decode("utf-8"))
        print("📩 CLOUD EVENT:", data)
except KeyboardInterrupt:
    pass
finally:
    c.close()
