# AWS Glue ETL Layer

This project uses AWS Glue Studio Visual ETL to process raw order data.

## Transformations

### Valid Records

Records are considered valid when:

- customer_id IS NOT NULL
- country IS NOT NULL
- sales > 0
- quantity > 0

Valid records are written to:

s3://mcea-data-lake-vanshika-2026/processed/orders/

### Invalid Records

Records failing validation are routed to:

s3://mcea-data-lake-vanshika-2026/error/orders/

## Additional Transformations

Region standardization:

COALESCE(state, county, province) AS region

## Output Format

Parquet

Partitioned by:

country