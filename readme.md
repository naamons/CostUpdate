# CostSyncer: MRPeasy to Shopify COGS Update

CostSyncer is a Streamlit application designed to synchronize inventory costs from MRPeasy to Shopify, facilitating accurate COGS (Cost of Goods Sold) calculations.

## Features

- Upload a CSV file containing SKU and cost data from MRPeasy.
- Fetch Shopify products to create a mapping of Shopify product ID to variant SKU.
- Compare SKUs from the CSV with Shopify's inventory and update the cost in Shopify.
- Display a report of the updates within the Streamlit UI.

## Setup Instructions

1. **Clone the repository** or download the provided Python script to your local machine.

2. **Install Required Packages**: Ensure you have Python installed on your system. Then, install the required packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Streamlit Secrets**: Add your Shopify API credentials to Streamlit's secrets. Create a `.streamlit/secrets.toml` file in your project directory with the following structure:

    ```toml
    [shopify]
    admin_api_access_token = "YOUR_SHOPIFY_ADMIN_API_ACCESS_TOKEN"
    store_name = "YOUR_SHOPIFY_STORE_NAME"
    ```

    Replace the placeholders with your actual Shopify Admin API access token and store name.

4. **Run the Application**: Navigate to the directory containing the script and run the application using Streamlit:

    ```bash
    streamlit run your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python script.

## Usage Guide

- **Start the Application**: Access the Streamlit application in your web browser following the URL displayed in the terminal.
- **Upload CSV**: Click on the 'Upload MRPeasy CSV' button to upload your CSV file containing the SKU and cost data.
- **Synchronize Costs**: Click on the 'Sync Inventory Costs' button to start the synchronization process. The application will fetch Shopify products, create a SKU mapping, compare SKUs, update costs in Shopify, and display a report of the updates.

## Note

This application is designed for use with Shopify and MRPeasy platforms. Ensure you have the necessary permissions and access rights to use the APIs and modify inventory data.
