SELECT  ROUND(AVG(price + freight_value), 2) AS ticket_medio
FROM    order_items;