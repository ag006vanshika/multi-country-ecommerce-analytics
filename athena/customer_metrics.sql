CREATE OR REPLACE VIEW customer_metrics AS
SELECT
    customer_id,
    country,
    COUNT(order_id) AS total_orders,
    SUM(sales) AS total_revenue,
    SUM(profit) AS total_profit
FROM orders_processed
GROUP BY customer_id, country;