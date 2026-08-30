-- Pergunta: Qual o faturamento total por estado do cliente?

SELECT  t2.customer_state AS estado,
        ROUND(SUM(t3.price + t3.freight_value), 2) AS faturamento
FROM    orders AS t1
LEFT JOIN customers AS t2
ON t1.customer_id = t2.customer_id
LEFT JOIN order_items AS t3
ON t1.order_id = t3.order_id
GROUP BY estado
ORDER BY faturamento DESC;