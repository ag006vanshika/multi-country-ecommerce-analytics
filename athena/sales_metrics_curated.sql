CREATE TABLE mcea_analytics.sales_metrics_curated
WITH (
    format = 'PARQUET',
    external_location = 's3://mcea-data-lake-vanshika-2026/curated/sales_metrics/'
) AS

SELECT
    country,
    category,
    COUNT(order_id) AS orders,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM mcea_analytics.orders_processed
GROUP BY country, category;