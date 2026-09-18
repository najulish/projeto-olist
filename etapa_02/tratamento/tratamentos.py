# %%
import pandas as pd

products_df = pd.read_csv(r'../../data/raw/olist_products_dataset.csv')

products_df['product_category_name'] = products_df['product_category_name'].str.replace('_', ' ').str.title()

# %%
products_df.to_csv(r'../../data/tratado/olist_products_dataset.csv', index=False)

# %%
order_payments_df = pd.read_csv(r'../../data/raw/olist_order_payments_dataset.csv')
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('_', ' ').str.title()
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('Credit Card', 'Cartao de Credito')
order_payments_df['payment_type'] = order_payments_df['payment_type'].str.replace('Debit Card', 'Cartao de Debito')

# %%
order_payments_df.to_csv(r'../../data/tratado/olist_order_payments_dataset.csv', index=False)

# %%
customers_df = pd.read_csv(r'../../data/raw/olist_customers_dataset.csv')
customers_df['customer_city'] = customers_df['customer_city'].str.title()

# %%
customers_df.to_csv(r'../../data/tratado/olist_customers_dataset.csv', index=False)