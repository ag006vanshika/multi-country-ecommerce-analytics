Purpose:
Consumes clickstream events from Kinesis and stores them in the S3 raw zone.

Flow:
Kinesis Stream
    ↓
Lambda Consumer
    ↓
raw/clickstream/