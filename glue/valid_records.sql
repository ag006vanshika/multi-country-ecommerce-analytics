-- Valid Records Query

SELECT
    order_id,
    order_date,
    ship_date,
    customer_id,
    geography,
    category,
    product_name,
    sales,
    quantity,
    profit,
    country,
    state,
    county,
    province,
    COALESCE(state, county, province) AS region
FROM myDataSource
WHERE customer_id IS NOT NULL
  AND country IS NOT NULL
  AND sales > 0
  AND quantity > 0