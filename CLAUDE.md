# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This branch is focused on Task 1 of the FinRL Contest 2025: developing automated stock trading agents using reinforcement learning combined with large language models (LLMs). The task involves training agents on stock prices and financial news data using PPO/CPPO algorithms with optional DeepSeek LLM integration.

## Development Environment Setup

```bash
# Run the installation script on Ubuntu (128GB RAM recommended)
bash Task_1_FinRL_DeepSeek_Stock/installation_script.sh

# The script sets up:
# - Miniconda environment with Python 3.10
# - Essential dependencies: gcc, swig, box2d-py, mpi4py
# - FinRL and spinningup_pytorch libraries
# - Hugging Face datasets and related tools
# - Serena coding agent toolkit for enhanced code analysis
```

### MPI Environment Variables (Required)
```bash
# Set these before running MPI training commands
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
```

## Training Commands

All training commands should be run from the `Task_1_FinRL_DeepSeek_Stock/` directory.

### Standard Reinforcement Learning Training
```bash
# PPO training with 8 MPI processes (recommended)
mpirun --allow-run-as-root -np 8 python train_ppo.py > output_ppo.log 2>&1 &

# CPPO training (single process)
python train_cppo.py
```

### LLM-Enhanced Training (DeepSeek Integration)
```bash
# PPO with sentiment analysis signals
python train_ppo_llm.py

# CPPO with risk assessment signals
python train_cppo_llm_risk.py
```

### Training Monitoring
```bash
# Monitor training progress in real-time
tail -f output_ppo.log

# Key metrics to watch:
# - AverageEpRet: Average episode return (higher is better)
# - KL: KL divergence (should stay close to 0.01)
# - ClipFrac: Fraction of policy updates clipped (target: 0.1-0.3)
```

## Data Processing Pipeline

### Dataset Sources
- **Base dataset**: FNSPID (Hugging Face: `Zihan1004/FNSPID`) - Stock prices and news
- **LLM sentiment signals**: `benstaf/nasdaq_news_sentiment` - DeepSeek-generated sentiment
- **Risk assessment data**: `benstaf/risk_nasdaq` - DeepSeek-generated risk scores

### Data Generation Scripts
```bash
# Generate LLM signals (requires DeepSeek API access)
python sentiment_deepseek_deepinfra.py  # Create sentiment signals
python risk_deepseek_deepinfra.py       # Create risk assessments
```

### Data Processing for Training
```bash
# Standard RL training data (no LLM signals)
python train_trade_data.py

# LLM-enhanced training data
python train_trade_data_deepseek_sentiment.py  # Process sentiment data
python train_trade_data_deepseek_risk.py       # Process risk data
```

## Architecture Overview

### Core Components

#### Trading Environments
- **`env_stocktrading.py`**: Base environment for standard PPO/CPPO training
- **`env_stocktrading_llm.py`**: Enhanced environment integrating DeepSeek sentiment signals
- **`env_stocktrading_llm_01.py`**: Alternative LLM integration with different influence parameters
- **`env_stocktrading_llm_risk.py`**: CPPO environment with DeepSeek risk assessment integration
- **`env_stocktrading_llm_risk_01.py`**: Alternative risk-enhanced environment

#### Training Algorithms
- **PPO (Proximal Policy Optimization)**: Standard RL algorithm using MPI for parallel training
- **CPPO (Conservative Policy Optimization)**: Risk-aware variant of PPO for stable trading
- **LLM Integration**: DeepSeek language model signals augment state space with sentiment/risk

#### State Space Architecture
The trading agent observes:
1. **Technical indicators**: Price, volume, technical analysis features
2. **Portfolio state**: Current holdings, cash balance, previous actions
3. **LLM signals** (optional): Sentiment scores, risk assessments from news analysis
4. **Market features**: Turbulence indicators, volatility measures

#### Action Space
- **Continuous actions**: Portfolio weights for each stock (-1 to +1)
- **Transaction costs**: Buy/sell costs applied to encourage realistic trading
- **Position limits**: Maximum holdings per stock to manage risk

## Key File Patterns

### Training Scripts
- **`train_ppo.py`**: Main PPO training with MPI parallelization
- **`train_cppo.py`**: Conservative PPO training for risk-aware trading
- **`train_ppo_llm.py`**: PPO training with DeepSeek sentiment integration
- **`train_cppo_llm_risk.py`**: CPPO training with DeepSeek risk assessment

### Environment Implementations
- **`env_stocktrading*.py`**: Gymnasium-compatible trading environments
- Each environment variant supports different LLM signal integration approaches

### Data Processing Scripts
- **`train_trade_data*.py`**: Convert raw datasets into RL-ready format
- **`sentiment_deepseek_deepinfra.py`**: Generate sentiment signals via DeepSeek API
- **`risk_deepseek_deepinfra.py`**: Generate risk assessments via DeepSeek API

### Evaluation & Analysis
- **`FinRL_DeepSeek_backtest.ipynb`**: Backtesting notebook for trading performance
- **`hugging_face_upload.py`**: Utility for uploading results to Hugging Face

## Evaluation & Metrics

### Trading Performance Evaluation
Evaluation is performed using the `FinRL_DeepSeek_backtest.ipynb` notebook on trading data from 2019-2023.

#### Primary Metrics
- **Cumulative Return**: Total portfolio return over the trading period
- **Maximum Drawdown**: Largest peak-to-trough decline in portfolio value
- **Rachev Ratio**: Risk-adjusted return measure comparing upside vs downside risk

#### Additional Metrics (Recommended)
- **Outperformance Frequency**: Percentage of periods beating market benchmark
- **Sharpe Ratio**: Risk-adjusted returns using standard deviation
- **Sortino Ratio**: Risk-adjusted returns using downside deviation only

## Common Issues & Solutions

### System Requirements
- **RAM**: 128GB recommended for optimal PPO training with 8 MPI processes
- **Storage**: Ensure sufficient space for training logs and model checkpoints
- **GPU**: Not required but can accelerate neural network components

### MPI Training Issues
```bash
# If MPI fails, ensure root permissions are enabled
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

# Alternative: Run with fewer processes if memory limited
mpirun --allow-run-as-root -np 4 python train_ppo.py
```

### Training Debugging
- **Monitor log files**: Watch for convergence issues, NaN values, or memory errors
- **Check data quality**: Ensure no missing values or infinite numbers in market data
- **Validate environments**: Test environment reset/step functions before training
- **Resource monitoring**: Use `htop` or `nvidia-smi` to monitor system resources

## Serena Integration

### Overview
Serena is a powerful coding agent toolkit that provides semantic code capabilities for enhanced development workflows. It enables precise code navigation, analysis, and editing at the symbol level across the FinRL project.

### Key Features for FinRL Development
- **Semantic Code Analysis**: Navigate complex RL/LLM integration code with symbol-level understanding
- **Multi-language Support**: Full Python support for FinRL environments and training scripts
- **IDE-like Capabilities**: Advanced code retrieval and editing tools for large codebases
- **Agent Integration**: Works seamlessly with Claude Code for enhanced development assistance

### Usage Examples
```bash
# Serena is automatically installed via the installation script
# Use with Claude Code for enhanced code analysis and editing

# Example use cases:
# - Navigate complex trading environment implementations
# - Analyze PPO/CPPO algorithm integrations
# - Review LLM signal processing pipelines
# - Understand state space and action space architectures
```

### Benefits for Contest Development
- **Code Quality**: Enhanced semantic understanding for better refactoring
- **Debugging**: Improved symbol-level code navigation for issue resolution
- **Integration**: Better understanding of RL-LLM integration patterns
- **Maintenance**: Efficient codebase management for contest submissions