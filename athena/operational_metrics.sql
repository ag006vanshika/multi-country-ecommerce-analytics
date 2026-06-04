CREATE OR REPLACE VIEW operational_metrics AS
SELECT
    country,
    COUNT(*) AS valid_records,
    SUM(sales) AS total_sales
FROM orders_processed
GROUP BY country;