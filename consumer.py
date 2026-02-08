import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "task-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="todo-demo-consumer",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print("Listening on topic: task-events")

for msg in consumer:
    print("EVENT RECEIVED:", msg.value)
