-- Quais categorias têm nota média de avaliação abaixo de 3.5

SELECT  t2.product_category_name,
        ROUND(AVG(t3.review_score), 2) AS media_avaliacao,
        COUNT(*) AS numero_avaliacoes
FROM    order_items AS t1
LEFT JOIN products AS t2
ON t1.product_id = t2.product_id
LEFT JOIN order_reviews AS t3
ON t1.order_id = t3.order_id
GROUP BY product_category_name
HAVING media_avaliacao < 3.5 AND numero_avaliacoes > 20
ORDER BY media_avaliacao;