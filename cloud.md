# TokenSHAP-Extensions: Structured Prompt Explainability Toolkit

### Project Overview
TokenSHAP-Extensions is a research-driven enhancement of the original [TokenSHAP](https://github.com/ronigold/TokenSHAP) framework, designed to make explainability methods more effective for **structured question-answering (QA)** and **biomedical reasoning** tasks.  
While the original TokenSHAP provides token-level interpretability for general text generation, this extension adapts it to handle **prompts with fixed sections** that should not be perturbed during Shapley value estimation.

This work is part of the **Advanced XAI Toolkit** project at *San José State University* for the course *DATA298*, focused on evaluating and improving explainability techniques for biomedical large language models (LLMs).

---

### Motivation
Standard XAI methods like SHAP or LIME are designed for unstructured text inputs.  
However, **QA datasets** often contain structured prompts with fixed sections, leading to unreliable attributions when those segments are randomly perturbed.  
Our goal is to extend TokenSHAP to:

1. Perturb only the **question** portion of structured QA prompts.  
2. Integrate **correctness-aware and semantic value functions** to make token importance more faithful to model reasoning.  
3. Enable domain-specific interpretability evaluation across biomedical LLMs.

---

### Core Features
- **QATokenSHAP** – Subclass of TokenSHAP that performs Monte Carlo sampling only on the question part of a structured prompt.
- **Flexible Section Extractors** – Functions that automatically separate variable (question) and fixed (suffix) parts of a prompt.
- **Correctness-Aware Value Function (planned)** – Computes explanation faithfulness based on model answer correctness.
- **Embedding-Based Value Function (planned)** – Uses semantic similarity from biomedical embeddings for improved interpretability.

---

### Architecture Overview
``` python
TokenSHAP/
├── qa_tokenshap.py # QATokenSHAP class implementation
├── extractors.py # Default QA prompt extractor functions
└── value_functions/
    └── correctness_aware.py # Placeholder for correctness-based value function
```
### Team & Acknowledgments

**Team 8 – Advanced XAI Toolkit**
Jeff Chong • Anne Ha • Jiyoon Lee • Matthew Leffler • Nairui Liu
Faculty Advisor: Prof. Simon Shim, Department of Applied Data Science, SJSU

This project builds upon the open-source [TokenSHAP](https://github.com/ronigold/TokenSHAP) library by **Roni Goldshmidt** and **Miriam Horovicz**.
All original source files under `token_shap/` remain **unmodified**. 