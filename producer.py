import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

event = {
    "event_type": "created",
    "task_id": 1,
    "task_data": {
        "id": 1,
        "title": "Buy groceries",
        "completed": False
    },
    "user_id": "demo-user",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

producer.send("task-events", event)
producer.flush()

print("EVENT SENT:", event)
