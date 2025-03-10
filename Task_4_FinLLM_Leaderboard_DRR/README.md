## FinRL-DRR task starter kit

### 📊 Question Dataset Overview

This dataset contains question-answer pairs collected and organized for evaluating model capabilities across three domains: **CDM (Common Domain Model)**, **MOF (Model Openness Framework)**, and **XBRL (eXtensible Business Reporting Language)**.

---

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

---

#### 📁 MOF Dataset

| **Data Category**            | **Size** | **Data Source**                                                                 |
|-----------------------------|----------|---------------------------------------------------------------------------------|
| License Abbreviations       | 41       | [OSI Website](https://opensource.org/licenses)                                 |
| License OSI Approval        | 50       | [OSI Website](https://opensource.org/licenses)                                 |
| Question Answering          | 70       | [OSI Website](https://opensource.org/licenses), [MOF Documentation](https://arxiv.org/abs/2403.13784) |
| **Total**                   | **161**  |                                                                                 |

---

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

---

