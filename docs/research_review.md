# Research Review — CareBot Healthcare AI

**Project:** CareBot Healthcare AI  
**Milestone:** Week 1 — Research and Architecture Design

## Introduction

The purpose of this research review is to study existing research papers and a clinical Natural Language Processing (NLP) library relevant to healthcare AI.

The review focuses on three areas:

1. Clinical note summarisation using Large Language Models (LLMs).
2. Verifiable summarisation of Electronic Health Records (EHRs).
3. Clinical text processing using MedSpaCy.

These references help identify suitable approaches, important challenges and possible technologies for the CareBot Healthcare AI project.

---

## 1. Research Paper: Development and Evaluation of a Clinical Note Summarization System Using Large Language Models

**Authors:** Juliana Damasio Oliveira et al.  
**Published:** 2025  
**Journal:** Communications Medicine  
**DOI:** https://doi.org/10.1038/s43856-025-01091-3

### 1.1 Objective

The paper focuses on developing an AI-based system that helps physicians prepare hospital discharge summaries.

Clinical notes contain important information about a patient's medical history, diagnosis, treatments, laboratory results and discharge plans. However, these notes can be lengthy and complex, making it difficult for physicians to identify and summarise the most important information efficiently.

The study explores how Large Language Models can assist with generating clear and organised discharge summaries.

### 1.2 Methodology and Approach

The researchers developed a discharge summary system integrated with NoHarm.ai.

Their approach combines Named Entity Recognition (NER) and Large Language Models.

The main steps include:

1. Identifying important information from clinical notes using NER models such as Flair.
2. Extracting information such as admission reasons, test results, drug allergies, medical conditions and discharge plans.
3. Organising the extracted information into predefined summary sections.
4. Using an LLM to generate a structured and readable discharge summary.
5. Allowing physicians to review, edit and validate the generated summary.

The system also uses structured data, such as laboratory results and medication information, by converting it into natural language.

The discharge summary includes sections such as diagnosis, allergies, home medications, clinical summary, laboratory tests, procedures, discharge conditions and discharge plans.

### 1.3 Evaluation and Findings

The researchers collected feedback through:

- An online survey involving 128 respondents.
- Interviews with 10 primary care physicians.
- Physician evaluations of AI-generated discharge summaries.

The study reported that physician evaluations were generally positive, with most generated summaries receiving ratings of Very Good or Excellent.

The paper also discusses an earlier evaluation comparing six LLMs with human assessments using the F1-score.

The findings suggest that combining NER with LLMs can help generate organised clinical summaries and reduce the amount of text that the LLM needs to process.

### 1.4 Limitations and Challenges

The paper identifies several challenges:

- LLMs can generate incorrect or unsupported information.
- Important clinical details may be omitted.
- Generated summaries require careful validation.
- The evaluation was predominantly qualitative.
- The amount of training and testing data was limited.
- Large-scale adoption had not yet been evaluated.

The researchers recommend further quantitative evaluation, independent validation and testing with a wider range of clinical cases.

### 1.5 Relevance to CareBot

This research is relevant because the CareBot project brief describes extracting important medical information and generating healthcare summaries.

The combination of NER and LLMs provides a useful reference for designing a system that extracts relevant clinical information before generating a summary.

It also highlights the importance of human review and responsible AI in healthcare applications.

---

## 2. Research Paper: Verifiable Summarization of Electronic Health Records Using Large Language Models to Support Chart Review

**Authors:** Ritchie Verma, Emily Alsentzer et al.  
**Published:** June 2025  
**Source:** medRxiv preprint  
**DOI:** https://doi.org/10.1101/2025.06.02.25328807

**Publication note:** This is a preprint and was not certified by peer review at the version provided.

### 2.1 Objective

The paper investigates how Large Language Models can help physicians review large Electronic Health Records (EHRs).

Patient records can contain hundreds or thousands of clinical notes. Reviewing all this information can be time-consuming and increases the cognitive workload of healthcare professionals.

The researchers developed a system to generate problem-based summaries of longitudinal medical records, focusing specifically on patients with heart failure.

### 2.2 Methodology and Approach

The researchers introduced an approach called **Extract-Then-Abstract**.

It consists of two main stages:

**Stage 1 — Information extraction**

The system uses predefined, disease-specific summary bundles to identify important clinical information from patient records.

For heart failure, these bundles include:

- Type of heart failure.
- Type of cardiomyopathy.
- History of arrhythmias.
- History of valve disease.
- Cardiac procedures.
- Laboratory results and vital information.
- Medications.
- Disease progression and care plans.

The extracted information is organised into a structured format.

**Stage 2 — Information summarisation**

An LLM uses the extracted information to generate a readable, structured summary.

The system also attaches references to the original clinical notes, including note identifiers, note types and encounter dates.

This allows physicians to verify the information in the generated summary against its original source.

### 2.3 Evaluation and Findings

The researchers evaluated the summaries with eight physicians using eight heart failure patient cases.

The study compared two conditions:

- Standard chart review using the EHR alone.
- Chart review using the EHR together with an LLM-generated summary.

The evaluation measured completion time and accuracy when answering patient-specific clinical questions.

The reported results were:

| Evaluation | EHR alone | Summary + EHR |
|---|---:|---:|
| Average completion time | 10.30 minutes | 9.45 minutes |
| Accuracy | 88.1% | 86.7% |

Access to summaries did not significantly reduce overall completion time or significantly change accuracy.

However, more frequent use of the summaries was associated with faster questionnaire completion.

All participating physicians indicated that they were likely or very likely to use the summaries in clinical practice, and 87.5% reported that the summaries could save them time.

### 2.4 Limitations and Challenges

The paper identifies several limitations:

- The evaluation involved only eight physicians.
- The study focused specifically on heart failure patients.
- The impact of summaries varied between physicians.
- Some summaries contained missing or inaccurate information.
- Some physicians found the summary organisation difficult to follow.
- Clinical summaries must be verifiable against their original sources.

The authors emphasise that summaries should support clinical reasoning rather than replace it.

### 2.5 Relevance to CareBot

This paper provides an important design idea for CareBot: extract relevant information first and generate a summary from the extracted information.

The source references attached to generated information are particularly useful because they improve transparency and allow users to verify the results.

The paper also shows that evaluation should consider not only summary quality but also accuracy, usability and the ability to verify information.

---

## 3. GitHub Repository: MedSpaCy

**Repository:** https://github.com/medspacy/medspacy  
**Technology:** Python and spaCy  
**Purpose:** Library for clinical Natural Language Processing (NLP).

### 3.1 Overview

MedSpaCy is a Python library designed for processing clinical text using the spaCy NLP framework.

It provides reusable components for clinical text processing and can be used as part of a clinical NLP pipeline.

The repository describes MedSpaCy as a modular library containing components for clinical sentence splitting, section detection, contextual analysis and clinical concept processing.

### 3.2 Important Features

The repository describes several useful components:

**1. Clinical sentence segmentation**

Identifies sentence boundaries in clinical documents.

**2. Section detection**

Identifies sections within clinical notes, helping organise information according to its context.

**3. Context and ConText processing**

Identifies contextual information, including negation and uncertainty.

For example:

- "Patient has pneumonia."
- "No evidence of pneumonia."

These statements contain the same medical concept but have different meanings. Contextual analysis helps identify this difference.

**4. Clinical concept extraction**

Helps identify medical concepts and relevant information from clinical text.

**5. QuickUMLS integration**

Provides an option for identifying clinical concepts using QuickUMLS.

### 3.3 Installation and Usage

The repository provides installation instructions using pip.

Example:

```bash
pip install medspacy
```

It also demonstrates how MedSpaCy can be imported and used with a spaCy-based NLP pipeline.

The repository includes examples and additional resources for implementing clinical text processing.

### 3.4 Relevance to CareBot

MedSpaCy is relevant to the CareBot project because the project brief involves extracting useful information from healthcare text.

Its sentence segmentation, section detection and contextual analysis features could help prepare clinical text before information extraction and summarisation.

In particular, recognising negation and uncertainty is important in healthcare because the presence or absence of a medical condition should not be interpreted incorrectly.

MedSpaCy can therefore be considered as a possible tool for the clinical NLP component of CareBot.

---

## 4. Overall Research Findings

The three references provide useful ideas for designing a healthcare AI system.

The main findings are:

1. **NER and LLM combination:** The first paper demonstrates how extracting important information before generating a summary can help organise clinical documentation.

2. **Extract-Then-Abstract approach:** The second paper demonstrates a structured summarisation approach in which important information is extracted first and then converted into a readable summary.

3. **Clinical text processing:** MedSpaCy provides reusable NLP components for processing clinical text, identifying sections and understanding contextual information such as negation.

4. **Evaluation and reliability:** Healthcare AI systems need careful evaluation of accuracy, completeness, usability and factual reliability.

5. **Human oversight:** AI-generated healthcare information should be reviewed and validated by qualified healthcare professionals.

## 5. Application to the CareBot Project

Based on the research, the following initial technical direction is proposed for CareBot:

- Prepare and preprocess healthcare data.
- Identify relevant symptoms, medical concepts and other information.
- Organise extracted information into a structured format.
- Explore suitable machine-learning or NLP methods for the available project datasets.
- Generate understandable outputs.
- Evaluate the outputs using supplied test cases and suitable evaluation metrics.

The research also highlights a difference between the project brief and the supplied datasets.

The project brief describes clinical-note summarisation, while the supplied CSV and labelled JSON datasets primarily support symptom-related classification and chatbot intent recognition.

Therefore, the final architecture and implementation scope should be confirmed against the mentor's requirements.

## 6. Conclusion

The reviewed research papers and MedSpaCy repository provide a foundation for understanding clinical text processing, healthcare summarisation and the evaluation of AI systems.

The most useful ideas for CareBot are the combination of information extraction and summarisation, structured clinical information processing, source-based verification and careful evaluation.

These findings will guide the proposed model architecture and the development of the initial data pipeline in the following project milestones.

---

**References**

1. Oliveira, J. D. et al. (2025). *Development and evaluation of a clinical note summarization system using large language models*. Communications Medicine. https://doi.org/10.1038/s43856-025-01091-3

2. Verma, R. et al. (2025). *Verifiable Summarization of Electronic Health Records Using Large Language Models to Support Chart Review*. medRxiv preprint. https://doi.org/10.1101/2025.06.02.25328807

3. MedSpaCy Contributors. *MedSpaCy: Library for clinical NLP with spaCy*. GitHub repository. https://github.com/medspacy/medspacy