<pre>
===========================================
Model Evaluation / Resampling Methods
│
├── Hold-Out
├── Cross-Validation
│   ├── LOOCV
│   ├── Leave-P-Out
│   ├── k-Fold
│   ├── Stratified k-Fold
│   ├── Repeated k-Fold
│   └── Nested k-Fold
├── Bootstrapping
└── Permutation Test
===========================================

1. HOLD-OUT METHOD
------------------

Idea:
Single train-test split.

Example:
80% Train
20% Test

Sklearn:
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

Advantages (+):
✔ Very fast
✔ Simple to implement
✔ Good for huge datasets

Disadvantages (-):
✘ High variance
✘ Performance depends on random split
✘ Can give misleading accuracy

When to Use:
✔ Large datasets
✔ Quick baseline model
✔ Fast experimentation

Avoid When:
✘ Small dataset
✘ Need reliable evaluation

------------------------------------------------------------

2. CROSS VALIDATION (CV)
------------------------

Idea:
Repeated train-test splitting.

Main Benefit:
More reliable performance estimate.

General Sklearn:
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)

print(scores.mean())

Advantages (+):
✔ Better generalization estimate
✔ Reduces variance
✔ Better use of data

Disadvantages (-):
✘ Slower than hold-out
✘ Expensive for large models

When to Use:
✔ Medium/small datasets
✔ Model comparison
✔ Hyperparameter tuning

Avoid When:
✘ Very large datasets
✘ Real-time training constraints

============================================================
A) LOOCV (Leave-One-Out Cross Validation)
============================================================

Idea:
1 sample for testing,
remaining for training.

Number of folds = number of samples

Sklearn:
from sklearn.model_selection import LeaveOneOut

cv = LeaveOneOut()

scores = cross_val_score(model, X, y, cv=cv)

Advantages (+):
✔ Maximum data for training
✔ Low bias

Disadvantages (-):
✘ Very slow
✘ High variance
✘ Computationally expensive

When to Use:
✔ Extremely small datasets

Avoid When:
✘ Large datasets

------------------------------------------------------------

B) LEAVE-P-OUT CV
-----------------

Idea:
P samples used for testing.

Sklearn:
from sklearn.model_selection import LeavePOut

cv = LeavePOut(p=2)

Advantages (+):
✔ More exhaustive evaluation

Disadvantages (-):
✘ Extremely expensive
✘ Impractical for large data

When to Use:
✔ Research/small datasets

Avoid When:
✘ Almost always for big datasets

------------------------------------------------------------

C) K-FOLD CV
------------

Idea:
Split into K folds.

Most common:
K = 5 or 10

Sklearn:
from sklearn.model_selection import KFold

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(model, X, y, cv=cv)

Advantages (+):
✔ Balanced bias-variance tradeoff
✔ Reliable evaluation
✔ Widely accepted

Disadvantages (-):
✘ Slower than hold-out

When to Use:
✔ Default choice for ML tasks

Avoid When:
✘ Time-series data (without proper split)

------------------------------------------------------------

D) STRATIFIED K-FOLD
--------------------

Idea:
Maintains class distribution in each fold.

Important for imbalanced datasets.

Sklearn:
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

Advantages (+):
✔ Handles imbalance better
✔ More stable scores

Disadvantages (-):
✘ Mainly for classification only

When to Use:
✔ Imbalanced classification problems

Avoid When:
✘ Regression tasks

------------------------------------------------------------

E) REPEATED K-FOLD
------------------

Idea:
K-Fold repeated multiple times
with different random splits.

Sklearn:
from sklearn.model_selection import RepeatedKFold

cv = RepeatedKFold(
    n_splits=5,
    n_repeats=10,
    random_state=42
)

Advantages (+):
✔ More robust estimate
✔ Reduces randomness

Disadvantages (-):
✘ Computationally expensive

When to Use:
✔ Need highly reliable estimate

Avoid When:
✘ Limited computation time

------------------------------------------------------------

F) NESTED K-FOLD
----------------

Idea:
Outer CV → model evaluation
Inner CV → hyperparameter tuning

Prevents data leakage.

Sklearn:
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

grid = GridSearchCV(model, param_grid, cv=5)

scores = cross_val_score(grid, X, y, cv=5)

Advantages (+):
✔ Best unbiased evaluation
✔ Proper hyperparameter tuning

Disadvantages (-):
✘ Very slow
✘ Complex

When to Use:
✔ Research
✔ Important model selection

Avoid When:
✘ Quick experimentation

------------------------------------------------------------

3. BOOTSTRAPPING
----------------

Idea:
Sampling WITH replacement.

Some samples repeat,
some are left out.

Used in:
Random Forest,
confidence intervals,
uncertainty estimation.

Sklearn:
from sklearn.utils import resample

X_boot, y_boot = resample(
    X, y,
    replace=True,
    n_samples=len(X),
    random_state=42
)

Advantages (+):
✔ Works well on small datasets
✔ Estimates uncertainty
✔ Robust statistics

Disadvantages (-):
✘ Duplicate samples
✘ Can overfit noisy data

When to Use:
✔ Small datasets
✔ Confidence intervals
✔ Ensemble methods

Avoid When:
✘ Extremely noisy datasets

------------------------------------------------------------

4. PERMUTATION TEST
-------------------

Idea:
Shuffle labels randomly
to check statistical significance.

If shuffled accuracy ≈ real accuracy
→ model learned nothing.

Sklearn:
from sklearn.model_selection import permutation_test_score

score, perm_scores, pvalue = permutation_test_score(
    model,
    X,
    y,
    scoring="accuracy",
    cv=5,
    n_permutations=100
)

Advantages (+):
✔ Checks if model is truly learning
✔ Statistical significance testing

Disadvantages (-):
✘ Very computationally expensive

When to Use:
✔ Research
✔ Feature importance
✔ Model validation

Avoid When:
✘ Fast production workflows

============================================================
IMPORTANT INTERVIEW DIFFERENCES
============================================================

Hold-Out:
→ Single split

Cross Validation:
→ Multiple splits

Bootstrapping:
→ Sampling WITH replacement

Permutation Test:
→ Shuffle labels/features for significance testing

LOOCV:
→ 1 test sample

Stratified KFold:
→ Preserves class balance

Nested CV:
→ Hyperparameter tuning + evaluation

============================================================
MOST IMPORTANT PRACTICAL CHOICES
============================================================

Huge Dataset:
→ Hold-Out

Normal ML Problem:
→ K-Fold CV

Imbalanced Classification:
→ Stratified KFold

Tiny Dataset:
→ LOOCV or Bootstrap

Hyperparameter Tuning:
→ Nested CV

Statistical Significance:
→ Permutation Test
```

========================================
NUMBER OF MODEL RUNS
========================================

Hold-Out
---------
Runs = 1

Reason:
Single train-test split


K-Fold Cross Validation
-----------------------
Runs = K

Example:
K = 5

Runs = 5


Repeated K-Fold
---------------
Runs = K × Repeats

Example:
K = 5
Repeats = 10

Runs = 5 × 10 = 50


LOOCV (Leave-One-Out CV)
------------------------
Runs = n

Reason:
Each sample becomes test set once

Example:
n = 100

Runs = 100


Leave-P-Out CV
---------------
Runs = nCp

Formula:
n! / (p! × (n-p)!)

Example:
n = 100
p = 2

Runs = 4950


Nested K-Fold
--------------
Runs ≈ Outer K × Inner K

Example:
Outer K = 5
Inner K = 5

Runs ≈ 25

(Note:
Actual runs are much higher because
hyperparameter tuning trains many models internally.)

Boostrapping-->n_bootstrap
Permutation Test-->n_permutations

</pre>