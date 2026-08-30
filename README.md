# Análise de Dados — E-commerce Olist

## Sobre o projeto
Este projeto é o primeiro de uma série de análises de dados que venho desenvolvendo como parte da minha transição de carreira para a área de Analytics, com foco em geointeligência. 

Utilizando o dataset público de e-commerce da Olist, o objetivo é responder perguntas de negócio reais sobre vendas, comportamento de clientes e distribuição geográfica no mercado brasileiro, aplicando e evoluindo conhecimentos em SQL, Excel, Power BI, Python e, futuramente, análise espacial com QGIS.

Mais do que um exercício técnico, este projeto documenta minha trajetória de aprendizado: cada etapa reflete uma nova ferramenta ou conceito incorporado ao meu processo de análise, do básico ao avançado.

## Status do projeto
- [x] Etapa 1 — SQL + Excel
- [ ] Etapa 2 — SQL avançado + Power BI
- [ ] Etapa 3 — Python
- [ ] Etapa 4 — Integração
- [ ] Etapa 5 — QGIS

## Próximas etapas:
Para as próximas etapas pretendo apresentar um dashboard em Power BI visando responder perguntas mais complexas de negócios baseadas nos dados disponíveis. Pretendo também integrar Python nas análises, a fim de demonstrar minhas habilidades com a ferramenta. Como etapa final, a intenção é integrar a ferramenta QGIS ao projeto, gerando mapas e análises espaciais com insights de negócio.

## Dataset
Fonte: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
Tabelas principais: 
- `customers`
- `products` 
- `sellers`
- `geolocation`
- `orders`
- `order_items`
- `order_payments` 
- `order_reviews`
- `product_category_name_translation` 

## Definições e premissas
- **Ticket médio**: considera o valor do produto (`price`) + valor do frete (`freight_value`), representando o gasto total do cliente por item.
- **Status dos pedidos**: as análises de faturamento e ticket médio (perguntas 1, 3, 5, 6) consideram todos os pedidos, independentemente do status. Análises futuras sobre cancelamentos ou entregas terão seus próprios critérios, documentados junto à respectiva pergunta.
- **Produtos sem categoria**: os 610 produtos sem categoria informada foram marcados como "nao_informado" em vez de excluídos.
- **Geolocalização**: a tabela original tinha múltiplas coordenadas por CEP; foi criada `geolocation_tratada` com a coordenada média por CEP, para uso nas análises espaciais futuras.
- **Formato de datas**: as colunas de data estão como TEXT no formato ISO (YYYY-MM-DD HH:MM:SS), compatível nativamente com as funções de data do SQLite (julianday, date, strftime)

## Ferramentas utilizadas
SQL e Excel.

## Perguntas de negócio respondidas
1. Qual o faturamento total por estado do cliente?
2. Quais as 10 categorias de produto mais vendidas?
3. Qual o ticket médio por forma de pagamento?
4. Quais categorias têm nota média de avaliação abaixo de 3.5? (**Nota: o critério original (nota < 3) não retornou nenhuma categoria com volume relevante de avaliações — o corte foi ajustado para < 3.5 para gerar um resultado com significância estatística.**)
5. Qual o ticket médio?
6. Quais estados têm ticket médio acima da média geral?
7. Qual a relação entre valor do frete e nota da avaliação?

## Como reproduzir
1. Clone este repositório
2. Certifique-se de ter os CSVs em `data/raw/` (já incluídos no repositório)
3. Instale as dependências:
```bash
   pip install pandas
```
4. Rode o script de importação:
```bash
   python scripts/import_data.py
```
5. Isso vai gerar o arquivo `olist_raw.db` na pasta `data/`
6. Abra no DB Browser for SQLite ou use a extensão SQLite no VSCode
7. As queries estão organizadas em `etapa_01/sql/`, uma por pergunta de negócio
8. Os resultados exportados estão em `etapa_01/csv/`.
