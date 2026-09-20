# %%
import pandas as pd

orders_df = pd.read_csv(
    r'../../../data/raw/olist_orders_dataset.csv',
    parse_dates=[
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
)

orders_df['order_purchase_date'] = orders_df['order_purchase_timestamp'].dt.date

orders_df = orders_df[
    (orders_df['order_purchase_timestamp'] >= '2017-08-01') &
    (orders_df['order_purchase_timestamp'] < '2018-09-01')
]

# %%
orders_df.to_csv(r'../csv/dPedidos.csv', index=False)