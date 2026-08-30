-- Quais as 10 categorias de produto mais vendidas?

SELECT  t3.product_category_name,
        COUNT(*) AS qtd_vendida
FROM    orders AS t1
LEFT JOIN order_items AS t2
ON t1.order_id = t2.order_id
LEFT JOIN products AS t3
ON t2.product_id = t3.product_id
GROUP BY t3.product_category_name
ORDER BY qtd_vendida DESC
LIMIT 10;
