#!/usr/bin/env python3
"""
Download only the key files we need for FinRL-DeepSeek Task 1
"""

import os
import pandas as pd
from huggingface_hub import hf_hub_download
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_file_from_repo(repo_id, filename, local_filename=None):
    """Download a specific file from a HuggingFace repository"""
    try:
        if local_filename is None:
            local_filename = filename.split('/')[-1]  # Get just the filename
            
        logger.info(f"Downloading {filename} from {repo_id}...")
        
        downloaded_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            repo_type="dataset",
            local_dir="./",
            local_dir_use_symlinks=False
        )
        
        # Move to desired filename if different
        if downloaded_path != local_filename:
            os.rename(downloaded_path, local_filename)
            
        logger.info(f"✅ Downloaded {filename} as {local_filename}")
        
        # Show file info
        if local_filename.endswith('.csv'):
            df = pd.read_csv(local_filename, nrows=5)  # Just peek at first 5 rows
            logger.info(f"   Preview: {len(df.columns)} columns, sample: {list(df.columns)[:5]}")
            
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to download {filename}: {e}")
        return False

def main():
    """Download key files only"""
    logger.info("Downloading key dataset files...")
    
    # Change to the correct directory
    os.chdir("/mnt/c/FinRL/FinRL_Contest_2025/Task_1_FinRL_DeepSeek_Stock")
    
    downloads = [
        # FNSPID dataset - key file
        ("Zihan1004/FNSPID", "Stock_news/nasdaq_exteral_data.csv", "nasdaq_external_data.csv"),
        
        # Sentiment dataset  
        ("benstaf/nasdaq_news_sentiment", "sentiment_deepseek_new_cleaned_nasdaq_news_full.csv", "sentiment_deepseek.csv"),
        
        # Risk dataset
        ("benstaf/risk_nasdaq", "risk_deepseek_cleaned_nasdaq_news_full.csv", "risk_deepseek.csv"),
    ]
    
    success_count = 0
    
    for repo_id, filename, local_name in downloads:
        if download_file_from_repo(repo_id, filename, local_name):
            success_count += 1
    
    logger.info(f"\n📊 Download Summary: {success_count}/{len(downloads)} files downloaded")
    
    if success_count == len(downloads):
        logger.info("🎉 All key dataset files downloaded successfully!")
        logger.info("\nNext steps:")
        logger.info("1. Run training data generation: python train_trade_data.py")
        logger.info("2. Run LLM training data: python train_trade_data_deepseek_sentiment.py")
        logger.info("3. Run risk training data: python train_trade_data_deepseek_risk.py")
    else:
        logger.warning(f"⚠️  Only {success_count}/{len(downloads)} files downloaded successfully")

if __name__ == "__main__":
    main()