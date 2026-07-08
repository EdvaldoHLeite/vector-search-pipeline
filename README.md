# Custom Vector Search Engine & Evaluation Pipeline

A Python implementation of a Vector Search engine designed to execute semantic query matching against dense candidate vectors. This repository includes custom query vector normalization scaling, edge-case structural validation, and domain-specific conditional scoring penalties.

## 🚀 Key Features
* **Mathematical Vector Matching:** Native implementation of Cosine Similarity using algebraic dot-product calculation and magnitude normalization.
* **Dynamic Query Scaling:** Computes an adaptive scale factor based on the maximum absolute feature value of the query to prevent dimension magnitude bias.
* **Conditional Search Penalty:** Features a business-logic heuristic that applies a structural score deduction ($1/3$ factor scaling) if a candidate vector exhibits negative positioning in its first principal dimension.
* **Comprehensive Test Coverage:** Structured test cases evaluating standard vectors, orthogonal mappings, opposite alignments, and zero-vector hardware edge cases.

## ⚙️ Mathematical Mechanics
The system computes the retrieval ranking score ($S$) for a query ($q$) and a candidate vector ($c$) using:

$$S = \left( \frac{1}{\max(|q|)} \right) \cdot \text{CosineSimilarity}(q, c)$$

If $c[0] < 0$, a domain-specific penalty is applied:

$$S_{\text{final}} = \frac{S}{3.0}$$

## 📁 Repository Structure
Based on your system modules, the codebase maps as follows:
* `pipeline.py`: Mathematical operations for `search` and `cosine_similarity`.
* `score_deduction.py`: Evaluation scripts applying factor matrix operations on query arrays.
* `validation.py`: The test harness handling edge-cases, dimensional constraints, and printing final ranked array results.

## 🛠️ Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EdvaldoHLeite/vector-search-pipeline/

2. Requirements: 
* Native application execution requires Python 3.8+. 
* No external runtime dependencies required (pure mathematical standard library). 