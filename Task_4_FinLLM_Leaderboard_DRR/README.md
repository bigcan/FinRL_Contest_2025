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

This dataset contains question-answer pairs collected and organized for evaluating model capabilities across **CDM**, **MOF**, and **XBRL**.

#### 📁 CDM Dataset

| **Data Category**               | **Size** | **Source**                                                                 |
|-------------------------------|----------|--------------------------------------------------------------------------|
| Product Model                 | 20       | [CDM Documentation](https://cdm.finos.org/)                              |
| Event Model                   | 20       | [CDM Documentation](https://cdm.finos.org/)                              |
| Legal Agreements              | 12       | [CDM Documentation](https://cdm.finos.org/)                              |
| Process Model                 | 19       | [CDM Documentation](https://cdm.finos.org/)                              |
| General and Other             | 9        | [CDM Documentation](https://cdm.finos.org/)                              |
| Implementation & Deployment  | 46       | [FAQs](https://www.finos.org/faq), FINOS CDM organizers, [CDM Documentation](https://cdm.finos.org/) |
| **Total**                     | **126**  |                                                                          |

#### 📁 MOF Dataset

| **Data Category**            | **Size** | **Data Source**                                                                 |
|-----------------------------|----------|---------------------------------------------------------------------------------|
| License Abbreviations       | 41       | [OSI Website](https://opensource.org/licenses)                                 |
| License OSI Approval        | 50       | [OSI Website](https://opensource.org/licenses)                                 |
| Question Answering          | 70       | [OSI Website](https://opensource.org/licenses), [MOF Documentation](https://arxiv.org/abs/2403.13784) |
| **Total**                   | **161**  |                                                                                 |

#### 📁 XBRL Dataset

| **Data Category**                         | **Size** | **Data Source**                                                                 |
|------------------------------------------|----------|---------------------------------------------------------------------------------|
| XBRL Term                                | 500      | [XBRL International Glossary](https://www.xbrl.org/guidance/xbrl-glossary/), [SEC XBRL Glossary](https://www.sec.gov/data-research/osd_xbrlglossary) |
| Domain Query to XBRL Reports             | 50       | [FinanceBench Dataset](https://arxiv.org/abs/2311.11944) (selectively provided)|
| Financial Math                           | 90     | Generated via ChatGPT (formulas/code), verified by a human                     |
| Numeric Query to XBRL Reports            | 50       | [FinanceBench Dataset](https://arxiv.org/abs/2311.11944) (selectively provided)|
| XBRL Tag Query to XBRL Reports           | 50       | [SEC Website](https://www.sec.gov/) (Dow Jones 30 Companies Reports)           |
| Financial Ratio Formula with XBRL Tags   | 50       | [SEC Website](https://www.sec.gov/) (Dow Jones 30 Companies Reports)           |
| **Total**                                | **790** |                                                                                 |

---

#### 📦 Dataset Summary

| **Domain** | **Total QA Pairs** |
|------------|--------------------|
| CDM        | 126                |
| MOF        | 161                |
| XBRL       | 790               |

#### 📘 Note for Participants

Participants are encouraged to use the above sources as a starting point to construct their own training datasets. Your model's performance will strongly depend on the quality and comprehensiveness of your self-collected training data. These sources can help you build a rich and task-aligned dataset for model training, ensuring better performance on regulatory reasoning and question answering.


