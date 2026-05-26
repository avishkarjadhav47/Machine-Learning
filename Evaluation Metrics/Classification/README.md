========================================================
        CLASSIFICATION EVALUATION METRICS
                PLACEMENT NOTES
========================================================

WHY CLASSIFICATION METRICS?
--------------------------------------------------------
Used to:
- Measure classification performance
- Understand model mistakes
- Compare classifiers
- Handle imbalanced datasets

Main Metrics:
1. Accuracy
2. Confusion Matrix
3. Precision
4. Recall
5. F1 Score
6. ROC Curve
7. AUC-ROC

========================================================
1. CONFUSION MATRIX
========================================================

sklearn Format:

| Actual \ Predicted | Negative | Positive |
|--------------------|----------|-----------|
| Negative           | TN       | FP        |
| Positive           | FN       | TP        |

Important Rules:
- Rows = Actual
- Columns = Predicted
- Diagonal = Correct predictions

========================================================
2. TP, TN, FP, FN
========================================================

TP (True Positive):
- Predicted Positive
- Actually Positive

Example:
Cancer patient correctly detected

--------------------------------------------------------

TN (True Negative):
- Predicted Negative
- Actually Negative

Example:
Healthy person correctly identified

--------------------------------------------------------

FP (False Positive):
- Predicted Positive
- Actually Negative
- False Alarm

Example:
Healthy person predicted cancer

Also Called:
- Type I Error

--------------------------------------------------------

FN (False Negative):
- Predicted Negative
- Actually Positive
- Missed Detection

Example:
Cancer patient predicted healthy

Also Called:
- Type II Error

========================================================
3. HYPOTHESIS TESTING CONNECTION
========================================================

Type I Error:
- Reject H0 when H0 true
- Equivalent to False Positive

--------------------------------------------------------

Type II Error:
- Fail to reject H0 when H1 true
- Equivalent to False Negative

--------------------------------------------------------

Correct Statistical Language:
- Reject H0
- Fail to reject H0

Avoid:
- Accept H0
- Reject H1

========================================================
4. ACCURACY
========================================================

Formula:
Accuracy = (TP + TN)/(TP + TN + FP + FN)

Definition:
- Overall correctness of predictions

Advantages:
- Easy interpretation
- Good for balanced datasets

Disadvantages:
- Misleading for imbalanced datasets

Use Cases:
- Balanced datasets
- Baseline metric

Key Point:
- Higher Accuracy = Better

========================================================
5. PRECISION
========================================================

Formula:
Precision = TP/(TP + FP)

Definition:
- Out of predicted positives,
  how many actually positive

Focus:
- False Positives

Use Cases:
- Spam Detection
- Loan Approval

Interpretation:
"When model predicts positive,
how often is it correct?"

Key Point:
- Higher Precision = Better

========================================================
6. RECALL (Sensitivity / TPR)
========================================================

Formula:
Recall = TP/(TP + FN)

Definition:
- Out of actual positives,
  how many correctly detected

Focus:
- False Negatives

Use Cases:
- Cancer Detection
- Fraud Detection

Interpretation:
"How many actual positives
did model catch?"

Key Point:
- Higher Recall = Better

========================================================
PRECISION vs RECALL
========================================================

Precision:
- Reduce FP
- Reduce false alarms

Recall:
- Reduce FN
- Reduce missed detections

Rule:
- FP dangerous → Precision
- FN dangerous → Recall

========================================================
7. F1 SCORE
========================================================

Formula:
F1 = 2PR/(P + R)

Definition:
- Harmonic mean of Precision & Recall

Advantages:
- Balances Precision & Recall
- Good for imbalanced datasets

Use Cases:
- Imbalanced datasets
- General classification tasks

Important Point:
High only when:
- Precision high
- Recall high

Interpretation:
"Balanced performance of
Precision and Recall"

Key Point:
- Higher F1 = Better

========================================================
8. IMBALANCED DATASET
========================================================

Definition:
- One class dominates another

Examples:
- Fraud Detection
- Disease Prediction
- Spam Detection

Problem:
- Accuracy becomes misleading

Example:
99 normal
1 fraud

Model predicts all normal:
Accuracy = 99%

But model useless.

========================================================
9. ROC CURVE + THRESHOLD NOTES
========================================================

ROC:
- Receiver Operating Characteristic

Plots:
- TPR vs FPR

Axes:
- Y-axis → TPR
- X-axis → FPR

Purpose:
- Threshold tuning
- Model comparison

Ideal Point:
- FPR = 0
- TPR = 1

Top-left corner

========================================================
10. predict_proba()
========================================================

Syntax:

model.predict_proba(X_test)

Purpose:
- Returns probability of each class

Example Output:

[
 [0.2,0.8],
 [0.7,0.3]
]

Meaning:
[class0_prob , class1_prob]

========================================================
11. predict_proba(X_test)[:,1]
========================================================

Purpose:
- Returns probability of positive class

Syntax Breakdown:
:  → all rows
1  → second column

Example:

[
 [0.2,0.8],
 [0.7,0.3]
]

Output:
[0.8,0.3]

Used In:
- ROC Curve
- AUC
- Threshold tuning
- Precision-Recall Curve

Important:
predict()       → labels
predict_proba() → probabilities

========================================================
12. TPR (True Positive Rate)
========================================================

Also Called:
- Recall
- Sensitivity

Formula:
TPR = TP/(TP + FN)

Meaning:
- Actual positives correctly predicted

========================================================
13. FPR (False Positive Rate)
========================================================

Formula:
FPR = FP/(FP + TN)

Meaning:
- Negatives wrongly predicted positive

========================================================
14. roc_curve()
========================================================

Syntax:

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test,y_scores)

Inputs:
- y_test   → actual labels
- y_scores → probabilities

Outputs:
- fpr
- tpr
- thresholds

========================================================
15. THRESHOLD
========================================================

Default Threshold:
- 0.5

Rule:

if probability >= threshold:
    class = 1
else:
    class = 0

--------------------------------------------------------

Low Threshold:
- More positives predicted
- TPR increases
- FPR increases

--------------------------------------------------------

High Threshold:
- Fewer positives predicted
- TPR decreases
- FPR decreases

========================================================
16. THRESHOLD TUNING
========================================================

Purpose:
- Find better threshold than 0.5

Useful For:
- Imbalanced datasets
- Improve Recall
- Improve Precision
- Reduce FP

========================================================
17. YOUDEN INDEX
========================================================

Formula:
J = TPR - FPR

Goal:
- Maximize TPR
- Minimize FPR

Higher value = Better threshold

========================================================
18. FINDING OPTIMAL THRESHOLD
========================================================

Code:

optimal_idx = np.argmax(tpr - fpr)

optimal_threshold = thresholds[optimal_idx]

Meaning:
- Finds threshold where
  (TPR - FPR) maximum

========================================================
19. np.argmax()
========================================================

Purpose:
- Returns index of maximum value

Example:

arr = [2,5,1]

np.argmax(arr)

Output:
1

========================================================
20. FULL ROC WORKFLOW
========================================================

y_scores = model.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(y_test,y_scores)

optimal_idx = np.argmax(tpr - fpr)

optimal_threshold = thresholds[optimal_idx]

========================================================
21. AUC (Area Under Curve)
========================================================

Definition:
- Area under ROC curve

Range:
- 0 → 1

Interpretation:
- 1.0  → Perfect
- 0.9+ → Excellent
- 0.8  → Good
- 0.7  → Fair
- 0.5  → Random Guessing

Higher AUC = Better classifier

========================================================
22. MULTICLASS CONFUSION MATRIX
========================================================

| Actual \ Predicted | A | B | C |
|--------------------|---|---|---|
| A                  |AA |AB |AC |
| B                  |BA |BB |BC |
| C                  |CA |CB |CC |

Important Rules:
- Rows = Actual
- Columns = Predicted
- Diagonal = Correct predictions

========================================================
23. MULTICLASS METRICS
========================================================

One-vs-Rest Strategy:
For each class:
- Positive = Current class
- Negative = Remaining classes

Then calculate:
- TP
- FP
- FN
- TN

========================================================
24. AVERAGES IN MULTICLASS
========================================================

average=None
--------------
- Per-class metrics

--------------------------------------------------------

average='macro'
----------------
- Simple average
- Equal importance to all classes

--------------------------------------------------------

average='weighted'
-------------------
- Weighted by class size
- Best for imbalanced datasets

--------------------------------------------------------

average='micro'
----------------
- Global TP/FP/FN calculation
- Overall performance

========================================================
25. classification_report()
========================================================

Gives:
- Precision
- Recall
- F1-score
- Support

Does NOT give:
- ROC-AUC
- Confusion Matrix

========================================================
IMPORTANT INTERVIEW COMPARISONS
========================================================

Accuracy vs F1 Score
-------------------------
Accuracy:
- Balanced datasets

F1 Score:
- Imbalanced datasets

--------------------------------------------------------

Precision vs Recall
-------------------------
Precision:
- Reduce FP

Recall:
- Reduce FN

========================================================
MOST IMPORTANT PLACEMENT POINTS
========================================================

- Accuracy fails on imbalanced datasets
- Precision important when FP dangerous
- Recall important when FN dangerous
- F1 balances Precision & Recall
- ROC used for threshold tuning
- AUC used for model comparison
- predict() gives labels
- predict_proba() gives probabilities

========================================================
LAST MINUTE REVISION
========================================================

predict_proba() → probabilities
[:,1] → probability of class 1
ROC → TPR vs FPR
TPR → TP/(TP+FN)
FPR → FP/(FP+TN)
Threshold default → 0.5
Best threshold → max(TPR-FPR)
AUC high → better model

========================================================
MEMORY TRICKS
========================================================

Accuracy  → Overall correctness
Precision → Correct predicted positives
Recall    → Catch actual positives
F1 Score  → Balance Precision & Recall
ROC       → TPR vs FPR graph
AUC       → Overall classifier quality

========================================================
SKLEARN CODE
========================================================

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    roc_curve,
    roc_auc_score
)

# Accuracy
acc = accuracy_score(y_test,y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test,y_pred)

# Precision
precision = precision_score(y_test,y_pred)

# Recall
recall = recall_score(y_test,y_pred)

# F1 Score
f1 = f1_score(y_test,y_pred)

# Probability scores
y_scores = model.predict_proba(X_test)[:,1]

# ROC
fpr,tpr,thresholds = roc_curve(y_test,y_scores)

# AUC
auc = roc_auc_score(y_test,y_scores)

print(acc)
print(cm)
print(precision)
print(recall)
print(f1)
print(auc)

========================================================