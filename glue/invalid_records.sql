SELECT *
FROM myDataSource
WHERE customer_id IS NULL
   OR country IS NULL
   OR sales <= 0
   OR quantity <= 0