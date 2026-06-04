# Athena Analytics Layer

These CTAS (Create Table As Select) queries generate the curated analytics layer from the processed orders dataset.

## Curated Tables

### sales_metrics_curated
Country and category level sales analytics.

### customer_metrics_curated
Customer-level revenue, profit, and order metrics.

### operational_metrics_curated
Country-level operational metrics and valid record counts.

All curated tables are stored as Parquet files in Amazon S3 and are consumed by Amazon QuickSight dashboards.