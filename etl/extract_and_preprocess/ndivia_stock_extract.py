# Libraries importing
from datetime import datetime
import yfinance as yf
import pandas as pd

# Extract all available nvidia stock daily
def nvidia_stock_extract():
    try:
        # Set the ticker symbol for Nvidia
        ticker = 'NVDA'

        # Download all available stock data
        nvda_stock = yf.download(ticker, period="max")

        # Reset index to make 'Date' a column (if you want to move it from index)
        nvda_stock.reset_index(inplace=True)

        # Saving into a csv file for further use
        nvda_stock.to_csv('./data/raw_data/data_to_s3/nvidia_stock_full_time.csv', index=False)
    except Exception as e:
        print(f"Error as: {e}")

if __name__ =="__main__":
    print(f"Starting fetch Nvidia stock indexes...")
    nvidia_stock_extract()
    print(f"Fetched data successfully.")
