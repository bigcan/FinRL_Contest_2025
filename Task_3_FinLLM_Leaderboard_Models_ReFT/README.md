# Task 3 Open FinLLM Leaderboard -- Models with Reinforcement Fine-Tuning

This task aims to encourage the community to learn, maintain, and update the [Open FinLLM Leaderboard](https://huggingface.co/spaces/finosfoundation/Open-Financial-LLM-Leaderboard) – add new models (rows) to the leaderboard. In this task, participants are expected to submit their models and compete for high rankings in the leaderboard. Participants are free to train or fine-tune their models, which will be evaluated across all tasks in the leaderboard. We encourage participants to explore reinforcement fine-tuning (ReFT) techniques to enhance LLMs’ capabilities in financial tasks.

#### 🎯 Objective
Your primary goal is to fine-tune or train a model that will be added to the [Open FinLLM Leaderboard](https://huggingface.co/spaces/finosfoundation/Open-Financial-LLM-Leaderboard), evaluated across different tasks, and compete for high rankings.

You can refer to the [Open FinLLM Leaderboard Documentation](https://finllm-leaderboard.readthedocs.io/en/latest/) for information.


#### 💡 What You Need To Do

1. **Learn the Tasks on the Open FinLLM Leaderboard**  
   Participants need to learn the tasks on the Open FinLLM Leaderboard and their datasets and metircs. 

2. **Train or Fine-Tune Your LLM**  
   Train or fine-tune your own LLM for open finance.

3. **Submit Your Model**  
   Participants need to submit a Hugging Face link containing
    * the model that can be easily loaded,
    * scripts that load and inference with the model,
    * evaluation results for all tasks.

5. **Benchmarking Phase**  
   After submission, we will use our evaluation framework to evaluate your model's performance across all tasks on the leaderboard.

    We will use the script evaluate_models.ipynb provided in the folder on Google colab A100 to evaluate submitted models.
    
    Datasets used in the script can be found at [Open FinLLM Leaderboard Blog](https://huggingface.co/blog/leaderboard-finbench/) at "Click here for a short explanation of each task"

#### 📊 Metrics
The final score of the model is the average score of all tasks. The metrics are specified by the Open FinLLM Leaderboard.



