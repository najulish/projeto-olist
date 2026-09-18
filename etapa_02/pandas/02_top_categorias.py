# %%
import pandas as pd

orders_df = pd.read_csv('../../data/raw/olist_orders_dataset.csv')
order_items_df =  pd.read_csv('../../data/raw/olist_order_items_dataset.csv')
products_df = pd.read_csv('../../data/tratado/olist_products_dataset.csv')

# %%
join_df = (orders_df.merge(order_items_df, how='left', on='order_id')
                    .merge(products_df, how='left', on='product_id'))

# %%
join_df['Faturamento'] = join_df['price'] + join_df['freight_value']
join_df = join_df[['product_category_name', 'Faturamento']]

# %%
join_df = (join_df.groupby('product_category_name')['Faturamento']
                  .sum()
                  .sort_values(ascending=False)
                  .reset_index())
join_df

# %%
join_df.to_csv(r'../csv/top_categorias.csv', index=False)