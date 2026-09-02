# Relatório de Análise — Olist

## Resumo executivo
- **Período analisado:** agosto de 2017 a agosto de 2018 (12 meses)
- **Faturamento total:** R$ 12.844.138,02
- **Total de pedidos:** 91.451
- **Ticket médio geral (preço + frete):** R$ 140,45
- **Frete médio sobre o faturamento:** 14,34%
- **Estados atendidos:** 27 (todos os estados brasileiros)
- **Concentração:** São Paulo representa 37,80% do faturamento total

## 1. Introdução
As análises buscaram compreender, a partir dos dados disponíveis, informações a respeito do desempenho comercial, comportamento dos consumidores e experiência de compra na plataforma Olist.

Dada a natureza dos dados, optou-se por um recorte temporal entre agosto de 2017 e agosto de 2018 — período de 12 meses em que os dados estão mais consistentes, evitando o baixo volume do início da operação (2016) e o registro incompleto do último mês disponível na base (setembro de 2018, com apenas uma venda registrada).

A partir de consultas iniciais em SQL, foi gerada uma planilha para possibilitar um trabalho mais visual com as informações através de tabelas dinâmicas e gráficos, que contribuíram para os insights explorados neste relatório.

**Nota metodológica sobre sazonalidade:** embora o recorte de 12 meses permita observar variações de volume de pedidos ao longo do ano, parte dessas variações — especialmente a queda nos meses finais do período — provavelmente reflete a forma como os dados foram extraídos (pedidos muito recentes tendem a estar sub-representados no momento do corte da base) e não necessariamente uma queda real de demanda. A exceção é o pico de novembro de 2017, coerente com o período de Black Friday, que é consistente com um efeito real de mercado.

## 2. Desempenho e concentração das vendas
O estado que se destaca em concentração de vendas, tanto em número de pedidos quanto em faturamento, é São Paulo. Esse resultado é esperado dada a concentração populacional e a relevância econômica do estado no contexto brasileiro.

Ao observar o estado líder por região, temos: Rio Grande do Sul na região Sul, Bahia no Nordeste, Goiás no Centro-Oeste e Pará no Norte.

De forma geral, a região Sudeste é a que mais contribui para o número de pedidos e faturamento, com São Paulo, Rio de Janeiro e Minas Gerais formando o Top 3 em ambas as análises.

## 3. O comportamento das categorias
As categorias que mais venderam no período analisado foram (1) Beleza e Saúde, (2) Cama, Mesa e Banho e (3) Esporte e Lazer, com nota média de avaliação de, respectivamente, 4,2, 3,9 e 4,1.

Já as categorias com melhores notas (considerando um mínimo de 100 avaliações), com média acima de 4,4, são (1) Livros Importados, (2) Livros de Interesse Geral e (3) Construção e Ferramentas.

Essas análises mostram que o desempenho comercial não é necessariamente acompanhado pela satisfação dos clientes — as categorias mais vendidas não são as mais bem avaliadas.

Com base nas avaliações (considerando pedidos acima de 100), a categoria que mais merece atenção pelo baixo desempenho é Móveis e Escritório, com 1.255 pedidos e nota 3,4.

## 4. O papel do pagamento no valor das compras
A forma de pagamento mais utilizada é o cartão de crédito, representando 78,86% das vendas. O ticket médio (preço + frete) dessa forma de pagamento é R$ 146,51 — acima do ticket médio geral de R$ 140,45.

Boleto é a segunda forma mais utilizada, com 17,48% das vendas. Cartão de débito e voucher somam, juntos, 3,66% das vendas.

Vale destacar que, apesar da baixa participação, o cartão de débito aparece com o segundo maior ticket médio entre as formas de pagamento: R$ 131,50.

## 5. Logística e experiência do cliente
O frete representa 14,34% do faturamento total.

Era esperado que estados mais distantes do eixo Sul-Sudeste tivessem fretes mais caros — o que se confirma. Mas chamou atenção um segundo padrão: esses mesmos estados apresentam ticket médio acima da média **mesmo quando o frete não é contabilizado**, ou seja, olhando só para o valor do produto. A Paraíba, por exemplo, é o estado com maior ticket médio de produto (R$ 196,09), enquanto São Paulo — líder em número de pedidos e faturamento — tem o menor (R$ 108,64).

Esse padrão sugere que a diferença regional de ticket médio não se explica apenas pelo custo de frete, podendo indicar também uma diferença de precificação ou de mix de produtos comprados por região. Caso essa hipótese se confirme em análises futuras, é interessante refletir sobre o potencial da Paraíba e de outros estados do Norte/Nordeste como foco de campanhas de vendas, dado o poder de compra evidenciado.

O valor do frete tem impacto pequeno na nota de avaliação (correlação de apenas -0,036), sugerindo que a insatisfação do cliente está ligada a outros fatores além do custo de entrega.

## 6. Clientes de maior valor
Foram identificados os 10 clientes com maior gasto total na base de dados (identificados por `customer_unique_id`, já que o dataset gera um ID novo por pedido):

- 0a0a92112bd4c708ca5fde585afaa872
- da122df9eeddfedc1dc1f5349a1a690c
- 763c8b1c9c68a0229c42c9fc6f662b93
- dc4802a71eae9be1dd28f5d788ceb526
- 459bef486812aa25204be022145caa62
- ff4159b92c40ebe40454e3e6a7c35ed6
- 4007669dec559734d6f53e029e360987
- 5d0a2980b292d049061542014e8960bf
- eebb5dda148d3893cdaf5b5ca3040ccb
- 48e1ac109decbb87765a3eade6854098

Esses clientes estão distribuídos entre os estados RJ, ES, MS, SP, MG, GO e PB. Essa distribuição reforça que, apesar da centralidade do Sudeste em volume, existe potencial de alto valor em outras regiões do país.

## 7. Síntese dos principais insights
1. São Paulo concentra 37,80% do faturamento no período, confirmando forte centralização das vendas no Sudeste — mas o ticket médio de produto em SP é o menor entre todos os estados.
2. O ticket médio sem considerar o frete já é maior nos estados mais distantes (ex: Paraíba, R$ 196,09) do que em São Paulo (R$ 108,64), sugerindo diferença de precificação/mix regional além do efeito do custo logístico.
3. O desempenho comercial (volume de vendas) e a satisfação do cliente (nota de avaliação) não caminham juntos — categorias líderes em vendas não são as mais bem avaliadas.
4. Cartão de crédito domina as vendas (78,86%) e também tem o maior ticket médio, sugerindo associação entre facilidade de parcelamento e compras de maior valor.
5. O frete tem participação relevante no faturamento (14,34%), mas pouca relação com a satisfação do cliente (correlação de -0,036) — a insatisfação parece estar ligada a outros fatores, possivelmente relacionados ao produto ou prazo de entrega.
6. Os clientes de maior valor individual estão espalhados por 7 estados diferentes, incluindo regiões fora do eixo Sul-Sudeste, indicando oportunidade de clientes de alto valor mesmo fora dos mercados mais concentrados.

## 8. Limitações e oportunidades de aprofundamento
- **Período de coleta:** os dados representam uma extração pontual da base da Olist; pedidos muito próximos à data de corte podem estar sub-representados, afetando a leitura de tendência nos últimos meses do período.
- **Hipótese de precificação regional não testada diretamente:** a diferença de ticket médio por estado (item 2 dos insights) é uma correlação observada, não uma causa comprovada — seria necessário cruzar com dados de categoria de produto por estado para confirmar se é mix de produto ou precificação de fato.
- **Sem dados de custo/margem:** a análise cobre receita e frete, mas não há informação de custo do produto ou margem de lucro, o que limita conclusões sobre rentabilidade real por estado ou categoria.
- **Próximos passos do projeto:** as próximas etapas (Power BI, Python e QGIS) vão aprofundar essas questões — em especial, o mapeamento geográfico via QGIS pode ajudar a investigar visualmente o padrão de precificação regional identificado aqui.

## 9. Conclusão
A análise do período de agosto de 2017 a agosto de 2018 confirma a forte concentração das vendas da Olist na região Sudeste, liderada por São Paulo — um padrão esperado dado o peso econômico e populacional da região. No entanto, os dados revelam nuances que vão além da concentração óbvia: estados mais distantes apresentam ticket médio mais alto mesmo sem considerar o frete, o desempenho de vendas nem sempre acompanha a satisfação do cliente, e existem clientes de alto valor distribuídos por diversas regiões do país.

Esses achados apontam para oportunidades de negócio que não são evidentes olhando apenas para volume de vendas — sugerindo que uma estratégia comercial mais granular, atenta a diferenças regionais e de categoria, poderia capturar valor adicional. As próximas etapas deste projeto (Power BI, Python e QGIS) vão aprofundar essas hipóteses, especialmente a relação entre geografia, precificação e comportamento do cliente.