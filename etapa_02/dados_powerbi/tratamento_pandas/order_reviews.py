# %%
import pandas as pd

order_reviews_df = pd.read_csv(r'../../../data/raw/olist_order_reviews_dataset.csv', parse_dates=['review_creation_date'])
orders_df = pd.read_csv(r'../csv/dPedidos.csv')

# %%
order_reviews_df = order_reviews_df.drop(['review_comment_title',	'review_comment_message', 'review_answer_timestamp'], axis=1)

# %%
pedidos_validos = orders_df['order_id'].tolist()

filtro = order_reviews_df['order_id'].isin(pedidos_validos)
order_reviews_df = order_reviews_df[filtro]

# %%
order_reviews_df.to_csv(r'../csv/fAvaliacoes.csv', index=False)