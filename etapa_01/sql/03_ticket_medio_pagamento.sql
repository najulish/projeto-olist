-- Qual o ticket médio por forma de pagamento?
-- Ticket médio considerando valor do produto + frete

SELECT  payment_type,
        ROUND(AVG(payment_value), 2) AS ticket_medio
FROM    order_payments
GROUP BY payment_type
ORDER BY ticket_medio DESC;
