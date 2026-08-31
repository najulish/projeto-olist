WITH tb_top10 AS (
SELECT  t3.customer_unique_id,
        ROUND(SUM(t2.price + t2.freight_value), 2) AS total_gasto
FROM    orders AS t1
LEFT JOIN order_items AS t2
ON t1.order_id = t2.order_id
LEFT JOIN customers AS t3
ON t1.customer_id = t3.customer_id
GROUP BY t3.customer_unique_id
ORDER BY total_gasto DESC
LIMIT 10),

tb_customers_rn AS (
SELECT  customer_unique_id,
        customer_id,
        customer_zip_code_prefix,
        customer_city,
        customer_state,
        ROW_NUMBER() OVER (
            PARTITION BY customer_unique_id
            ORDER BY customer_id ASC
        ) AS rn
FROM    customers),

tb_customers_final AS (
SELECT  customer_unique_id, 
        customer_zip_code_prefix, 
        customer_city, 
        customer_state
FROM tb_customers_rn
WHERE rn = 1)

SELECT  t1.customer_unique_id,
        t1.total_gasto,
        t2.customer_zip_code_prefix,
        t2.customer_city,
        t2.customer_state
FROM    tb_top10 AS t1
LEFT JOIN tb_customers_final AS t2
ON t1.customer_unique_id = t2.customer_unique_id
ORDER BY t1.total_gasto DESC;