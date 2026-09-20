# %%
import pandas as pd

order_payments_df = pd.read_csv(r'../../../data/raw/olist_order_payments_dataset.csv')
orders_df = pd.read_csv(r'../csv/dPedidos.csv')

# %%
pedidos_validos = orders_df['order_id'].tolist()

filtro = order_payments_df['order_id'].isin(pedidos_validos)
order_payments_df = order_payments_df[filtro]

# %%
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('_', ' ').str.title()
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('Credit Card', 'Cartao de Credito')
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('Debit Card', 'Cartao de Debito')
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('Not Defined', 'Nao Definido')

# %%
order_payments_df.to_csv(r'../csv/fPagamentos.csv', index=False)