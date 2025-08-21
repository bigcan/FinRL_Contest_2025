#!/usr/bin/env python3
"""
Download just the LLM signal CSV files we need
"""

import os
import sys
import urllib.request
import pandas as pd
from huggingface_hub import hf_hub_download

def download_llm_files():
    """Download sentiment and risk CSV files from HuggingFace"""
    
    print("🚀 Downloading LLM signal files...")
    
    files_to_download = [
        {
            'repo': 'benstaf/nasdaq_news_sentiment', 
            'file': 'sentiment_deepseek_new_cleaned_nasdaq_news_full.csv',
            'local': 'sentiment_deepseek.csv'
        },
        {
            'repo': 'benstaf/risk_nasdaq',
            'file': 'risk_deepseek_cleaned_nasdaq_news_full.csv', 
            'local': 'risk_deepseek.csv'
        }
    ]
    
    success_count = 0
    
    for item in files_to_download:
        try:
            print(f"📥 Downloading {item['file']} from {item['repo']}...")
            
            # Download file
            downloaded_path = hf_hub_download(
                repo_id=item['repo'],
                filename=item['file'],
                repo_type="dataset",
                cache_dir="./hf_cache"
            )
            
            # Copy to local filename
            import shutil
            shutil.copy2(downloaded_path, item['local'])
            
            # Check the file
            if os.path.exists(item['local']):
                size_mb = os.path.getsize(item['local']) / (1024*1024)
                print(f"✅ Success: {item['local']} ({size_mb:.1f}MB)")
                
                # Quick preview
                try:
                    df = pd.read_csv(item['local'], nrows=3)
                    print(f"   Preview: {len(df.columns)} columns, shape: {df.shape}")
                    print(f"   Columns: {list(df.columns)[:5]}...")
                except Exception as e:
                    print(f"   Warning: Could not preview CSV: {e}")
                
                success_count += 1
            else:
                print(f"❌ Failed: {item['local']} not created")
                
        except Exception as e:
            print(f"❌ Error downloading {item['file']}: {e}")
    
    print(f"\n📊 Download Summary: {success_count}/{len(files_to_download)} files downloaded")
    
    if success_count == len(files_to_download):
        print("🎉 All LLM data files downloaded successfully!")
        print("\nYou can now run:")
        print("1. python train_trade_data_deepseek_sentiment.py")
        print("2. python train_trade_data_deepseek_risk.py") 
        print("3. python train_ppo_llm.py (PPO with sentiment)")
        print("4. python train_cppo_llm_risk.py (CPPO with risk)")
    else:
        print("⚠️  Some files failed to download. Check errors above.")
    
    return success_count == len(files_to_download)

if __name__ == "__main__":
    download_llm_files()