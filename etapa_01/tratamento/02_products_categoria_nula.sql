-- Marca produtos sem categoria como 'nao_informado' em vez de NULL
UPDATE products
SET product_category_name = 'nao_informado'
WHERE product_category_name IS NULL;