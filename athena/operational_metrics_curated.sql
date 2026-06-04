CREATE TABLE mcea_analytics.operational_metrics_curated
WITH (
    format = 'PARQUET',
    external_location = 's3://mcea-data-lake-vanshika-2026/curated/operational_metrics/'
) AS

SELECT
    country,
    ROUND(SUM(sales), 2) AS total_sales,
    COUNT(*) AS valid_records
FROM mcea_analytics.orders_processed
GROUP BY country;