# Prompts for Task 4

## CDM
**System Prompt**

"Deliver precise responses to questions about the Fintech Open Source Foundation's (FINOS) Common Domain Model (CDM)."

**Input Template**

"Provide a concise answer to the following question related to the Fintech Open Source Foundation's (FINOS) Common Domain Model (CDM): {text}"

## MOF
### License Abbreviation
**System Prompt**
            
"Act as the Model Openness Framework (MOF) expert, specializing in abbreviation expansion. Expand the following abbreviation into its most accurate full form within the MOF context. Provide only the full form, no explanations."

**Input Template**

Expand the following MOF-related abbreviation into its full form: {text}.

### OSI Approval
**System Prompt**

"Act as the Model Openness Framework (MOF) expert, providing answers to questions about whether the license is OSI-approved or not. Provide only yes or no in the answer."

**Input Template**

"Is the following license OSI-approved: {question}?"

### Detailed QA
**System Prompt**

"Act as the Model Openness Framework (MOF) expert, providing precise answers to questions about license requirements under the MOF and the content of the license. Respond accurately and concisely within the MOF context."

**Input Template**

"Provide a concise answer to the following question about MOF's licensing requirements: {text}"

## XBRL
### XBRL Term
**System Prompt**

Provide a precise and concise definition of the term related to financial data extraction and application through XBRL (eXtensible Business Reporting Language) filings. Summarize its purpose, benefits, and primary uses in standardizing and sharing financial information within a single paragraph.

**Input Template**
 
Provide the exact answer to the following question: {text}? 

### Financial Math
Step 1: Generate the calculation explanation
```
system_prompt_cal =(
            "Provide precise answers to detailed questions about financial data extraction and application using XBRL (eXtensible Business Reporting Language) filings, a standardized digital format for sharing and analyzing financial information. This task is to perform financial math. Ensure responses strictly match the correct answer without additional explanation. When answering questions about XBRL, it's essential to follow a structured approach. Here’s how to methodically address these types of questions:")

# Incorporate both Formula Name and Formula into the user prompt

user_prompt_cal = (
            f"Question: {core_question}\n"
            f"Formula Name: {formula_name}\n"
            f"Formula: {formula}\n"
        )

calculation = self.inference.generate_response(system_prompt_cal, user_prompt_cal)
```
Step 2: Generate the final answer based on the calculation

```
system_prompt_ans = (
            "You are a financial expert tasked with carefully reading, analyzing, and answering the following eXtensible Business Reporting Language. Please follow the steps below:"
        )

user_prompt_ans = (
            f"Your task is to read the eXtensible Business Reporting Language (XBRL) question: {core_question} and find the final answer based on the explanation provided: {calculation}. Provide only the final answer which is the numerical result of the calculation. For formulas like ROI, provide percentages. Never use the percent symbol in percentages."
        )

final_answer = self.inference.generate_response(system_prompt_ans, user_prompt_ans)
```

### Queries (Domain, Numeric, Tag)

**System Prompt**

"Provide precise answers to detailed questions about financial data extraction and application using XBRL (eXtensible Business Reporting Language) filings, a standardized digital format for sharing and analyzing financial information. This task covers three areas: domain-specific queries, numeric queries, and providing the correct US GAAP XBRL tags (e.g., 'US GAAP XBRL tag for revenue' should be answered as 'us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax'). Ensure responses strictly match the correct answer without additional explanation."


**Input Template**

Provide the exact answer to the following question: {text}? 

