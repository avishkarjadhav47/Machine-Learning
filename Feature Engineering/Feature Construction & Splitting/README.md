<pre>

========================================
## FEATURE CONSTRUCTION 
========================================

### Key Idea

Feature Construction is the process of manually creating new features from existing features using domain knowledge, intuition, and business understanding.

Unlike scaling, encoding, or imputation:

✔ No fixed mathematical procedure

✔ No universal rule

✔ Highly dependent on the problem and dataset

---

### Why is Feature Construction Important?

Feature Construction often has a larger impact on model performance than algorithm selection.

A better feature can improve performance even when using a simple model.

Common Goals:

* Improve predictive power
* Capture hidden relationships
* Represent information more effectively
* Increase model accuracy

---

### What Makes Feature Construction Difficult?

Feature Construction is:

* Manual
* Domain-specific
* Experience-driven

The quality of constructed features depends on:

1. Domain Knowledge
2. Data Understanding
3. Business Understanding
4. Practical Experience

As experience increases, identifying useful features becomes easier.

---

### Typical Workflow

Understand Dataset
↓
Understand Business Problem
↓
Identify Hidden Relationships
↓
Create New Features
↓
Train Model
↓
Evaluate Improvement

---

========================================
## FEATURE SPLITTING 
========================================
### Key Idea

Feature Splitting is used when a single column contains multiple pieces of information.

The goal is to separate the information into independent and meaningful features.

---

### Why Perform Feature Splitting?

A machine learning model learns better when information is represented in separate columns.

Benefits:

✔ Better interpretability

✔ Better feature representation

✔ Easier analysis

✔ Improved model learning

---

### Atomicity Principle

A good dataset should satisfy atomicity.

Atomicity means:

Each cell should contain only one piece of information.

Good:

One value per cell

Bad:

Multiple independent values in one cell

When atomicity is violated:

→ Apply Feature Splitting

---

### Common Indicators for Feature Splitting

Apply Feature Splitting when:

* A column contains multiple entities
* Text contains meaningful components
* Date-time information is combined
* Structured information is stored in a single field
* Independent information can be separated

---

### Practical Goal

Feature Construction
→ Create Information

Feature Splitting
→ Extract Information

Both aim to improve feature quality and model performance.

---
========================================
## INTERVIEW QUESTIONS
========================================
### Q. What is Feature Construction?

Creating new features from existing features using domain knowledge and business understanding to improve model performance.

---

### Q. What is Feature Splitting?

Breaking a feature into multiple meaningful features so that each feature contains a single type of information.

---

### Q. What is the difference?

Feature Construction
→ Creates new information

Feature Splitting
→ Separates existing information

---

### Q. Which is more important: Algorithm or Features?

In many practical ML projects:

Better Features > Better Algorithms

Feature engineering often contributes more to performance improvement than changing algorithms.

</pre>