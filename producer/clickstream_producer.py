import boto3
import json
import random
from datetime import datetime
import time

STREAM_NAME = "mcea-clickstream-stream"
REGION = "ap-south-1"  # stream region

kinesis = boto3.client(
    "kinesis",
    region_name=REGION
)

countries = ["India", "UK", "Canada"]

event_types = [
    "page_view",
    "product_view",
    "add_to_cart",
    "checkout",
    "purchase"
]

products = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Keyboard",
    "Monitor"
]


def generate_event():

    return {
        "user_id": f"U{random.randint(1000,9999)}",
        "country": random.choice(countries),
        "event_type": random.choice(event_types),
        "product": random.choice(products),
        "timestamp": datetime.utcnow().isoformat()
    }


def send_event(event):

    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(event),
        PartitionKey=event["country"]
    )


if __name__ == "__main__":

    print("Sending clickstream events...\n")

    for _ in range(50):

        event = generate_event()

        send_event(event)

        print(event)

        time.sleep(0.2)

    print("\nDone.")
