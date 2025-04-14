## FinRL-DRR task starter kit

### 🧠 Task Overview

This task is designed to test the capabilities of large language models (LLMs) to generate accurate and context-aware responses related to regulatory and financial texts across three domains: **CDM (Common Domain Model)**, **MOF (Model Openness Framework)**, and **XBRL (eXtensible Business Reporting Language)**.

#### 🎯 Objective
Your primary goal is to fine-tune or train a model that can accurately interpret and respond to a variety of domain-specific questions. These questions span structured domains like financial product modeling, regulatory compliance, licensing standards, and financial reporting.

#### 💡 What You Need To Do

1. **Collect and Prepare Your Raw Training Data**  
   Participants need to collect raw data given the source provided below. 

2. **Train or Fine-Tune Your LLM**  
   Use your collected data to fine-tune your own LLM or adapt an existing model for regulatory question answering.

3. **Submit Your Model**  
   Submit your trained model following the competition guidelines. Make sure your model is:
   - Capable of answering complex domain-specific questions.
   - Robust in interpreting structured data and reasoning over it.

4. **Benchmarking Phase**  
   After submission, we will use our standardized question sets to evaluate your model's performance on real-world regulatory QA tasks.

---

### 📊 Question Dataset Overview

This dataset contains question-answer pairs collected and organized for evaluating model capabilities across **CDM**, **MOF**, and **XBRL**. You can refer to the [Financial Regulations Documentation](https://financial-regulations.readthedocs.io/en/latest/) for more detailed descriptions.

#### 📁 CDM Dataset

| **Data Category**               | **Size** | **Metrics**     | **Source**                                                                 |
|-------------------------------|----------|----------------|--------------------------------------------------------------------------|
| Product Model                 | 20       | FActScore    | [CDM Documentation](https://cdm.finos.org/)                              |
| Event Model                   | 20       | FActScore   | [CDM Documentation](https://cdm.finos.org/)                              |
| Legal Agreements              | 12       | FActScore      | [CDM Documentation](https://cdm.finos.org/)                              |
| Process Model                 | 19       | FActScore    | [CDM Documentation](https://cdm.finos.org/)                              |
| General and Other             | 9        | FActScore   | [CDM Documentation](https://cdm.finos.org/)                              |
| Implementation & Deployment  | 42       | FActScore    | [FAQs](https://www.finos.org/faq), FINOS CDM organizers, [CDM Documentation](https://cdm.finos.org/) |
| **Total**                     | **122**  |                |                                                                          |

#### 📁 MOF Dataset

| **Data Category**            | **Size** | **Metrics**     | **Data Source**                                                                 |
|-----------------------------|----------|----------------|---------------------------------------------------------------------------------|
| License Abbreviations       | 31       | Accuracy   | [OSI Website](https://opensource.org/licenses)                                 |
| License OSI Approval        | 50       | Accuracy       | [OSI Website](https://opensource.org/licenses)                                 |
| Question Answering          | 59       | FActScore      | [OSI Website](https://opensource.org/licenses), [MOF Documentation](https://arxiv.org/abs/2403.13784) |
| **Total**                   | **140**  |                |                                                                                 |

#### 📁 XBRL Dataset

| **Data Category**                         | **Size** | **Metrics**     | **Data Source**                                                                 |
|------------------------------------------|----------|----------------|---------------------------------------------------------------------------------|
| XBRL Term                                | 391      | FActScore      | [XBRL Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495)                     |
| Domain Query to XBRL Reports             | 40       | FActScore      | [XBRL Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495) |
| Financial Math                           | 90       | Accuracy       | [XBRL Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495)                     |
| Numeric Query to XBRL Reports            | 50       | FActScore      | [XBRL Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495) |
| XBRL Tag Query to XBRL Reports           | 90       | Accuracy       | [XBRL filings from SEC Website](https://www.sec.gov/)           |                                                                            |
| FiNER: Financial Numeric Entity Recognition for XBRL Tagging           | 100  |     Selectively provided | FiNER-139 Dataset: https://huggingface.co/datasets/nlpaueb/finer-139, https://github.com/nlpaueb/finer |
| FNXL: Financial Numeric Extreme Labelling              | 100 |       Selectively provided   | FNXL Dataset: https://huggingface.co/datasets/ChanceFocus/flare-fnxl, https://arxiv.org/abs/2306.03723 |
| **Total**                                | **861** |                |                                                                                 |

##### 📂 How to Download XBRL Filings

To construct or extend your training dataset with real-world XBRL filings, participants may utilize the following data sources:

##### 📥 1. Company-Level Financial Statements

You can manually retrieve XBRL filings for individual companies via the U.S. Securities and Exchange Commission (SEC):

1. Visit the [SEC EDGAR Company Search](https://www.sec.gov/edgar/searchedgar/companysearch).
2. Search by company name or ticker symbol.
3. Filter by filing types such as 10-K, 10-Q, etc.
4. Click on a specific filing.
5. Look for files with extensions like:
   - `.xml`
   - `.xsd`
   - `.xbrl`
   - or links labeled "Interactive Data".
6. Download the corresponding XBRL instance and taxonomy files.

> 💡 This method is ideal for collecting filings from specific companies or filing types in a controlled manner.

##### ⚙️ 2. XBRL Terminology & Standards

As a starting point, you may also use the provided web crawling script to automate the retrieval of XBRL-related documents from the [XBRL International Glossary](https://www.xbrl.org/guidance/xbrl-glossary/). This source provides standardized definitions and explanations of XBRL terms. These documents help the model better understand the semantics and structure of XBRL as a framework.

- 📎 Provided Code: [xbrl_webcrawl.ipynb](./xbrl_webcrawl.ipynb)

This script offers a basic template to:
- Scrape and parse glossary terms.
- Crawl linked resources or downloadable attachments related to XBRL filings.
- Extend it further for large-scale automated crawling from additional sources (e.g., SEC bulk data feeds, company repositories, etc.).

> 💡 This data helps build XBRL term comprehension tasks, enabling models to understand and explain technical terms used in filings. Participants are encouraged to adapt and extend the script to suit their own dataset construction needs.

Note: We will additionally test on a subset of the FiNER-139 and FNXL datasets. Please use the batched versions provided in this folder for fine-tuning to avoid overfitting. To test, please use the code from https://github.com/Open-Finance-Lab/FinLoRA/blob/main/test/xbrl.py.

---

#### 📦 Dataset Summary

| **Domain** | **Total QA Pairs** |
|------------|--------------------|
| CDM        | 122                |
| MOF        | 140                |
| XBRL       | 861               |

### 📊 Metrics
The model evaluation is the average score of all tasks. 

#### 📘 Note for Participants

Participants are encouraged to use the above sources as a starting point to construct their own training datasets. Your model's performance will strongly depend on the quality and comprehensiveness of your self-collected training data. These sources can help you build a rich and task-aligned dataset for model training, ensuring better performance on regulatory reasoning and question answering.

To ensure fair comparison and practical deployment, it is recommended that the model size should not exceed 8B parameters.

