# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains the starter kits and materials for the FinRL Contest 2025, featuring four distinct tasks that combine financial machine learning, reinforcement learning, and large language models. The contest focuses on automated trading, factor mining, and financial language understanding.

## Development Environment Setup

### Task 1 (FinRL-DeepSeek Stock Trading)
```bash
# Run the installation script on Ubuntu (128GB RAM recommended)
bash Task_1_FinRL_DeepSeek_Stock/installation_script.sh

# The script sets up:
# - Miniconda environment with Python 3.10
# - Essential dependencies: gcc, swig, box2d-py, mpi4py
# - FinRL and spinningup_pytorch libraries
# - Hugging Face datasets and related tools
```

### Task 2 (AlphaSeek Crypto Trading)
```bash
cd Task_2_FinRL_AlphaSeek_Crypto/
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Task 3 (FinLLM Models with ReFT)
- Uses Google Colab with A100 GPU
- Evaluation through PIXIU framework
- Requires Hugging Face authentication tokens

### Task 4 (Digital Regulatory Reporting)
- Model size should not exceed 8B parameters
- Requires access to CDM, MOF, and XBRL documentation
- Uses FActScore and accuracy metrics for evaluation

## Training Commands

### Task 1: Stock Trading with PPO/CPPO
```bash
# Standard PPO training (8 processes)
mpirun --allow-run-as-root -np 8 python train_ppo.py > output_ppo.log 2>&1 &

# CPPO training
python train_cppo.py

# PPO with DeepSeek LLM integration
python train_ppo_llm.py

# CPPO with risk assessment
python train_cppo_llm_risk.py

# Monitor training progress in logs:
# Key metrics: AverageEpRet, KL, ClipFrac
tail -f output_ppo.log
```

### Task 2: Crypto Factor Mining & Ensemble
```bash
# 1. Generate Alpha101 factors
python seq_data.py

# 2. Train RNN model for factor aggregation
python seq_run.py

# 3. Train DQN reinforcement learning agent
python erl_run.py

# 4. Train ensemble models
python task2_ensemble.py

# 5. Evaluate ensemble performance
python task2_eval.py
```

### Task 3: FinLLM Model Evaluation
```bash
# Run in Google Colab with A100 GPU
# See evaluate_models.ipynb for complete evaluation pipeline
python PIXIU/src/eval.py \
    --model "hf-causal-vllm" \
    --model_args "pretrained=your-model,tokenizer=your-tokenizer" \
    --tasks "flare_ner,flare_finqa,flare_tatqa" \
    --batch_size 20000 \
    --num_fewshot 0
```

## Data Processing Pipeline

### Task 1: Stock Trading Data
- Base dataset: FNSPID (Hugging Face: `Zihan1004/FNSPID`)
- LLM sentiment signals: `benstaf/nasdaq_news_sentiment`
- Risk assessment data: `benstaf/risk_nasdaq`
- Processing scripts:
  - `sentiment_deepseek_deepinfra.py` - Generate sentiment signals
  - `risk_deepseek_deepinfra.py` - Generate risk assessments
  - `train_trade_data_deepseek_sentiment.py` - Process sentiment data
  - `train_trade_data_deepseek_risk.py` - Process risk data

### Task 2: Crypto Trading Data
- BTC_1sec.csv: Second-level Limit Order Book data
- Alpha101 technical factors generated from price data
- RNN-processed strong factors for trading signals

### Task 4: Regulatory Data Sources
- CDM: [FINOS CDM Documentation](https://cdm.finos.org/)
- MOF: [OSI License Database](https://opensource.org/licenses)
- XBRL: [SEC EDGAR Filings](https://www.sec.gov/edgar/searchedgar/companysearch)

## Architecture Overview

### Task 1: RL + LLM Integration
- **Environments**: `env_stocktrading*.py` files provide different configurations
  - `env_stocktrading.py`: Standard PPO/CPPO environment
  - `env_stocktrading_llm*.py`: LLM-enhanced environments with sentiment/risk
- **Training**: PPO/CPPO algorithms with optional LLM signal integration
- **Evaluation**: Cumulative Return, Maximum Drawdown, Rachev Ratio

### Task 2: Multi-Stage Pipeline
- **Factor Mining**: `seq_*.py` modules for technical factor generation
- **Deep Learning**: LSTM+GRU networks for factor aggregation
- **Reinforcement Learning**: DQN agent in `erl_*.py` modules
- **Ensemble**: Multiple model voting schemes in `task2_ensemble.py`

### Task 3: LLM Evaluation Framework
- Uses PIXIU evaluation framework
- 41 financial tasks across multiple domains
- Supports Hugging Face model integration with LoRA adapters

### Task 4: Regulatory QA System
- Three domains: CDM (122 QA pairs), MOF (140 QA pairs), XBRL (861 QA pairs)
- Metrics: FActScore for comprehension, Accuracy for classification
- Fine-tuning with domain-specific regulatory texts

## Key File Patterns

### Environment Files
- `env_stocktrading*.py` - Trading environment implementations
- `trade_simulator.py` - Market replay simulator for crypto

### Training Scripts
- `train_*.py` - Main training entry points
- `*_run.py` - Execution frameworks for different models

### Data Processing
- `*_data*.py` - Data preprocessing and feature engineering
- `seq_*.py` - Sequential model components
- `erl_*.py` - Ensemble reinforcement learning components

### Configuration
- `*_config.py` - Model and environment configurations
- `requirements.txt` - Python dependencies
- `installation_script.sh` - System setup automation

## Evaluation & Metrics

### Task 1 Evaluation
```python
# Backtest evaluation in FinRL_DeepSeek_backtest.ipynb
# Key metrics: Cumulative Return, Maximum Drawdown, Rachev Ratio
# Trading period: 2019-2023
```

### Task 2 Evaluation
```python
# Initial cash: $1 million
# Metrics: Cumulative return, win/loss rate, Sharpe ratio
# Ensemble voting mechanism in task2_eval.py
```

### Task 3 Evaluation
- Average score across all FinLLM Leaderboard tasks
- Automated evaluation through PIXIU framework
- Task-specific metrics defined by Open FinLLM Leaderboard

### Task 4 Evaluation
- FActScore for reading comprehension tasks
- Accuracy for classification and math problems
- Average score across CDM, MOF, and XBRL domains

## Common Issues & Solutions

### Memory Requirements
- Task 1: Requires 128GB RAM for optimal training
- Task 3: Requires A100 GPU for model evaluation
- Use batch processing and gradient accumulation for large models

### MPI Training Issues
```bash
# If MPI fails, ensure root permissions are enabled
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
```

### Data Leakage Prevention
- Task 2: Check Alpha101 factors for future information leakage
- Ensure validation sets are properly held out from training data
- Monitor unusual validation loss patterns

### Model Size Constraints
- Task 4: Models should not exceed 8B parameters
- Use quantization and pruning techniques if needed
- Consider LoRA adapters for parameter-efficient fine-tuning