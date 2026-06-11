<pre>

# OUTLIER DETECTION & TREATMENT

OUTLIERS
│
├── 1. WHAT ARE OUTLIERS?
│   │
│   ├── Definition
│   │   └── Observations significantly different
│   │       from the majority of data points.
│   │
│   └── Example
│       └── Salary:
│           20k, 25k, 30k, 35k,10 Cr
│                               ↑
│                            Outlier
│
├── 2. WHY ARE OUTLIERS IMPORTANT?
│   │
│   ├── Distort Mean
│   ├── Affect Standard Deviation
│   ├── Bias Machine Learning Models
│   └── Reduce Prediction Accuracy
│
├── 3. IMPACT ON MACHINE LEARNING
│   │
│   ├── Highly Affected Algorithms
│   │   ├── Linear Regression
│   │   ├── Logistic Regression
│   │   ├── PCA
│   │   ├── KNN
│   │   └── Deep Learning
│   │
│   └── Less Affected Algorithms
│       ├── Decision Trees
│       ├── Random Forest
│       ├── XGBoost
│       └── Gradient Boosting
│
├── 4. OUTLIER DETECTION METHODS
│   │
│   ├── A. Z-SCORE METHOD
│   │   │
│   │   ├── Use When?
│   │   │   └── Normal Distribution
│   │   │
│   │   ├── Formula
│   │   │   └── Z = (X - μ) / σ
│   │   │
│   │   └── Rule
│   │       └── |Z| > 3
│   │
│   ├── B. IQR METHOD
│   │   │
│   │   ├── Use When?
│   │   │   └── Skewed Distribution
│   │   │
│   │   ├── Formula
│   │   │   └── IQR = Q3 - Q1
│   │   │
│   │   ├── Lower Limit
│   │   │   └── Q1 - 1.5(IQR)
│   │   │
│   │   ├── Upper Limit
│   │   │   └── Q3 + 1.5(IQR)
│   │   │
│   │   └── Rule
│   │       └── Outside Limits = Outlier
│   │
│   └── C. PERCENTILE METHOD
│       │
│       ├── Use When?
│       │   └── Any Distribution
│       │
│       └── Common Thresholds
│           ├── Below 1%
│           ├── Below 5%
│           ├── Above 95%
│           └── Above 99%
│
├── 5. OUTLIER TREATMENT METHODS
│   │
│   ├── A. TRIMMING
│   │   ├── Remove Outliers
│   │   ├── Fast
│   │   └── Data Loss
│   │
│   ├── B. CAPPING (WINSORIZATION in case of PERCENTILE METHOD ) 
│   │   ├── Replace Extreme Values
│   │   ├── No Data Loss
│   │   └── Most Preferred
│   │
│   ├── C. MISSING VALUE TREATMENT
│   │   └── Outlier → NaN → Imputation
│   │
│   └── D. DISCRETIZATION
│       └── Convert Values into Bins
│           Example:
│           Age → 0-10, 10-20, 20-30
│
├── 6. SHOULD WE REMOVE OUTLIERS?
│   │
│   ├── REMOVE
│   │   │
│   │   ├── Age = 838
│   │   ├── Height = 20m
│   │   └── Negative Salary
│   │
│   └── KEEP
│       │
│       ├── Fraud Detection
│       ├── Anomaly Detection
│       ├── Cyber Security
│       └── Medical Diagnosis
│
├── 7. DECISION FLOW
│
│       Check Distribution
│              │
│              ▼
│       Normal Data?
│              │
│      Yes ───► Z-Score
│              │
│              ▼
│          No
│              │
│              ▼
│       Skewed Data?
│              │
│      Yes ───► IQR
│              │
│              ▼
│          No
│              │
│              ▼
│      Percentile Method
│
└── 8. REVISION (30 SECONDS)
    │
    ├── Normal Data  → Z-Score
    ├── Skewed Data  → IQR
    ├── Any Data     → Percentile
    ├── Preferred Treatment → Capping
    └── Tree Models are less affected than Linear Models



# OUTLIER DETECTION & TREATMENT 

=========================================================
1. Z-SCORE METHOD (3-SIGMA RULE)
=========================================================

WHEN TO USE?
------------
✔ Data is Normally Distributed
✔ Bell-shaped distribution
✔ Mean ≈ Median ≈ Mode

CONCEPT
-------
In a normal distribution:

68% data lies within ±1σ
95% data lies within ±2σ
99.7% data lies within ±3σ

Any observation outside ±3σ is treated as an Outlier.

FORMULAS
--------

Z-Score:

z = (x - μ) / σ

where,
x = data point
μ = mean
σ = standard deviation

Outlier Condition:

z < -3  OR  z > +3

OR

Lower Limit = μ - 3σ
Upper Limit = μ + 3σ

If value < Lower Limit OR value > Upper Limit
=> OUTLIER

STEPS
-----
1. Check whether data is normally distributed.
2. Calculate Mean (μ).
3. Calculate Standard Deviation (σ).
4. Find Lower and Upper limits.
5. Detect outliers.
6. Apply treatment:
   - Trimming
   - Capping

ADVANTAGES
----------
✔ Very simple
✔ Fast
✔ Effective for normal distributions

LIMITATIONS
-----------
✘ Not suitable for skewed data
✘ Sensitive to extreme values

=========================================================
2. IQR METHOD (BOX PLOT METHOD)
=========================================================

WHEN TO USE?
------------
✔ Data is Skewed
✔ Not Normally Distributed
✔ Right-skewed or Left-skewed data

IMPORTANT TERMS
---------------
Q1 = 25th Percentile

Q2 = 50th Percentile
   = Median

Q3 = 75th Percentile

IQR = Q3 - Q1

FORMULAS
--------

Lower Limit

= Q1 - 1.5 × IQR

Upper Limit

= Q3 + 1.5 × IQR

OUTLIER CONDITION
-----------------
If value < Lower Limit
OR

If value > Upper Limit

=> OUTLIER

STEPS
-----
1. Plot Box Plot.
2. Calculate Q1 and Q3.
3. Find IQR.
4. Compute Lower & Upper Limits.
5. Detect Outliers.
6. Apply Trimming or Capping.

ADVANTAGES
----------
✔ Works well on skewed data
✔ Robust to extreme values
✔ Most widely used method

LIMITATIONS
-----------
✘ Less effective when data is perfectly normal
✘ Threshold (1.5×IQR) is heuristic

=========================================================
3. PERCENTILE METHOD
=========================================================

WHEN TO USE?
------------
✔ Any distribution
✔ When business rules are available
✔ Large datasets

CONCEPT
-------
Values beyond selected percentiles are treated as outliers.

Common choices:

1st - 99th Percentile

or

5th - 95th Percentile

or

2.5th - 97.5th Percentile

depending on business requirement.

FORMULAS
--------

Lower Limit
= P1 or P5

Upper Limit
= P99 or P95

(Chosen according to problem)

OUTLIER CONDITION
-----------------
Value < Lower Percentile

OR

Value > Upper Percentile

=> OUTLIER

STEPS
-----
1. Select percentile thresholds.
2. Calculate lower percentile.
3. Calculate upper percentile.
4. Detect outliers.
5. Apply treatment.

ADVANTAGES
----------
✔ Flexible
✔ Works on any distribution
✔ Easy to implement

LIMITATIONS
-----------
✘ Threshold selection is subjective
✘ May remove valid extreme observations

=========================================================
OUTLIER TREATMENT TECHNIQUES
=========================================================

A) TRIMMING
-----------

Definition:
Remove outlier rows completely.

Example:

Data:
[10, 12, 15, 18, 200]

After Trimming:
[10, 12, 15, 18]

Pros:
✔ Simple
✔ Fast

Cons:
✘ Data loss
✘ May remove important information

---------------------------------------------------------

B) CAPPING (called as 'WINSORIZATION' in case of PERCENTILE Method)
--------------------------

Definition:
Replace outliers with boundary values.

Example:

Upper Limit = 100

Data:
[10, 12, 15, 18, 200]

After Capping:
[10, 12, 15, 18, 100]

Pros:
✔ No data loss
✔ Keeps dataset size unchanged

Cons:
✘ Distribution gets modified


====================================================
IMPORTANT INTERVIEW NOTES
====================================================

1. SHOULD WE ALWAYS REMOVE OUTLIERS?
------------------------------------
NO.

Remove Outliers:
✔ Data entry errors
✔ Measurement errors
✔ Impossible values
  (Age = 300, Salary = -5000)

Keep Outliers:
✔ Genuine rare observations
✔ Fraud detection
✔ Anomaly detection
✔ High-value customers

Example:
Bill Gates' salary among normal employees
→ Outlier but valid data.


2. WHICH ML ALGORITHMS ARE SENSITIVE TO OUTLIERS?
-------------------------------------------------

Highly Sensitive:
✔ Linear Regression
✔ Logistic Regression
✔ KNN
✔ K-Means Clustering
✔ PCA
✔ Neural Networks

Less Sensitive:
✔ Decision Trees
✔ Random Forest
✔ XGBoost
✔ LightGBM

Reason:
Tree-based models split data using thresholds,
so extreme values usually don't affect them much.


3. DATASET SIZE IMPACT
-------------------------------------------------

Trimming:
✔ Removes rows
✘ Dataset size decreases

Capping:
✔ Dataset size unchanged
✔ All rows retained

4. EFFECT ON STATISTICS
-------------------------------------------------
Trimming:
→ Mean changes
→ Std Dev changes
→ Quartiles may change
→ Dataset size changes

Capping:
→ Mean changes
→ Std Dev changes
→ Quartiles usually change less
→ Dataset size unchanged

5. QUICK COMPARISON
-------------------------------------------------

               Trimming      Capping
Rows Removed?     YES          NO
Data Loss?        YES          NO
Distribution      Changes      Changes
Dataset Size      Smaller      Same
Preferred?        Less         More

In practice:
Capping/Winsorization is usually preferred
because it preserves data.


6.ONE-LINE INTERVIEW ANSWER
-------------------------------------------------
Outliers can be detected using:
1. Z-Score (Normal Data)
2. IQR (Skewed Data)
3. Percentile Method (Any Data)

Outliers can be treated using:
1. Trimming (Remove rows)
2. Capping/Winsorization (Replace with limits)

Capping is generally preferred because
it avoids data loss.


7.Does distribution of data changes ?
-------------------------------------------------
Detection Methods:
✔ Z-Score
✔ IQR
✔ Percentile
→ Distribution remains unchanged
→ Only identifies outliers

Treatment Methods:
✔ Trimming
✔ Capping/Winsorization
→ Distribution changes

Special Note:
Trimming changes distribution more because rows are deleted.
Capping changes distribution less because rows are retained and only values are adjusted.



8.METHOD SELECTION CHEAT SHEET
-------------------------------------------------
Normal Distribution
      ↓
Use Z-Score Method

Skewed Distribution
      ↓
Use IQR Method

Any Distribution / Business Rule Based
      ↓
Use Percentile Method



9.PLACEMENT INTERVIEW ANSWER
-------------------------------------------------
Q: How do you handle Outliers?
1. First visualize distribution using histogram/boxplot.
2. If data is normal → use Z-score.
3. If data is skewed → use IQR method.
4. If business thresholds exist → use Percentile method.
5. After detection:
   - Trimming (remove rows)
   - Capping/Winsorization (replace with limits)
6. Recheck distribution and model performance.

=========================================================
ONE-LINE MEMORY TRICKs
=========================================================
Normal Data  → Z-Score
Skewed Data  → IQR
Any Data     → Percentile

Treatment:
Remove = Trimming
Replace = Capping/Winsorization


Detection Method ≠ Treatment Method

Z-Score, IQR, Percentile
→ Only detect outliers.

Trimming, Capping
→ Actually treat outliers.

You can mix them:

IQR Detection + Capping
Z-Score Detection + Trimming
Percentile Detection + Capping


</pre>