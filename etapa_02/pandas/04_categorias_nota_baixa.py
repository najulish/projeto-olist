# %% 
import pandas as pd

order_items_df = pd.read_csv(r'../../data/raw/olist_order_items_dataset.csv')
products_df = pd.read_csv(r'../../data/tratado/olist_products_dataset.csv')
order_review_df = pd.read_csv(r'../../data/raw/olist_order_reviews_dataset.csv')

# %%
join_df = (order_items_df.merge(products_df, how='left', on='product_id')
                         .merge(order_review_df, how='left', on='order_id'))
join_df = join_df[['order_id', 'product_category_name', 'review_score']]

# %%
join_df = (join_df.groupby('product_category_name')
                  .agg({'order_id': ['count'],
                        'review_score': ['mean']})
                  .reset_index())
# %%
join_df.columns = ['Categoria', 'Num. Pedidos', 'Nota Média']
filtro = (join_df['Num. Pedidos']>20) & (join_df['Nota Média']<3.5)
join_df = join_df[filtro].round(2)
join_df

# %%
join_df.to_csv(r'../csv/categorias_nota_baixa.csv', index=False)