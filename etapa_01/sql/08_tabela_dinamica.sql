WITH tb_payments_rn AS (
SELECT  order_id,
        payment_type,
        payment_value,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY payment_value DESC, 
            payment_sequential ASC) AS rn
FROM    order_payments),

tb_pagamento_final AS (
SELECT order_id, payment_type, payment_value
FROM tb_payments_rn
WHERE rn = 1),

tb_reviews_rn AS (
SELECT  order_id,
        review_score,
        review_creation_date,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY review_creation_date DESC, 
            review_id ASC) AS rn
FROM    order_reviews),

tb_review_final AS (
SELECT order_id, review_score
FROM tb_reviews_rn
WHERE rn = 1)

SELECT  t1.order_id,
        t2.order_purchase_timestamp,
        t3.customer_state,
        t4.product_category_name,
        t5.payment_type,
        t6.review_score
FROM    order_items AS t1
LEFT JOIN orders AS t2 ON t1.order_id = t2.order_id
LEFT JOIN customers AS t3 ON t2.customer_id = t3.customer_id
LEFT JOIN products AS t4 ON t1.product_id = t4.product_id
LEFT JOIN tb_pagamento_final AS t5 ON t1.order_id = t5.order_id
LEFT JOIN tb_review_final AS t6 ON t1.order_id = t6.order_id;