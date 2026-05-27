<pre>
========================================================
         REGRESSION EVALUATION METRICS
========================================================

WHY EVALUATION METRICS?
--------------------------------------------------------
Used to:
- Measure model performance
- Measure prediction error
- Compare models

Main Metrics:
1. MAE
2. MSE
3. RMSE
4. R² Score
5. Adjusted R²
6. MAPE
7. RMSLE
8. Median Absolute Error
9. Huber Loss

========================================================
1. MAE (Mean Absolute Error)
========================================================

Formula:
MAE = (1/n) * Σ|yi - ŷi|

Definition:
- Average absolute prediction error

Advantages:
- Easy to understand
- Same unit as target
- Robust to outliers

Disadvantages:
- Not differentiable at 0
- Large errors not penalized heavily

Use Cases:
- Business problems
- Outlier datasets

Key Point:
- Lower MAE = Better

--------------------------------------------------------

2. MSE (Mean Squared Error)
========================================================

Formula:
MSE = (1/n) * Σ(yi - ŷi)^2

Definition:
- Average squared error

Advantages:
- Differentiable
- Good for Gradient Descent
- Penalizes large errors heavily

Disadvantages:
- Sensitive to outliers
- Squared unit problem

Use Cases:
- ML optimization
- Linear Regression loss function

Key Point:
- Lower MSE = Better

--------------------------------------------------------

3. RMSE (Root Mean Squared Error)
========================================================

Formula:
RMSE = √[(1/n) * Σ(yi - ŷi)^2]

Definition:
- Square root of MSE

Advantages:
- Same unit as target
- Easy interpretation
- Industry standard

Disadvantages:
- Sensitive to outliers

Use Cases:
- Forecasting
- General regression tasks

Key Point:
- Lower RMSE = Better

--------------------------------------------------------

MAE vs MSE vs RMSE
========================================================

MAE:
- Robust to outliers
- Equal error treatment

MSE:
- Penalizes large errors heavily
- Differentiable

RMSE:
- Same unit as target
- Most interpretable

Rule:
- Outliers present → MAE
- Large error costly → MSE/RMSE

========================================================
4. R² Score (Coefficient of Determination)
========================================================

Formula:
R² = 1 - (SSres / SStot)

Definition:
- Measures explained variance

Range:
- Usually 0 → 1

Interpretation:
- R² = 1 → Perfect model
- R² = 0 → Predicting mean only
- R² < 0 → Very poor model

Advantages:
- Easy interpretation
- Scale independent

Disadvantages:
- Increases with useless features

Key Point:
- Higher R² = Better

--------------------------------------------------------

5. Adjusted R²
========================================================

Formula:
Adjusted R² = 1 - (1-R²)(n-1)/(n-p-1)

Definition:
- Penalized R²

Advantages:
- Penalizes useless features
- Better for Multiple Regression

Disadvantages:
- Slightly harder interpretation

Use Cases:
- Multiple Linear Regression
- Feature selection

Key Point:
- Preferred over R² in MLR

========================================================
6. MAPE (Mean Absolute Percentage Error)
========================================================

Formula:
MAPE = (100/n) * Σ|(yi - ŷi)/yi|

Definition:
- Percentage prediction error

Advantages:
- Business friendly
- Easy interpretation

Disadvantages:
- Undefined when actual value = 0

Use Cases:
- Sales forecasting

Key Point:
- Lower MAPE = Better

========================================================
7. RMSLE (Root Mean Squared Log Error)
========================================================

Formula:
RMSLE = √[(1/n) * Σ(log(yi+1)-log(ŷi+1))²]

Definition:
- Log-based error metric

Advantages:
- Good for growth prediction
- Reduces effect of huge values

Disadvantages:
- Cannot handle negative targets

Use Cases:
- Population growth
- Sales growth
- Kaggle competitions

Key Point:
- Penalizes underestimation more

========================================================
8. Median Absolute Error
========================================================

Definition:
- Median of absolute errors

Advantages:
- Extremely robust to outliers

Disadvantages:
- Ignores full error distribution

Use Cases:
- Heavy outlier datasets

========================================================
9. Huber Loss
========================================================

Definition:
- Combination of MAE + MSE

Behavior:
- Small errors → MSE
- Large errors → MAE

Advantages:
- Less sensitive to outliers
- Differentiable

Disadvantages:
- More complex
- Threshold tuning required

Use Cases:
- Moderate outlier datasets

========================================================
IMPORTANT INTERVIEW COMPARISONS
========================================================

MAE vs RMSE
-------------------------
MAE:
- Robust to outliers

RMSE:
- Penalizes large errors heavily

--------------------------------------------------------

R² vs Adjusted R²
-------------------------
R²:
- Always increases with features

Adjusted R²:
- Penalizes useless features

========================================================
MOST IMPORTANT PLACEMENT POINTS
========================================================

- MSE preferred in ML because differentiable
- RMSE preferred in reports because same unit
- MAE robust to outliers
- R² can become negative
- Adjusted R² important in MLR

========================================================
MEMORY TRICKS
========================================================

MAE   → Average mistake
MSE   → Squared penalty
RMSE  → Error in original unit
R²    → Variance explained
AdjR² → Penalizes useless features
MAPE  → Percentage error
RMSLE → Growth metric
Huber → MAE + MSE hybrid

========================================================
SKLEARN CODE
========================================================

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test,y_pred)

mse = mean_squared_error(y_test,y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test,y_pred)

print(mae)
print(mse)
print(rmse)
print(r2)

========================================================
</pre>