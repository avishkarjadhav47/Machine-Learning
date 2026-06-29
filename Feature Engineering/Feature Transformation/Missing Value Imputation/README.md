<pre>

MISSING VALUE HANDLING
│
├── Missing Data Types
│      ├── MCAR
│      ├── MAR
│      └── MNAR
│
├── Deletion
│      ├── Row
│      └── Column
│
├── Imputation
│      │
│      ├── Univariate
│      │      ├── Mean
│      │      ├── Median
│      │      ├── Mode
│      │      ├── Constant
│      │      ├── Random Sample
│      │      ├── End of Distribution
│      │      └── Missing Category
│      │
│      └── Multivariate
│             ├── KNN Imputer
│             ├── Regression Imputation
│             └── Iterative Imputer (MICE)
│
└── Time Series
       ├── Forward Fill
       ├── Backward Fill
       ├── Linear Interpolation
       └── Spline Interpolation

================================================================================
1. MISSING DATA TYPES (Before choosing any method)
================================================================================

MCAR (Missing Completely At Random)
───────────────────────────────────
Working:
• Missingness is completely random and unrelated to any variable.

Example:
• Sensor randomly failed to record temperature.

When to Use:
• Safe to delete rows or use simple imputation.

Advantages:
✔ Least biased
✔ Easy to handle

Disadvantages:
✘ Rare in real-world datasets


MAR (Missing At Random)
───────────────────────────────────
Working:
• Missing depends on other observed variables, not itself.

Example:
• Salary missing because Occupation is missing.

When to Use:
• Multivariate methods (KNN, MICE) work well.

Advantages:
✔ Most common assumption
✔ Advanced imputation performs well

Disadvantages:
✘ Cannot be verified with certainty


MNAR (Missing Not At Random)
───────────────────────────────────
Working:
• Missing depends on its own value.

Example:
• High-income people hide salary.

When to Use:
• Domain knowledge required.
• Simple imputation usually performs poorly.

Advantages:
✔ Represents many real business cases

Disadvantages:
✘ Hardest to handle
✘ May introduce bias



================================================================================
2. DELETION METHODS
================================================================================

A. Row Deletion (Listwise Deletion)
───────────────────────────────────
Working:
• Remove rows containing missing values.

When to Use:
✔ Missing values < 5%
✔ Large dataset
✔ MCAR assumption

Advantages:
✔ Very simple
✔ No artificial values
✔ Fast

Disadvantages:
✘ Data loss
✘ Smaller dataset
✘ Biased if not MCAR

Implementation:
df.dropna()


B. Column Deletion
──────────────────
Working:
• Remove entire feature.

When to Use:
✔ Missing percentage > 40–60%
✔ Feature not important

Advantages:
✔ Simple
✔ Removes noisy feature

Disadvantages:
✘ Permanent information loss

Implementation:
df.drop(columns=['column'])




================================================================================
3. IMPUTATION METHODS
================================================================================

===========================
A. UNIVARIATE IMPUTATION
===========================

(Uses only the same column)

------------------------------------------------
1. Mean Imputation
------------------------------------------------
Working:
Replace missing values with column mean.

When to Use:
✔ Numerical feature
✔ Approximately normal distribution
✔ Few missing values

Advantages:
✔ Fast
✔ Easy
✔ Preserves mean

Disadvantages:
✘ Sensitive to outliers
✘ Reduces variance
✘ Distorts correlations

Implementation:
from sklearn.impute import SimpleImputer
SimpleImputer(strategy="mean")


------------------------------------------------
2. Median Imputation
------------------------------------------------
Working:
Replace missing values with median.

When to Use:
✔ Skewed distribution
✔ Outliers present

Advantages:
✔ Robust to outliers
✔ Better for skewed data

Disadvantages:
✘ Ignores relationships
✘ Reduces variance

Implementation:
SimpleImputer(strategy="median")


------------------------------------------------
3. Mode Imputation
------------------------------------------------
Working:
Replace missing categorical values with most frequent value.

When to Use:
✔ Categorical features

Advantages:
✔ Simple
✔ Maintains valid category

Disadvantages:
✘ Over-represents majority class

Implementation:
SimpleImputer(strategy="most_frequent")


------------------------------------------------
4. Constant Value Imputation
------------------------------------------------
Working:
Replace missing values with fixed value.

Examples:
0
-1
999
"Unknown"

When to Use:
✔ Business-specific default exists
✔ Missing has fixed meaning

Advantages:
✔ Very simple
✔ No data loss

Disadvantages:
✘ Can introduce bias
✘ Artificial values

Implementation:
SimpleImputer(strategy="constant",
              fill_value=0)


------------------------------------------------
5. Random Sample Imputation
------------------------------------------------
Working:
Randomly sample existing values from same column.

When to Use:
✔ Preserve original distribution
✔ MCAR

Advantages:
✔ Preserves variance
✔ Better distribution than mean

Disadvantages:
✘ Random output
✘ Less reproducible

Implementation:
No direct sklearn function
Use:
Series.sample()


------------------------------------------------
6. End of Distribution Imputation
------------------------------------------------
Working:
Replace missing values with an extreme value
(e.g. Mean + 3×Std).

When to Use:
✔ Missing itself is informative
✔ Tree models

Advantages:
✔ Creates missing indicator naturally
✔ Easy

Disadvantages:
✘ Introduces artificial outliers

Implementation:
Manual
df[col]=df[col].fillna(df[col].mean()+3*df[col].std())


------------------------------------------------
7. Missing Category Imputation
------------------------------------------------
Working:
Treat missing as a new category.

Example:
Red
Blue
NaN

↓

Red
Blue
Missing

When to Use:
✔ Categorical variables
✔ Missing carries information

Advantages:
✔ No information loss
✔ Good for tree models

Disadvantages:
✘ Extra artificial category

Implementation:
df[col]=df[col].fillna("Missing")




===========================
B. MULTIVARIATE IMPUTATION
===========================

(Uses multiple columns)

------------------------------------------------
1. KNN Imputer
------------------------------------------------
Working:
Find K nearest records using other features.
Fill missing value using neighbor average/mode.

When to Use:
✔ Features correlated
✔ Moderate dataset
✔ Numerical features

Advantages:
✔ Better than mean
✔ Preserves local patterns

Disadvantages:
✘ Slow
✘ Sensitive to scaling
✘ Performs poorly in high dimensions

Implementation:
from sklearn.impute import KNNImputer
KNNImputer(n_neighbors=5)



------------------------------------------------
2. Regression Imputation
------------------------------------------------
Working:
Train regression model using complete rows.
Predict missing values.

Example:
Age = f(Salary, Experience)

When to Use:
✔ Strong linear relationship
✔ Moderate missing values

Advantages:
✔ Uses feature relationships
✔ Better estimates

Disadvantages:
✘ Underestimates uncertainty
✘ Can overfit

Implementation:
Manual
Train regression model
Predict missing values



------------------------------------------------
3. Iterative Imputer (MICE)
------------------------------------------------
Working:
Step 1:
Fill all missing values roughly (mean).

Step 2:
Predict one feature using all others.

Step 3:
Repeat for every feature.

Step 4:
Continue until convergence.

(Multivariate Imputation by Chained Equations)

When to Use:
✔ MAR
✔ Strong feature relationships
✔ High-quality imputation required

Advantages:
✔ Highly accurate
✔ Preserves relationships
✔ Better statistical properties

Disadvantages:
✘ Slow
✘ Computationally expensive
✘ Complex

Implementation:
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer




================================================================================
4. TIME SERIES IMPUTATION
================================================================================

------------------------------------------------
1. Forward Fill (ffill)
------------------------------------------------
Working:
Copy previous value forward.

Example:
10
12
NaN

↓

10
12
12

When to Use:
✔ Sensor data
✔ Stock prices
✔ Sequential data

Advantages:
✔ Very fast
✔ Preserves continuity

Disadvantages:
✘ Long gaps become inaccurate

Implementation:
df.fillna(method="ffill")
or
df.ffill()


------------------------------------------------
2. Backward Fill (bfill)
------------------------------------------------
Working:
Copy next value backward.

Example:
10
NaN
15

↓

10
15
15

When to Use:
✔ Future observation known
✔ Small gaps

Advantages:
✔ Simple
✔ Fast

Disadvantages:
✘ Uses future information
✘ May cause data leakage in forecasting

Implementation:
df.fillna(method="bfill")
or
df.bfill()


------------------------------------------------
3. Linear Interpolation
------------------------------------------------
Working:
Estimate value using straight line between neighbors.

Example:
10
NaN
20

↓

10
15
20

When to Use:
✔ Continuous numerical time series
✔ Smooth trends

Advantages:
✔ Better than ffill
✔ Maintains trend

Disadvantages:
✘ Poor for sudden changes

Implementation:
df.interpolate(method="linear")


------------------------------------------------
4. Spline Interpolation
------------------------------------------------
Working:
Fit smooth polynomial curve through data.

When to Use:
✔ Smooth nonlinear time series
✔ Scientific measurements

Advantages:
✔ Very smooth estimates
✔ Captures nonlinear trends

Disadvantages:
✘ Slower
✘ Can overfit

Implementation:
df.interpolate(method="spline",
               order=3)



================================================================================
PLACEMENT DECISION FLOW
================================================================================

Missing Values
│
├── <5% missing + Large Dataset
│      └── Delete Rows
│
├── >50% missing + Low Importance
│      └── Delete Column
│
├── Numerical
│      ├── Normal → Mean
│      ├── Skewed/Outliers → Median
│      ├── Preserve Distribution → Random Sample
│      ├── Business Default → Constant
│      └── Informative Missing → End of Distribution
│
├── Categorical
│      ├── Most Frequent → Mode
│      └── Missing is Informative → Missing Category
│
├── Correlated Features
│      ├── Moderate Dataset → KNN
│      ├── Linear Relationship → Regression
│      └── Highest Quality → MICE
│
└── Time Series
       ├── Previous Value Valid → Forward Fill
       ├── Next Value Valid → Backward Fill
       ├── Linear Trend → Linear Interpolation
       └── Nonlinear Trend → Spline Interpolation

================================================================================

</pre>