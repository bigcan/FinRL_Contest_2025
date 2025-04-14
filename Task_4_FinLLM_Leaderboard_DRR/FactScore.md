---

# 🔍 FActScore Evaluation Pipeline 

This repository provides clear instructions for running **FActScore** with a customized evaluation setup. All necessary files and Colab scripts are provided — **no additional coding is required**.

---

## 📦 What We Provide

You will receive the following files from the organizers:

- `demos.zip`: A curated test dataset  
- `openai_lm.py`: A custom model interface (to replace the original one)  
- `knowledge_base.jsonl`: A knowledge base precisely aligned with the test questions  

---

## 🚀 Evaluation Workflow (Colab Recommended)

Please follow these steps **exactly** to ensure your evaluation is consistent and valid:

### ✅ Step 1. Clone the Official FActScore Repository

You’ll start by cloning the [FActScore GitHub repository](https://github.com/shmsw25/FActScore).
The code is provided [here](https://github.com/Open-Finance-Lab/FinRL_Contest_2025/blob/main/Task_4_FinLLM_Leaderboard_DRR/FinRL_FactScore.ipynb)

### 🔁 Step 2. Replace `openai_lm.py`

Upload the provided `openai_lm.py` file and **replace** the one in the cloned repository. This file ensures compatibility with the evaluation script and your model interface.

### 📦 Step 3. Upload and Unzip `demos.zip`

Upload the provided `demos.zip`, which contains the test questions. It must remain unchanged and will be unzipped for evaluation.

### 📚 Step 4. Upload `knowledge_base.jsonl`

This file was built specifically for the released testing dataset.  
> **Important:** The questions in this knowledge base exactly match those in `demos.zip`. Your model answers must align perfectly in order to receive valid scores.

### 🧪 Step 5. Run the Evaluation

Use the provided Colab notebook to run the full FActScore evaluation pipeline. You’ll simply upload your model's answers and the script will handle everything else.

---

## ⚠️ Key Guidelines

- Do **not** modify the provided `demos.zip`, `openai_lm.py`, or `knowledge_base.jsonl`.
- Do **not** change question wording in your model predictions — **exact match is required**.
- Do **not** substitute your own code — all code is already provided via Colab.

---

