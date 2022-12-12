import streamlit as st
import pandas as pd
from helper_functions import get_items_list, hide_table_index

# TODO refactor page configuration into function (?)


def reformat_items_df(json_data):
    df = pd.DataFrame(json_data)
    df.rename(
        columns={
            'item_name': 'ITEM', 'item_category': 'CATEGORY',
            'item_description': 'DESCRIPTION', 'price': 'PRICE',
            'sell_price': 'SELL PRICE', 'sell_location': 'SHOP'},
        inplace=True)

    df = df.astype({'PRICE': 'Int64', 'SELL PRICE': 'Int64'})
    df = df[['ITEM', 'CATEGORY', 'DESCRIPTION', 'PRICE', 'SELL PRICE', 'SHOP']]
    return df


def query_item_data(df):
    if category_search and shop_search:
        df = df.query("CATEGORY == @category_search & SHOP == @shop_search")
    elif category_search:
        df = df.query("CATEGORY == @category_search")
    elif shop_search:
        df = df.query("SHOP == @shop_search")

    return df


if __name__ == "__main__":
    item_data = get_items_list()
    item_data = reformat_items_df(item_data)

    st.markdown("## Items Table")
    category_search = st.multiselect(label="Search by category",
                                     options=item_data['CATEGORY'].unique(),)
    shop_search = st.multiselect(label="Search by category",
                                 options=item_data['SHOP'].unique(),)

    item_data = query_item_data(item_data)

    hide_table_index()

    st.table(item_data)
