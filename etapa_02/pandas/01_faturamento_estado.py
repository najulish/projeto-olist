# %%
import pandas as pd

order_items_df = pd.read_csv(r"..\..\data\raw\olist_order_items_dataset.csv")
orders_df = pd.read_csv(r"..\..\data\raw\olist_orders_dataset.csv")
customers_df = pd.read_csv(r"..\..\data\raw\olist_customers_dataset.csv")

# %%
order_items_df["total"] = order_items_df["price"] + order_items_df["freight_value"]
order_items_df = order_items_df[["order_id", "total"]]

# %%
join_df = (order_items_df.merge(orders_df, how='left', on='order_id')
           .merge(customers_df, how='left', on='customer_id'))
join_df = (join_df[['customer_state','total']]
           .groupby(['customer_state'])
           .sum()['total']
           .sort_values(ascending=False)
           .reset_index())

# %%
join_df.to_csv(r'../csv/faturamento_estado.csv', index=False)