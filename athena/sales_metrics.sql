CREATE OR REPLACE VIEW sales_metrics AS
SELECT
    country,
    category,
    SUM(sales) AS revenue,
    SUM(profit) AS profit,
    COUNT(order_id) AS orders
FROM orders_processed
GROUP BY country, category;