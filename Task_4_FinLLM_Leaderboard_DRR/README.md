## FinRL-DRR task starter kit

### 📊 Question Dataset Overview

This dataset contains question-answer pairs collected and organized for evaluating model capabilities across three domains: **CDM (Common Domain Model)**, **MOF (Model Openness Framework)**, and **XBRL (eXtensible Business Reporting Language)**.

---

#### 📁 CDM Dataset

| **Data Category**              | **Size** | **Source**                        |
|-------------------------------|----------|-----------------------------------|
| Product Model                 | 20       |                                   |
| Event Model                   | 20       |                                   |
| Legal Agreements              | 12       |                                   |
| Process Model                 | 19       |                                   |
| General and Other             | 9        | [CDM Documentation](https://cdm.finos.org/) |
| Implementation & Deployment  | 46       | [FAQs](https://www.finos.org/faq), FINOS CDM organizers, [CDM Documentation](https://cdm.finos.org/) |
| **Total**                    | **126**   |                                   |


---

#### 📁 MOF Dataset

| **Data Category**            | **Size** | **Data Source**               |
|-----------------------------|----------|-------------------------------|
| License Abbreviations       | 41       | OSI Website  https://opensource.org/licenses                 |
| License OSI Approval        | 50       | OSI Website https://opensource.org/licenses                  |
| Question Answering          | 70       | OSI Website https://opensource.org/licenses, MOF Documentation https://arxiv.org/abs/2403.13784 |
| **Total**                   | **161**  |                               |

---

#### 📁 XBRL Dataset

| **Data Category**                         | **Size** | **Data Source**                                                                 |
|------------------------------------------|----------|---------------------------------------------------------------------------------|
| XBRL Term                                | 500      | XBRL International Website https://www.xbrl.org/guidance/xbrl-glossary/, XBRL Documents on the SEC Website https://www.sec.gov/data-research/osd_xbrlglossary                  |
| Domain Query to XBRL Reports             | 50       | XBRL Reports in FinanceBench (selectively provided) https://arxiv.org/abs/2311.11944                            |
| Financial Math                           | 1000     | Generated via ChatGPT (formulas/code), verified by a human                     |
| Numeric Query to XBRL Reports            | 50       | XBRL Reports in FinanceBench (selectively provided) https://arxiv.org/abs/2311.11944                            |
| XBRL Tag Query to XBRL Reports           | 50       | XBRL Reports of Companies in Dow Jones 30 from the SEC https://www.sec.gov/                        |
| Financial Ratio Formula with XBRL Tags   | 50       | XBRL Reports of Companies in Dow Jones 30 from the SEC  https://www.sec.gov/                       |
| **Total**                                | **1700** |                                                                                 |

---

#### 📦 Dataset Summary

| **Domain** | **Total QA Pairs** |
|------------|--------------------|
| CDM        | 126                |
| MOF        | 161                |
| XBRL       | 1700               |
