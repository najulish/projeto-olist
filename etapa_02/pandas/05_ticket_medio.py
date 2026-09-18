# %%
import pandas as pd

order_items_df = pd.read_csv(r"..\..\data\raw\olist_order_items_dataset.csv")

# %%
ticket_medio = (order_items_df["price"] + order_items_df["freight_value"]).mean()
ticket_medio.round(2)