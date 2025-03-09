## FinRL-DRR task starter kit

### 📊 Question Dataset Overview

This dataset contains question-answer pairs collected and organized for evaluating model capabilities across three domains: **CDM (Common Domain Model)**, **MOF (Model Openness Framework)**, and **XBRL (eXtensible Business Reporting Language)**.

---

#### 📁 CDM Dataset

| **Data Category**               | **Size** | **Source**             |
|-------------------------------|----------|------------------------|
| Product Model                 | 20       | CDM Documentation      |
| Event Model                   | 20       | CDM Documentation      |
| Legal Agreements              | 12       | CDM Documentation      |
| Process Model                 | 19       | CDM Documentation      |
| General and Other             | 9        | CDM Documentation      |
| Implementation & Deployment  | 46       | FAQs, FINOS CDM organizers, CDM Documentation |
| **Total**                     | **126**  |                        |

---

#### 📁 MOF Dataset

| **Data Category**            | **Size** | **Data Source**               |
|-----------------------------|----------|-------------------------------|
| License Abbreviations       | 41       | OSI Website                   |
| License OSI Approval        | 50       | OSI Website                   |
| Question Answering          | 70       | OSI Website, MOF Documentation |
| **Total**                   | **161**  |                               |

---

#### 📁 XBRL Dataset

| **Data Category**                         | **Size** | **Data Source**                                                                 |
|------------------------------------------|----------|---------------------------------------------------------------------------------|
| XBRL Term                                | 500      | XBRL International Website, XBRL Documents on the SEC Website                  |
| Domain Query to XBRL Reports             | 50       | XBRL Reports in FinanceBench (selectively provided)                            |
| Financial Math                           | 1000     | Generated via ChatGPT (formulas/code), verified by a human                     |
| Numeric Query to XBRL Reports            | 50       | XBRL Reports in FinanceBench (selectively provided)                            |
| XBRL Tag Query to XBRL Reports           | 50       | XBRL Reports of Companies in Dow Jones 30 from the SEC                         |
| Financial Ratio Formula with XBRL Tags   | 50       | XBRL Reports of Companies in Dow Jones 30 from the SEC                         |
| **Total**                                | **1700** |                                                                                 |

---

#### 📦 Dataset Summary

| **Domain** | **Total QA Pairs** |
|------------|--------------------|
| CDM        | 126                |
| MOF        | 161                |
| XBRL       | 1700               |
