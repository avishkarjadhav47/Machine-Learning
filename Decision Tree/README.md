<pre>
==============
DECISION TREE
===============

1. WHAT IS DECISION TREE?
-------------------------
- Supervised ML Algorithm.
- Works for Classification & Regression.
- Learns IF-ELSE rules recursively.
- sklearn uses CART internally.
- All sklearn trees are Binary Trees.

Decision Tree
│
├── Classification Tree
│   └── Predicts Class
│
└── Regression Tree
    └── Predicts Numerical Value

--------------------------------------------------

2. DECISION TREE ALGORITHMS

| Algorithm / Implementation            | Used For       | Split Criterion Options                                    | Children     |
| ------------------------------------- | -------------- | ---------------------------------------------------------- | ------------ |
| ID3                                   | Classification | Information Gain (Entropy-based)                           | Multi-branch |
| C4.5                                  | Classification | Gain Ratio (Entropy-based)                                 | Multi-branch |
| CART (Traditional Theory)             | Classification | Gini Impurity                                              | Binary       |
| CART (Traditional Theory)             | Regression     | Variance Reduction / MSE                                   | Binary       |
| CART in scikit-learn (Classification) | Classification | Gini Impurity / Entropy / Log Loss                         | Binary       |
| CART in scikit-learn (Regression)     | Regression     | Squared Error (MSE), Friedman MSE, Absolute Error, Poisson | Binary       |

sklearn Classification:
- gini
- entropy
- log_loss

sklearn Regression:
- squared_error
- friedman_mse
- absolute_error
- poisson

--------------------------------------------------

3. ENTROPY

Measures Uncertainty.

Entropy = -Σ(pi log2(pi))

Properties:
- Pure Node → Entropy = 0
- Mixed Node → Higher Entropy

--------------------------------------------------

4. INFORMATION GAIN (ID3)

Information Gain =
Entropy(Parent)
-
Weighted Entropy(Children)

Choose Feature:
→ Maximum Information Gain

--------------------------------------------------

5. GAIN RATIO (C4.5)

Gain Ratio =
Information Gain
/
Split Information

Choose Feature:
→ Maximum Gain Ratio

--------------------------------------------------

6. GINI IMPURITY (CART)

Gini = 1 - Σ(pi²)

Interpretation:
- Probability of incorrect classification.
- Measures how mixed a node is.

Properties:
- Pure Node → Gini = 0
- 50%-50% Binary Node → Gini = 0.5 (Maximum)

Weighted Gini =
(NL/N)*GiniL
+
(NR/N)*GiniR

Choose Split:
→ Minimum Weighted Gini

Interview Line:
"Gini Impurity measures probability of incorrect classification."

--------------------------------------------------

7. CLASSIFICATION TREE

Goal:
→ Create Pure Nodes

Steps:
1. Calculate Impurity
2. Try All Splits
3. Compute Weighted Child Impurity
4. Choose Best Split
5. Repeat Recursively

Leaf Prediction:
→ Majority Class

--------------------------------------------------

8. REGRESSION TREE

Goal:
→ Reduce MSE / Variance

MSE =
(1/n)Σ(yi - ŷ)²

Variance =
Σ(xi - x̄)² / n

Leaf Prediction =
Mean Target Value

Prediction =
Σyi / n

Interview Line:
"Decision Tree Regressor predicts average value in leaf node."

--------------------------------------------------

9. FEATURE IMPORTANCE

Definition:
- Measures usefulness of feature.

Node Importance =
Parent Impurity
-
Weighted Child Impurity

Feature Importance =
Σ(Node Importance from Feature)
/
Σ(All Node Importances)

Classification:
→ Gini/Entropy Reduction

Regression:
→ MSE/Variance Reduction

sklearn:
model.feature_importances_

Important:
Feature Importance ≠ Causation

--------------------------------------------------

10. OVERFITTING

Why?
- Tree keeps splitting.
- Impurity approaches 0.
- Memorizes training data.

Result:
- Low Bias
- High Variance

Interview Line:
"A fully grown decision tree has low bias and high variance."

--------------------------------------------------

11. PRE-PRUNING

Definition:
- Stop Tree Growth Early.

Methods:
- max_depth
- min_samples_split
- min_samples_leaf
- max_leaf_nodes
- min_impurity_decrease

Advantages:
+ Faster
+ Less Memory
+ Simpler Tree

Disadvantages:
- Can Underfit
- May Stop Too Early

--------------------------------------------------

12. POST-PRUNING

Definition:
- Grow Full Tree First
- Remove Unnecessary Branches

Types:
1. Reduced Error Pruning (REP)
2. Cost Complexity Pruning (CCP)

Advantages:
+ Better Generalization
+ Lower Underfitting Risk

Disadvantages:
- Slower
- More Computation

--------------------------------------------------

13. REDUCED ERROR PRUNING (REP)

Build Full Tree
↓
Remove Branch
↓
Check Validation Performance
↓
No Performance Drop?
↓
Keep Branch Removed

Idea:
"If branch doesn't improve validation performance, remove it."

--------------------------------------------------

14. COST COMPLEXITY PRUNING (CCP)

sklearn Parameter:
ccp_alpha

Cost =
Error
+
α(Tree Complexity)

α ↑
→ More Pruning
→ Smaller Tree

α = 0
→ Full Tree

Idea:
"Does this branch justify its complexity?"

--------------------------------------------------

15. ADVANTAGES

+ Highly Interpretable
+ Easy Visualization
+ No Scaling Required
+ Handles Non-Linear Relationships
+ Classification + Regression
+ Feature Importance Available
+ Minimal Preprocessing

--------------------------------------------------

16. DISADVANTAGES

- Overfitting
- High Variance
- Unstable
- Sensitive to Data Changes
- Poor Extrapolation

Interview Line:
"Decision Trees are excellent at interpolation but poor at extrapolation."

--------------------------------------------------

17. TREE-BASED FEATURE SELECTION

Type:
Embedded Feature Selection

Models:
- Decision Tree
- Random Forest
- XGBoost
- LightGBM

Process:
Train Tree
→ Get Feature Importance
→ Keep Important Features
→ Remove Weak Features

--------------------------------------------------

18. IMPORTANT SKLEARN COMMANDS

DecisionTreeClassifier()

DecisionTreeRegressor()

export_text(tree)
→ Print Tree Rules

plot_tree(tree)
→ Visualize Tree

model.feature_importances_
→ Feature Importance

criterion='gini'
criterion='entropy'

ccp_alpha=0.01

--------------------------------------------------

19. ULTRA-SHORT REVISION

- sklearn uses CART.
- CART Classification → Gini.
- CART Regression → MSE/Variance.
- Gini = Probability of incorrect classification.
- Classification Tree → Predict Class.
- Regression Tree → Predict Mean Value.
- Feature Importance = Total Impurity Reduction.
- Overfitting → Low Bias + High Variance.
- Pre-Pruning → Stop Early.
- Post-Pruning → Grow Then Trim.
- REP → Validation Based.
- CCP → Complexity Penalty Based.
- Strength → Interpretability.
- Weakness → Overfitting + Poor Extrapolation.
- Tree-Based Models provide Feature Importance naturally.
```
</pre>