# TokenSHAP-Extensions: Structured Prompt Explainability for Biomedical QA

> **Note:**  
> This repository is a research fork of the original [TokenSHAP](https://github.com/ronigold/TokenSHAP) project by **Roni Goldshmidt** and **Miriam Horovicz**.  
> All original source files under `token_shap/` remain **unmodified**.  
> This fork adds new modules under `token_shap_extensions/` that extend TokenSHAP for **structured question-answering (QA)** and **biomedical interpretability research**, developed as part of the **Advanced XAI Toolkit** project at *San José State University* for the course *DATA298*.

## Overview
TokenSHAP and PixelSHAP introduced Monte Carlo Shapley value estimation for interpretability of large language and vision-language models.  
This fork builds on those foundations to make TokenSHAP more effective for **structured prompts**—such as multiple-choice or yes/no questions—where part of the text (e.g., “Answer Choices”) must remain fixed.

### New in this fork
- **`QATokenSHAP`** – subclass of `TokenSHAP` that perturbs only the *question* portion of structured prompts while keeping suffixes constant.  
- **Flexible extractor API** – pass a custom `section_extractor(prompt: str) → (question_text, static_suffix)` to support diverse prompt templates.  
- **Correctness-aware value functions** *(in progress)* – evaluate token contributions based on model answer correctness when ground truth labels are available.  
- **Embedding-based similarity** *(planned)* – replace TF-IDF similarity with semantic embedding similarity for improved faithfulness.


---

## Repository Structure
```python
TokenSHAP/
├── token_shap/ # Original TokenSHAP source (untouched)
├── token_shap_extensions/ # New research extensions
│   ├── init.py
│   ├── qa_token_shap.py # QATokenSHAP subclass implementation
│   ├── extractors.py # Default and custom prompt extractors
│   └── value_functions/ # Experimental correctness/semantic modules
└── notebooks/
    ├── QA_TokenSHAP_Examples.ipynb # Not implemented yet
    └── (original TokenSHAP notebooks)
```
