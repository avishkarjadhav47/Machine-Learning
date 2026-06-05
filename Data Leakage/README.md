<pre>
========================================
DATA LEAKAGE
========================================

Definition:
Data leakage happens when model gets
information during training that would
not be available at prediction time.

Result:
Artificially high performance.

========================================
WAYS DATA LEAKAGE OCCURS
========================================

1. Target Leakage
-----------------

Feature directly/indirectly reveals target.

Example:
Predict Loan Default

Feature:
"Loan Approved Status"

Model indirectly sees answer.


2. Train-Test Contamination
---------------------------

Preprocessing done before train-test split.

Wrong:

scaler.fit(X)

Correct:

scaler.fit(X_train)

Affected Operations:
- Scaling
- Encoding
- PCA
- Imputation
- Feature Selection


3. Improper Cross Validation
----------------------------

Preprocessing outside CV loop.

Wrong:
Scale entire dataset before CV.

Correct:
Preprocessing should happen
inside each fold.


4. Duplicate / Overlapping Data
-------------------------------

Same or nearly same rows appear
in train and test data.

Result:
Model memorizes data.


5. Time Leakage
---------------

Future information used to predict past.

Common in:
- Stock prediction
- Forecasting


6. Hyperparameter Tuning Leakage
--------------------------------

Using test data repeatedly
during tuning process.

Solution:
Nested Cross Validation.


========================================
HOW TO DETECT DATA LEAKAGE
========================================

1. Unexpectedly High Performance
--------------------------------

Example:
Accuracy = 99%

Too good to be true.


2. Huge Gap Between Validation
   and Real-World Performance
--------------------------------

Validation Accuracy:
98%

Production Accuracy:
65%


3. Feature Importance Analysis
------------------------------

Suspiciously powerful feature.

Example:
Feature indirectly reveals target.


4. Manual Feature Inspection
----------------------------

Check whether feature would
actually be available during prediction.


========================================
HOW TO PREVENT DATA LEAKAGE
========================================

1. Proper Train-Test Split
--------------------------

Split data BEFORE preprocessing.


2. Fit Preprocessing ONLY
   on Training Data
--------------------------

Correct:

scaler.fit(X_train)

Wrong:

scaler.fit(X)


3. Use Pipelines
----------------

Pipelines automatically reduce leakage.


4. Careful Feature Selection
----------------------------

Remove:
- future information
- target revealing columns


5. Proper Cross Validation
--------------------------

Preprocessing must happen
inside CV folds.


6. Use Separate Test Set
------------------------

Never repeatedly tune on test data.


========================================
IMPORTANT INTERVIEW LINE
========================================

Data leakage causes overly optimistic
performance estimates and poor
real-world generalization.
</pre>