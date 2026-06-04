"""
Reference implementation of the AWS Glue Visual ETL job.

Actual project implementation uses:
AWS Glue Studio Visual ETL

Responsibilities:
1. Schema evolution
   state/county/province -> region

2. Data quality validation
   - customer_id not null
   - country not null
   - sales > 0
   - quantity > 0

3. Route valid records to processed zone

4. Route invalid records to error zone

5. Write Parquet output partitioned by country
"""
