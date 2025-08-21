#!/usr/bin/env python3
"""
Create seagen.csv from Yahoo Finance data
"""

import pandas as pd
import yfinance as yf
from datetime import datetime

def create_seagen_csv():
    """Download SGEN data and save as seagen.csv"""
    print("Downloading SGEN data from Yahoo Finance...")
    
    try:
        # Download SGEN data
        ticker = yf.Ticker("SGEN")
        data = ticker.history(start="2013-01-01", end="2023-12-31")
        
        if data.empty:
            print("No SGEN data available, creating empty file...")
            # Create empty CSV with expected columns
            empty_df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Price', 'Vol.', 'Change %'])
            empty_df.to_csv('seagen.csv', index=False)
            return
        
        # Reset index to make Date a column
        data = data.reset_index()
        
        # Rename columns to match expected format
        data = data.rename(columns={
            'Date': 'Date',
            'Open': 'Open', 
            'High': 'High',
            'Low': 'Low',
            'Close': 'Price',  # Price column expects Close price
            'Volume': 'Vol.'
        })
        
        # Calculate Change %
        data['Change %'] = data['Price'].pct_change() * 100
        
        # Select only the columns we need
        columns_needed = ['Date', 'Open', 'High', 'Low', 'Price', 'Vol.', 'Change %']
        data = data[columns_needed]
        
        # Save to CSV
        data.to_csv('seagen.csv', index=False)
        print(f"✅ Created seagen.csv with {len(data)} rows")
        print(f"Date range: {data['Date'].min()} to {data['Date'].max()}")
        
    except Exception as e:
        print(f"Error downloading SGEN: {e}")
        print("Creating empty seagen.csv file...")
        # Create empty CSV with expected columns
        empty_df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Price', 'Vol.', 'Change %'])
        empty_df.to_csv('seagen.csv', index=False)

if __name__ == "__main__":
    create_seagen_csv()