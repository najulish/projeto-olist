# %%
import pandas as pd

order_items_df = pd.read_csv(r"..\..\data\raw\olist_order_items_dataset.csv")
orders_df = pd.read_csv(r"..\..\data\raw\olist_orders_dataset.csv")
customers_df = pd.read_csv(r"..\..\data\raw\olist_customers_dataset.csv")

# %%
join_df = (orders_df.merge(order_items_df, how='left', on='order_id')
                    .merge(customers_df, how='left', on='customer_id'))
join_df['total'] = join_df['price'] + join_df['freight_value']
join_df = (join_df.groupby('customer_unique_id')['total']
                  .sum()
                  .nlargest(10)
                  .reset_index())
join_df

# %%
join2_df = customers_df.sort_values('customer_id')
join2_df = join2_df.drop_duplicates(subset='customer_unique_id')
join2_df = join2_df[['customer_unique_id', 
                    'customer_zip_code_prefix', 
                    'customer_city', 
                    'customer_state']]

# %%
top10 = join_df.merge(join2_df, how='left', on='customer_unique_id')
top10

# %%
top10.to_csv(r'../csv/top10_clientes.csv', index=False)