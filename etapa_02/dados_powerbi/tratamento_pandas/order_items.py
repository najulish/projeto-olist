# %%
import pandas as pd

order_items_df = pd.read_csv(r'../../../data/raw/olist_order_items_dataset.csv', sep=';', decimal=',')
orders_df = pd.read_csv(r'../csv/dPedidos.csv')

# %%
pedidos_validos = orders_df['order_id'].tolist()

filtro = order_items_df['order_id'].isin(pedidos_validos)
order_items_df = order_items_df[filtro]

# %%
order_items_df['total'] = order_items_df['price'] + order_items_df['freight_value']

# %%
order_items_df.to_csv(r'../csv/fPedidos_Items.csv', index=False)