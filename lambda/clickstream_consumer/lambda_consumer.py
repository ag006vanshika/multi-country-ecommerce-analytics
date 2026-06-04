import json
import boto3
from datetime import datetime, UTC

s3 = boto3.client("s3")

BUCKET_NAME = "mcea-data-lake-vanshika-2026"


def lambda_handler(event, context):

    records = []

    for record in event["Records"]:

        payload = record["kinesis"]["data"]

        import base64

        decoded_data = base64.b64decode(payload)

        records.append(
            json.loads(decoded_data)
        )

    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

    file_key = (
        f"raw/clickstream/"
        f"clickstream_{timestamp}.json"
    )

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_key,
        Body=json.dumps(records, indent=2)
    )

    return {
        "statusCode": 200,
        "records_processed": len(records)
    }