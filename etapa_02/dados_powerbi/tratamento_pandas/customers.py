# %%
import pandas as pd

customers_df = pd.read_csv(r'../../../data/raw/olist_customers_dataset.csv')
orders_df = pd.read_csv(r'../csv/dPedidos.csv')

# %%
customers_df['customer_city'] = customers_df['customer_city'].str.title()

# %%
clientes_validos = orders_df['customer_id'].tolist()

filtro = customers_df['customer_id'].isin(clientes_validos)
customers_df = customers_df[filtro]

# %%
customers_df.to_csv(r'../csv/dClientes.csv', index=False)