# Purpose:
Produces clickstream events into kinesis and Consumes clickstream events from Kinesis and stores them in the S3 raw zone.

## Flow:
Lambda Producer
    ↓
Kinesis Stream
    ↓
Lambda Consumer
    ↓
raw/clickstream/