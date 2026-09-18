# %%
import pandas as pd

order_payments_df = pd.read_csv(r'../../data/tratado/olist_order_payments_dataset.csv')

# %%
order_payments_df = order_payments_df[['payment_type', 'payment_value']]

# %%
order_payments_df = (order_payments_df.groupby('payment_type')
                     ['payment_value'].mean()
                     .reset_index())

order_payments_df['payment_value'] = order_payments_df['payment_value'].round(2)
order_payments_df

# %%
order_payments_df.to_csv(r'../csv/ticket_medio_pagamento.csv', index=False)