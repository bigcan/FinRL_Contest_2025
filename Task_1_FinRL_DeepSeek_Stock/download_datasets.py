#!/usr/bin/env python3
"""
Download required datasets for FinRL-DeepSeek Task 1
"""

import os
import pandas as pd
from datasets import load_dataset
from huggingface_hub import hf_hub_download
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_fnspid_dataset():
    """Download FNSPID base dataset containing stock prices and news"""
    logger.info("Downloading FNSPID dataset (5.73GB)...")
    try:
        # Download the specific file we need
        dataset = load_dataset("Zihan1004/FNSPID")
        
        # Save to local CSV for easier processing
        train_data = dataset['train']
        df = train_data.to_pandas()
        
        logger.info(f"FNSPID dataset loaded: {len(df)} rows, {len(df.columns)} columns")
        logger.info(f"Columns: {list(df.columns)}")
        
        # Save the main dataset
        csv_path = "fnspid_nasdaq_data.csv"
        df.to_csv(csv_path, index=False)
        logger.info(f"Saved FNSPID data to {csv_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error downloading FNSPID dataset: {e}")
        return False

def download_sentiment_dataset():
    """Download LLM sentiment dataset"""
    logger.info("Downloading sentiment dataset...")
    try:
        dataset = load_dataset("benstaf/nasdaq_news_sentiment")
        
        train_data = dataset['train']
        df = train_data.to_pandas()
        
        logger.info(f"Sentiment dataset loaded: {len(df)} rows, {len(df.columns)} columns")
        logger.info(f"Columns: {list(df.columns)}")
        
        # Save for processing
        csv_path = "sentiment_deepseek_raw.csv"
        df.to_csv(csv_path, index=False)
        logger.info(f"Saved sentiment data to {csv_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error downloading sentiment dataset: {e}")
        return False

def download_risk_dataset():
    """Download LLM risk dataset"""
    logger.info("Downloading risk dataset...")
    try:
        dataset = load_dataset("benstaf/risk_nasdaq")
        
        train_data = dataset['train']
        df = train_data.to_pandas()
        
        logger.info(f"Risk dataset loaded: {len(df)} rows, {len(df.columns)} columns")
        logger.info(f"Columns: {list(df.columns)}")
        
        # Save for processing
        csv_path = "risk_deepseek_raw.csv"
        df.to_csv(csv_path, index=False)
        logger.info(f"Saved risk data to {csv_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error downloading risk dataset: {e}")
        return False

def main():
    """Download all required datasets"""
    logger.info("Starting dataset download process...")
    
    # Change to the correct directory
    os.chdir("/mnt/c/FinRL/FinRL_Contest_2025/Task_1_FinRL_DeepSeek_Stock")
    
    success_count = 0
    total_datasets = 3
    
    # Download each dataset
    if download_fnspid_dataset():
        success_count += 1
        
    if download_sentiment_dataset():
        success_count += 1
        
    if download_risk_dataset():
        success_count += 1
    
    logger.info(f"Download complete: {success_count}/{total_datasets} datasets downloaded successfully")
    
    if success_count == total_datasets:
        logger.info("✅ All datasets downloaded successfully!")
        logger.info("Next steps:")
        logger.info("1. Process sentiment data: python sentiment_deepseek_deepinfra.py") 
        logger.info("2. Process risk data: python risk_deepseek_deepinfra.py")
        logger.info("3. Generate training data: python train_trade_data.py")
    else:
        logger.warning(f"⚠️  Only {success_count}/{total_datasets} datasets downloaded")

if __name__ == "__main__":
    main()