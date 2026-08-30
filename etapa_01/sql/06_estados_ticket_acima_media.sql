-- Quais estados têm ticket médio acima da média geral?

SELECT  t2.customer_state,
        ROUND(AVG(t3.price + t3.freight_value), 2) AS ticket_medio
FROM    orders AS t1
LEFT JOIN customers AS t2
ON t1.customer_id = t2.customer_id
LEFT JOIN order_items AS t3
ON t1.order_id = t3.order_id
GROUP BY customer_state
HAVING ticket_medio > (SELECT ROUND(AVG(price + freight_value), 2) FROM    order_items)
ORDER BY ticket_medio DESC;