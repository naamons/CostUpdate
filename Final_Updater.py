import streamlit as st
import pandas as pd
import requests
import json

# Function to load credentials securely
def load_credentials():
    shopify_token = st.secrets["shopify"]["admin_api_access_token"]
    shopify_store_name = st.secrets["shopify"]["store_name"]
    return shopify_token, shopify_store_name

shopify_token, shopify_store_name = load_credentials()

# Function to read MRPeasy CSV data
@st.cache
def load_mrpeasy_data(file):
    data = pd.read_csv(file)
    return data

# Function to fetch Shopify products
def fetch_shopify_products():
    url = f"https://{shopify_store_name}.myshopify.com/admin/api/2022-04/products.json"
    headers = {"X-Shopify-Access-Token": shopify_token}
    response = requests.get(url, headers=headers)
    products = response.json()["products"]
    return products

# Function to create SKU to Shopify ID mapping
def create_sku_mapping(products):
    mapping = {}
    for product in products:
        for variant in product["variants"]:
            sku = variant["sku"]
            id = variant["id"]
            mapping[sku] = id
    return mapping

# Function to update Shopify product cost
def update_shopify_cost(product_id, cost):
    url = f"https://{shopify_store_name}.myshopify.com/admin/api/2022-04/variants/{product_id}.json"
    headers = {"X-Shopify-Access-Token": shopify_token, "Content-Type": "application/json"}
    payload = {
        "variant": {
            "id": product_id,
            "cost": cost
        }
    }
    response = requests.put(url, json=payload, headers=headers)
    return response.status_code == 200

# Streamlit UI
st.title('CostSyncer: MRPeasy to Shopify COGS Update')

uploaded_file = st.file_uploader("Upload MRPeasy CSV", type=['csv'])
if uploaded_file is not None:
    data = load_mrpeasy_data(uploaded_file)
    if st.button('Sync Inventory Costs'):
        with st.spinner('Fetching Shopify products...'):
            products = fetch_shopify_products()
        
        sku_mapping = create_sku_mapping(products)
        updates, skips = 0, 0

        for _, row in data.iterrows():
            sku, cost = row['Part No.'], row['Cost']
            shopify_id = sku_mapping.get(sku)

            if shopify_id and pd.notnull(cost):
                success = update_shopify_cost(shopify_id, cost)
                if success:
                    updates += 1
                    st.write(f"Updated {sku} with cost {cost}")
                else:
                    skips += 1
                    st.error(f"Failed to update {sku}")
            else:
                skips += 1
                st.warning(f"Skipped {sku}: Not found or invalid cost")

        st.success(f"Sync completed. Updates: {updates}, Skipped: {skips}.")
