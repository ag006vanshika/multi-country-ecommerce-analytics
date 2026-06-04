CREATE TABLE mcea_analytics.customer_metrics_curated
WITH (
    format = 'PARQUET',
    external_location = 's3://mcea-data-lake-vanshika-2026/curated/customer_metrics/'
) AS

SELECT
    customer_id,
    country,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM mcea_analytics.orders_processed
GROUP BY customer_id, country;