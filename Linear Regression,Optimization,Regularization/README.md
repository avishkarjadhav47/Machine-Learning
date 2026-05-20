
# LINEAR REGRESSION ECOSYSTEM




# 1. MODELS (Feature Structure)


models = {
    "SLR": "Simple Linear Regression",
    "MLR": "Multiple Linear Regression",
    "PR":  "Polynomial Regression"
}



# 2. OBJECTIVES / LOSS FUNCTIONS


objectives = {

    "OLS": {
        "formula": "min ||y - Xb||^2",
        "regularization": None
    },

    "Ridge": {
        "formula": "min ||y - Xb||^2 + λ||b||²",
        "regularization": "L2"
    },

    "Lasso": {
        "formula": "min ||y - Xb||^2 + λ||b||₁",
        "regularization": "L1"
    },

    "ElasticNet": {
        "formula": "min ||y - Xb||^2 + λ1||b||₁ + λ2||b||²",
        "regularization": "L1 + L2"
    }
}



# 3. SOLVERS / OPTIMIZATION METHODS


solvers = {

    # -----------------------------
    # Gradient-based Optimizers
    # -----------------------------
    "GD": "Gradient Descent",

    "BGD": "Batch Gradient Descent",

    "SGD": "Stochastic Gradient Descent",

    "MBGD": "Mini Batch Gradient Descent",

    "SAG": "Stochastic Average Gradient",

    "SAGA": "Improved SAG Variant",

    "LBFGS": "Limited-memory BFGS",


    # -----------------------------
    # Coordinate-wise Optimizer
    # -----------------------------
    "CoordinateDescent": "Coordinate Descent",


    # -----------------------------
    # Iterative Linear Solver
    # -----------------------------
    "LSQR": "Least Squares QR",


    # -----------------------------
    # Matrix Decomposition Solvers
    # -----------------------------
    "SVD": "Singular Value Decomposition",

    "QR": "QR Decomposition",

    "Cholesky": "Cholesky Decomposition"
}



# 4. SKLEARN MODEL MAPPING


sklearn_models = {

    "LinearRegression": {
        "objective": "OLS",
        "regularization": None,
        "default_solver": "SVD"
    },

    "Ridge": {
        "objective": "OLS + L2",
        "regularization": "L2",
        "possible_solvers": [
            "SVD",
            "Cholesky",
            "LSQR",
            "SAG",
            "SAGA",
            "LBFGS"
        ]
    },

    "Lasso": {
        "objective": "OLS + L1",
        "regularization": "L1",
        "default_solver": "CoordinateDescent"
    },

    "ElasticNet": {
        "objective": "OLS + L1 + L2",
        "regularization": "L1 + L2",
        "default_solver": "CoordinateDescent"
    },

    "SGDRegressor": {
        "objective": "Configurable",
        "regularization": [
            "None",
            "L1",
            "L2",
            "ElasticNet"
        ],
        "solver": "SGD"
    }
}

# Regression Metrics Notes for Placements

# 1. MAE (Mean Absolute Error)

Formula:
MAE = (1/n) * Σ|yi - ŷi|

## Advantages

* Easy to understand
* Same unit as target variable
* Robust to outliers compared to MSE
* Treats all errors equally

## Disadvantages

* Not differentiable at zero
* Does not heavily penalize large errors

## When to Use

* When interpretability matters
* When outliers should not dominate
* Real-world business problems

## When to Avoid

* When large errors are very costly

## Important Points

* Lower MAE is better
* Unit same as target variable

---

# 2. MSE (Mean Squared Error)

Formula:
MSE = (1/n) * Σ(yi - ŷi)^2

## Advantages

* Differentiable
* Works very well with Gradient Descent
* Penalizes large errors heavily

## Disadvantages

* Very sensitive to outliers
* Unit becomes squared

## When to Use

* ML optimization problems
* When large errors must be penalized strongly

## When to Avoid

* Datasets with many outliers

## Important Points

* Lower MSE is better
* Most commonly used loss function in ML

---

# 3. RMSE (Root Mean Squared Error)

Formula:
RMSE = √MSE

## Advantages

* Same unit as target variable
* Penalizes large errors
* Widely used in industry

## Disadvantages

* Sensitive to outliers
* More affected by large errors than MAE

## When to Use

* General regression evaluation
* Forecasting problems
* Industry applications

## When to Avoid

* Extreme outlier-heavy datasets

## Important Points

* Lower RMSE is better
* Easier to interpret than MSE

---

# 4. R² Score (Coefficient of Determination)

Formula:
R² = 1 - (SSE/SST)

## Advantages

* Easy interpretation
* Measures goodness of fit
* Scale independent

## Disadvantages

* Always increases when features are added
* Cannot determine overfitting alone

## When to Use

* Regression model evaluation
* Comparing regression models

## When to Avoid

* As sole evaluation metric

## Important Points

* Higher R² is better
* R² = 1 → perfect fit
* R² = 0 → model predicts mean only
* R² can be negative

---

# 5. Adjusted R²

Formula:
Adjusted R² = 1 - (1-R²)(n-1)/(n-p-1)

## Advantages

* Penalizes unnecessary features
* Better for multiple regression
* Helps detect overfitting

## Disadvantages

* Slightly harder to interpret

## When to Use

* Multiple Linear Regression
* Feature selection

## When to Avoid

* Simple regression with very few features

## Important Points

* Can decrease when irrelevant features are added
* Preferred over R² in MLR

---

# 6. MAPE (Mean Absolute Percentage Error)

Formula:
MAPE = (100/n) * Σ|(yi - ŷi)/yi|

## Advantages

* Percentage interpretation
* Easy for business understanding

## Disadvantages

* Undefined when actual value = 0
* Sensitive to very small actual values

## When to Use

* Sales forecasting
* Business analytics

## When to Avoid

* Data containing zeros

## Important Points

* Lower MAPE is better
* Expressed in percentage

---

# 7. RMSLE (Root Mean Squared Log Error)

Formula:
RMSLE = √[(1/n) * Σ(log(yi+1)-log(ŷi+1))²]

## Advantages

* Handles exponential growth well
* Reduces impact of large values

## Disadvantages

* Difficult interpretation
* Cannot handle negative values

## When to Use

* Growth prediction
* Kaggle competitions
* Population/sales growth

## When to Avoid

* Negative target values

## Important Points

* Penalizes underestimation more
* Useful when relative error matters

---

# 8. Median Absolute Error

## Advantages

* Extremely robust to outliers
* Simple interpretation

## Disadvantages

* Ignores distribution of errors
* Less smooth for optimization

## When to Use

* Heavy outlier datasets

## When to Avoid

* When large errors matter strongly

## Important Points

* Uses median instead of mean
* Very stable metric

---

# 9. Huber Loss

## Advantages

* Combines benefits of MAE and MSE
* Less sensitive to outliers than MSE
* Differentiable

## Disadvantages

* More complex
* Requires threshold tuning

## When to Use

* Datasets with moderate outliers

## When to Avoid

* Very simple regression tasks

## Important Points

* Behaves like:

  * MSE for small errors
  * MAE for large errors

---

# Important Interview Comparisons

## MAE vs RMSE

MAE:

* Treats all errors equally
* More robust to outliers

RMSE:

* Penalizes large errors heavily
* Sensitive to outliers

---

## R² vs Adjusted R²

R²:

* Never decreases with new features

Adjusted R²:

* Penalizes unnecessary features
* Better for feature selection

---

# Most Important Placement Points

1. MSE preferred in ML because it is differentiable.

2. RMSE preferred in reports because unit remains same as target variable.

3. MAE and Median Absolute Error are robust to outliers.

4. R² can become negative if model performs worse than predicting mean.

5. Adjusted R² is important in Multiple Linear Regression.

6. Feature scaling does not affect tree models but affects distance-based and gradient-based models.

7. Always explain:

* intuition
* outlier sensitivity
* higher/lower is better
  during interviews.
