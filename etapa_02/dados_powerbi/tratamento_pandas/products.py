# %%
import pandas as pd

products_df = pd.read_csv(r'../../../data/raw/olist_products_dataset.csv')

# %%
products_df['product_category_name'] = products_df['product_category_name'].str.replace('_', ' ').str.title()
products_df['product_category_name'] = products_df['product_category_name'].fillna('Nao Informado')

# %%
products_df = products_df[['product_id', 'product_category_name']]

# %%
products_df.to_csv(r'../csv/dProdutos.csv', index=False)