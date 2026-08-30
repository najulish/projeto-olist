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

## Próximas etapas
Para as próximas etapas pretendo apresentar um dashboard em Power BI visando responder perguntas mais complexas de negócios baseadas nos dados disponíveis. Pretendo também integrar Python nas análises, a fim de demonstrar minhas habilidades com a ferramenta. Como etapa final, a intenção é integrar a ferramenta QGIS ao projeto, gerando mapas e análises espaciais com insights de negócio.

## Dataset
Fonte: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Os arquivos CSV brutos estão em `data/raw/` (não incluí o banco `.db` pronto no repositório por limite de tamanho do GitHub — veja "Como reproduzir" abaixo).

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
- **Produtos sem categoria**: os 610 produtos sem categoria informada foram marcados como "nao_informado" em vez de excluídos (script de tratamento em `etapa_01/tratamento/`).
- **Geolocalização**: a tabela original tinha múltiplas coordenadas por CEP; foi criada `geolocation_tratada` com a coordenada média por CEP, para uso nas análises espaciais futuras (script de tratamento em `etapa_01/tratamento/`).
- **Formato de datas**: as colunas de data estão como TEXT no formato ISO (YYYY-MM-DD HH:MM:SS), compatível nativamente com as funções de data do SQLite (julianday, date, strftime).

## Ferramentas utilizadas
SQL e Excel.

## Perguntas de negócio respondidas
1. Qual o faturamento total por estado do cliente?
2. Quais as 10 categorias de produto mais vendidas?
3. Qual o ticket médio por forma de pagamento?
4. Quais categorias têm nota média de avaliação abaixo de 3.5? (**Nota: o critério original (nota < 3) não retornou nenhuma categoria com volume relevante de avaliações — o corte foi ajustado para < 3.5 para gerar um resultado com significância estatística.**)
5. Qual o ticket médio geral?
6. Quais estados têm ticket médio acima da média geral?
7. Qual a relação entre valor do frete e nota da avaliação?

## Principais insights
- São Paulo concentra 37,4% do faturamento total (R$ 5,9 milhões de R$ 15,8 milhões), evidenciando forte concentração de vendas no Sudeste
- Cama, mesa e banho é a categoria mais vendida em quantidade (11.115 itens), à frente de saúde/beleza e esporte/lazer
- Cartão de crédito é a forma de pagamento dominante (76.795 transações) e também tem o maior ticket médio (R$ 163,32), acima de boleto e débito
- Apenas duas categorias com volume relevante de avaliações ficam abaixo de 3,5: produtos de higiene/fraldas (nota 3,26) e móveis de escritório (nota 3,49) — a grande maioria das categorias mantém boa avaliação
- O ticket médio geral é de R$ 140,64; curiosamente, estados do Norte e Nordeste (como PB, AL e AC) apresentam ticket médio mais alto que São Paulo, provavelmente pelo maior custo de frete devido à distância dos centros de distribuição
- O valor do frete tem impacto pequeno na nota da avaliação (correlação de apenas -0,036), sugerindo que a insatisfação do cliente está ligada a outros fatores além do custo de entrega

## Como reproduzir
1. Clone este repositório
2. Os CSVs brutos já estão disponíveis em `data/raw/`
3. Importe os arquivos para um banco SQLite:
   - Abra o DB Browser for SQLite
   - Crie um novo banco de dados
   - Para cada CSV em `data/raw/`, use `File > Import > Table from CSV`, mantendo o nome do arquivo (sem extensão) como nome da tabela
4. Aplique os scripts de tratamento, na ordem, em `etapa_01/tratamento/`:
   - `01_geolocation_tratada.sql`
   - `02_products_categoria_nula.sql`
5. As queries de cada pergunta de negócio estão em `etapa_01/queries/`
6. Os resultados exportados estão em `etapa_01/resultados/`