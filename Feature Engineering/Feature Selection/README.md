# Important Notes on Feature Selection Methods

# 1. Filter Methods

Filter methods use statistical techniques to evaluate features independently of machine learning models.

Examples:

* Variance Threshold
* Correlation
* ANOVA
* Chi-Square
* Mutual Information

## Advantages

* Very fast
* Computationally efficient
* Works well for high-dimensional datasets
* Easy to understand and implement
* Good preprocessing step before modeling

## Disadvantages

* Ignores feature interactions
* Evaluates each feature independently
* May remove features that become useful in combination
* Usually less accurate than wrapper methods

## When to Use

* Large datasets with many features
* Initial dimensionality reduction
* Faster preprocessing pipelines
* Before wrapper or embedded methods

## When to Avoid

* When feature interactions are important
* When highest possible accuracy is required

## Important Placement Points

* Correlation removes redundant features.
* ANOVA works for numerical features + categorical target.
* Chi-Square works for categorical features.
* Mutual Information captures nonlinear relationships.
* Filter methods are model-independent.

---

# 2. Wrapper Methods

Wrapper methods select features by repeatedly training machine learning models and evaluating performance.

Examples:

* Exhaustive Feature Selection (EFS)
* Sequential Forward Selection (SFS)
* Sequential Backward Selection (SBS)
* Recursive Feature Elimination (RFE)
* RFECV

## Advantages

* Usually better feature subsets
* Considers feature interactions
* Model-aware selection
* Often improves predictive performance

## Disadvantages

* Computationally expensive
* Slow for high-dimensional data
* Repeated model training required
* Risk of overfitting on small datasets

## When to Use

* Moderate number of features
* When accuracy is very important
* When computational resources are available

## When to Avoid

* Very high-dimensional datasets
* Time-constrained environments
* Large-scale real-time systems

## Important Placement Points

### Exhaustive Feature Selection (EFS)

* Tries all possible feature combinations
* Finds globally best subset
* Extremely slow for large feature sets

### Sequential Forward Selection (SFS)

* Starts with zero features
* Adds best features step-by-step
* Faster greedy approach

### Sequential Backward Selection (SBS)

* Starts with all features
* Removes weakest features one-by-one
* Works well when many features are useful

### Recursive Feature Elimination (RFE)

* Removes weakest features recursively using model coefficients
* Popular interview topic
* Faster than exhaustive search

### RFECV

* RFE + Cross Validation
* Automatically selects optimal number of features
* One of the most practical wrapper methods

---

# 3. Embedded Methods

Embedded methods perform feature selection during model training itself.

Examples:

* L1 Regularization (Lasso)
* Tree-Based Feature Importance
* Elastic Net

## Advantages

* Faster than wrapper methods
* Scales well to large datasets
* Model-aware feature selection
* Automatic feature selection during training

## Disadvantages

* Depends heavily on model choice
* Different models may produce different feature importance
* Tree importance can be biased toward continuous variables

## When to Use

* Large datasets
* Real-world production systems
* High-dimensional problems
* When computational efficiency matters

## When to Avoid

* When model interpretability is difficult
* When model assumptions are violated

## Important Placement Points

### L1 Regularization (Lasso)

* Forces weak feature coefficients to zero
* Performs automatic feature elimination
* Smaller C → stronger regularization

### Tree-Based Feature Importance

* Uses impurity reduction to rank features
* Handles nonlinear relationships
* No feature scaling required

---

# Overall Important Interview/Placement Concepts

## 1. Data Leakage

Feature selection should generally be performed after train-test split.

Correct workflow:

* Split data
* Fit selector on training data
* Transform training and test data

---

## 2. Curse of Dimensionality

More features do not always improve model performance.
Too many irrelevant features can:

* increase noise
* increase overfitting
* slow training

---

## 3. Feature Selection vs Feature Extraction

### Feature Selection

Selects subset of existing features.
Examples:

* RFE
* ANOVA
* Lasso

### Feature Extraction

Creates new transformed features.
Examples:

* PCA
* LDA

---

## 4. No Single Best Method

Different methods often select different feature subsets because:

* optimization strategies differ
* feature interactions differ
* datasets contain redundant information

This is completely normal in practical machine learning.

---

## 5. Most Practical Methods in Industry

Most commonly used:

* Mutual Information
* RFE / RFECV
* L1 Regularization
* Tree-Based Importance

because they balance:

* accuracy
* speed
* scalability

---

## 6. Important Real-World Insight

If multiple methods repeatedly select the same features, those features are usually genuinely important predictors.

In your experiments, features like:

* Age
* Income
* InterestRate
* LoanAmount
* MonthsEmployed

appeared consistently across methods, indicating strong predictive importance for loan default prediction.
