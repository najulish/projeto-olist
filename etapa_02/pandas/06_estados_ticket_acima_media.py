# %%
import pandas as pd

order_items_df = pd.read_csv(r"..\..\data\raw\olist_order_items_dataset.csv")
customers_df = pd.read_csv(r"..\..\data\tratado\olist_customers_dataset.csv")
orders_df = pd.read_csv(r"..\..\data\raw\olist_orders_dataset.csv")
# %%
ticket_medio = (order_items_df["price"] + order_items_df["freight_value"]).mean()
ticket_medio = ticket_medio.round(2)
ticket_medio

# %%
join_df = (orders_df.merge(order_items_df, how='left', on='order_id')
                    .merge(customers_df, how='left', on='customer_id'))
join_df['Ticket Médio'] = join_df['price'] + join_df['freight_value']
join_df = (join_df.groupby('customer_state')[['Ticket Médio']]
                  .mean())
filtro = join_df['Ticket Médio'] > ticket_medio
join_df = join_df[filtro].round(2)
join_df = join_df['Ticket Médio'].sort_values(ascending=False).reset_index()

# %%
join_df.to_csv(r'../csv/estados_ticket_acima_media.csv', index=False)