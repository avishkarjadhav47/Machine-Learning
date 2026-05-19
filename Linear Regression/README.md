# =========================================================
# LINEAR REGRESSION ECOSYSTEM
# =========================================================


# =========================================================
# 1. MODELS (Feature Structure)
# =========================================================

models = {
    "SLR": "Simple Linear Regression",
    "MLR": "Multiple Linear Regression",
    "PR":  "Polynomial Regression"
}


# =========================================================
# 2. OBJECTIVES / LOSS FUNCTIONS
# =========================================================

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


# =========================================================
# 3. SOLVERS / OPTIMIZATION METHODS
# =========================================================

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


# =========================================================
# 4. SKLEARN MODEL MAPPING
# =========================================================

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