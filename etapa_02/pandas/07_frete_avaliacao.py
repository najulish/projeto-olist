# %%
import pandas as pd
import numpy as np

order_items_df = pd.read_csv(r"..\..\data\raw\olist_order_items_dataset.csv")
order_reviews_df = pd.read_csv(r"..\..\data\raw\olist_order_reviews_dataset.csv")

# %%
condicoes = [order_items_df['freight_value'] < 15,
             order_items_df['freight_value'] < 30,
             order_items_df['freight_value'] < 50]

valores = ['Baixo', 'Médio', 'Alto']

order_items_df['faixa_frete'] = np.select(condicoes, 
                                          valores, 
                                          default='Muito Alto')

# %%
order_items_df = order_items_df[['order_id','faixa_frete']]
join_df = order_items_df.merge(order_reviews_df, how='left', on='order_id')
join_df = join_df[['order_id', 'review_score','faixa_frete']]
join_df = (join_df.groupby('faixa_frete')
                  .agg({'order_id': ['count'],
                        'review_score': ['mean']})
                  .reset_index())
join_df.columns = ['faixa_frete', 'num_avaliacoes', 'media_avaliacao']
join_df[['media_avaliacao']] = join_df[['media_avaliacao']].round(2)
join_df

# %%
join_df.to_csv(r'../csv/frete_avaliacao.csv', index=False)