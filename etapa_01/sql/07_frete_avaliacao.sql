-- Qual a relação entre valor do frete e nota da avaliação?

SELECT
  CASE
    WHEN t1.freight_value < 15 THEN '1 - Frete baixo (<15)'
    WHEN t1.freight_value < 30 THEN '2 - Frete médio (15-30)'
    WHEN t1.freight_value < 50 THEN '3 - Frete alto (30-50)'
    ELSE '4 - Frete muito alto (>50)'
  END AS faixa_frete,
  ROUND(AVG(t2.review_score), 2) AS nota_media,
  COUNT(*) AS numero_avaliacoes
FROM order_items AS t1
LEFT JOIN order_reviews AS t2
ON t1.order_id = t2.order_id
GROUP BY faixa_frete
ORDER BY faixa_frete;