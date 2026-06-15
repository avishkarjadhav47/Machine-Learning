"""

MACHINE LEARNING PROJECT WORKFLOW
│
├── 1. BUSINESS PROBLEM UNDERSTANDING
│   │
│   ├── Problem Statement
│   ├── ML Objective
│   │   ├── Regression
│   │   ├── Classification
│   │   ├── Clustering
│   │   └── Recommendation
│   │
│   ├── Success Metrics
│   └── Business Constraints
│
├── 2. DATA COLLECTION & DATA UNDERSTANDING
│   │
│   ├── Data Collection Sources
│   │   ├── CSV
│   │   ├── SQL Databases
│   │   ├── API
│   │   ├── Web Scraping
│   │   └── Sensors
│   │
|   |── Data Understanding
│       ├── Data Dictionary
│       ├── Feature Understanding
│       ├── Target Variable
│       └── Data Types
│
├── 3. EXPLORATORY DATA ANALYSIS (EDA)
│   │
│   ├── Dataset Shape
│   ├── Data Types Analysis
│   ├── Missing Value Analysis
│   ├── Duplicate Analysis
│   ├── Outlier Analysis
│   ├── Univariate Analysis
│   ├── Bivariate Analysis
│   ├── Multivariate Analysis
│   ├── Correlation Analysis
│   ├── Target Variable Analysis
│   ├── Class Imbalance Analysis
│   └── Visualization
│
├── 4. TRAIN / VALIDATION / TEST SPLIT
│   │
│   ├── Hold-Out Split
│   ├── Stratified Split
│   └── Time Series Split
│
├── 5. DATA PREPROCESSING
│   │
│   ├── Missing Value Handling
│   │   ├── Mean
│   │   ├── Median
│   │   └── Mode
│   │
│   ├── Duplicate Removal
│   │
│   ├── Outlier Treatment
│   │   ├── IQR
│   │   └── Z-Score
│   │
│   ├── Class Imbalance Handling
│   │   ├── Random Oversampling
│   │   ├── Random Undersampling
│   │   ├── SMOTE
│   │   ├── ADASYN
│   │   └── Class Weights
│   │
│   ├── Encoding
│   │   ├── One Hot Encoding
│   │   ├── Ordinal Encoding
│   │   └── Label Encoding
│   │
│   ├── Feature Scaling
│   │   ├── Standardization
│   │   ├── Normalization
│   │   └── Robust Scaling
│   │
│   └── Data Transformation
│       ├── Log Transform
│       ├── Box-Cox
│       └── Yeo-Johnson
│
├── 6. FEATURE ENGINEERING
│   │
│   ├── Feature Construction
│   ├── Feature Splitting
│   ├── Date Feature Extraction
│   ├── Binning
│   ├── Interaction Features
│   └── Domain Features
│
├── 7. FEATURE SELECTION
│   │
│   ├── Filter Methods
│   │   ├── Correlation
│   │   ├── Chi-Square
│   │   └── ANOVA
│   │
│   ├── Wrapper Methods
│   │   ├── Forward Selection
│   │   ├── Backward Elimination
│   │   └── RFE
│   │
│   └── Embedded Methods
│       ├── Lasso
│       ├── Ridge
│       └── Tree Based Importance
│
├── 8. MODEL BUILDING
│   │
│   ├── Algorithm Selection
│   ├── Model Training
│   ├── Baseline Model
│   └── Model Comparison
│
├── 9. HYPERPARAMETER TUNING
│   │
│   ├── Grid Search
│   ├── Random Search
│   ├── Bayesian Optimization
│   └── Cross Validation
│
├── 10. MODEL EVALUATION
│   │
│   ├── Regression Metrics
│   │   ├── MAE
│   │   ├── MSE
│   │   ├── RMSE
│   │   └── R²
│   │
│   ├── Classification Metrics
│   │   ├── Accuracy
│   │   ├── Precision
│   │   ├── Recall
│   │   ├── F1 Score
│   │   ├── ROC-AUC
│   │   └── Confusion Matrix
│   │
│   ├── Bias-Variance Analysis
│   ├── Error Analysis
│  
├── 11. MODEL INTERPRETATION
│   │
│   ├── Feature Importance
│   │
│   ├── SHAP
│   │   ├── SHAP Summary Plot
│   │   ├── SHAP Dependence Plot
│   │   └── SHAP Force Plot
│   │
│   ├── LIME
│   │
│   ├── Partial Dependence Plot (PDP)
│   │
│   ├── Individual Conditional Expectation (ICE)
│   │
│   └── Permutation Importance
│
└── 12. MLOPS
└─────────────────────────────────────────────

MAIN ITERATION LOOP

    5. Data Preprocessing
            ↓
    6. Feature Engineering
            ↓
    7. Feature Selection
            ↓
    8. Model Building
            ↓
    9. Hyperparameter Tuning
            ↓
   10. Model Evaluation
            ↓
      Satisfied?
      │
      ├── YES → Final Model
      │
      └── NO
            ↓
      Go Back To:
      ├── Preprocessing
      ├── Feature Engineering
      ├── Feature Selection
      ├── Model Building
      └── Hyperparameter Tuning

─────────────────────────────────────────────

INTERVIEW ONE-LINER

Steps 1-4 → Understand Data
Steps 5-7 → Prepare Features
Steps 8-10 → Build, Tune & Evaluate Model

Most ML work happens inside the loop:
Preprocessing → Engineering → Selection →
Modeling → Tuning → Evaluation
until performance becomes satisfactory.

"""


"""
================================================================================
FINAL BOSS: CORE ML EXPERIMENTATION & MODELING WORKFLOW


MACHINE LEARNING PROJECT WORKFLOW
│
├── 1. BUSINESS PROBLEM UNDERSTANDING
│   │
│   ├── Problem Statement
│   ├── ML Objective
│   │   ├── Regression
│   │   ├── Classification
│   │   ├── Clustering
│   │   └── Recommendation
│   │
│   ├── Success Metrics (Business KPIs vs. Optimization Loss)
│   └── Business Constraints (Compute, Memory, SLA Latency Targets)
│
├── 2. DATA COLLECTION & DATA UNDERSTANDING
│   │
│   ├── Data Collection Sources (CSV, SQL Databases, APIs, Web Scraping, Streams)
│   └── Data Understanding
│       ├── Data Dictionary Definition
│       ├── Feature Typology Identification (Nominal, Ordinal, Continuous, Discrete)
│       ├── Target Variable Characteristics
│       └── Base Data Types (Tabular, Text, Image, Audio, Graph, Time-Series)
│
├── 3. EXPLORATORY DATA ANALYSIS (EDA)
│   │
│   ├── Dataset Shape & Dimensionality Audit
│   ├── Descriptive Statistical Data Type Analysis
│   ├── Missing Value & Null Pattern Analysis
│   ├── Duplicate Rows & Key Multiplicity Analysis
│   ├── Outlier Boxplot & Z-Score Anomaly Analysis
│   ├── Univariate Analysis (Individual Feature Skewness, Variance, Sparsity)
│   ├── Bivariate Analysis (Feature-to-Feature & Feature-to-Target relationships)
│   ├── Multivariate Analysis & Interaction Maps
│   ├── Multicollinearity Verification (Pearson/Spearman Matrices & VIF)
│   ├── Target Variable Distribution Properties
│   ├── Class Imbalance Severity Assessment
│   └── Statistical Visualizations (Histograms, Scatter Plots, Heatmaps)
│
├── 4. TRAIN / VALIDATION / TEST SPLIT  # <-- 🔥 THE INVIOLABLE FENCE ERECTED HERE
│   │
│   ├── Hold-Out Split (Standard IID Data)
│   ├── Stratified Split (Imbalanced Class Preservation)
│   └── Time Series Split (Ordered Sequential Constraints - No Future Lookahead)
│
├── 5. DATA PREPROCESSING (Calculated STRICTLY from the Train Split to prevent leakage)
│   │
│   ├── Missing Value Handling
│   │   ├── Statistical Imputation (Mean / Median / Mode)
│   │   ├── Constant Flag Assignment (e.g., Missing Category, -999)
│   │   └── Advanced Multivariant Approximation (MICE, KNN Imputer)
│   │
│   ├── Duplicate Removal
│   │
│   ├── Outlier Treatment
│   │   ├── IQR Filtering (Interquartile Range Trimming)
│   │   └── Winsorization (Percentile Clipping)
│   │
│   ├── Class Imbalance Handling (Applied ONLY to the training partition)
│   │   ├── Random Oversampling & Random Undersampling
│   │   ├── Synthetic Minority Over-sampling Technique (SMOTE)
│   │   ├── Adaptive Synthetic Sampling (ADASYN)
│   │   └── Algorithm Cost-Sensitivity adjustments (Class Weights)
│   │
│   ├── Encoding Categorical Dimensions
│   │   ├── One Hot Encoding (Low Cardinality)
│   │   ├── Ordinal Encoding (Preserving Natural Ranked Orders)
│   │   ├── Label Encoding (Strictly for Target Variables)
│   │   └── Advanced Informed Methods (Target Encoding, Frequency Encoding)
│   │
│   ├── Feature Scaling
│   │   ├── Standardization (Z-Score Normalization to Mean=0, Std=1)
│   │   ├── Normalization (Min-Max Scaling to 0-1 boundaries)
│   │   └── Robust Scaling (Median & IQR Scaling resilient to remaining outliers)
│   │
│   └── Mathematical Data Transformations
│       ├── Log Transform (Fixing heavily right-skewed variables)
│       ├── Box-Cox Transformation (Requires strictly positive data)
│       └── Yeo-Johnson Transformation (Stabilizes variance for zero/negative data)
│
├── 6. FEATURE ENGINEERING (Creative, Domain-Driven Signal Optimization)
│   │
│   ├── Feature Construction (Combining continuous inputs mathematically)
|   |--Feature Extraction (Deriving new features from raw data like text, images, audio)
│   ├── Feature Splitting (Deconstructing compound strings like dirty text addresses)
│   ├── Datetime Component Extraction (Extracting Year, Month, Day, Hour, is_weekend)
│   ├── Value Binning (Converting continuous segments into discrete ordinal blocks)
│   ├── Interaction Feature Synthesis (Cross-multiplying high-signal features: X1 * X2)
│   └── Domain Features (Calculating industry metrics like Debt-to-Income, LTV)
│
├── 7. FEATURE SELECTION (Dropping noise to combat the Curse of Dimensionality)
│   │
│   ├── Filter Methods (Fast, model-agnostic statistical evaluations)
│   │   ├── Constant/Quasi-Constant Variance Thresholding
│   │   ├── Correlation Coefficient Dropping
│   │   ├── Chi-Square Test (Categorical dependence)
│   │   └── ANOVA F-Test & Mutual Information Scores
│   │
│   ├── Wrapper Methods (Iterative, model-dependent search spaces)
│   │   ├── Forward Feature Selection
│   │   ├── Backward Feature Elimination
│   │   └── Recursive Feature Elimination (RFE)
│   │
│   └── Embedded Methods (Regularized intrinsic pruning during optimization)
│       ├── Lasso (L1 Regularization driving weights to zero)
│       ├── Ridge (L2 Regularization weight shrinkage)
│       └── Tree-Based Feature Importances (Gini/Gain/Permutation metrics)
│
├── 8. MODEL BUILDING & ARCHITECTURE EVALUATION
│   │
│   ├── Spot-Checking Baseline Estimators (Simple Heuristics, DummyClassifiers)
│   ├── Model Class Training (Linear, Distance, Margin, Tree-Based, Probabilistic Families)
│   └── Model Structural Comparison Matrix
│
├── 9. HYPERPARAMETER TUNING & VALIDATION LOOP
│   │
│   ├── Cross-Validation Engine (K-Fold, Stratified K-Fold, TimeSeriesSplit Folds)
│   ├── Grid Search Optimization (Exhaustive search over predefined matrix)
│   ├── Random Search Optimization (Broad stochastic exploration)
│   └── Bayesian Optimization (Intelligent, history-guided optimization using Optuna)
│
├── 10. FINAL MODEL EVALUATION (The Final Exam on the Pristine, Untouched Test Set)
│   │
│   ├── Regression Evaluation Metrics (MAE, MSE, RMSE, R², Adjusted R²)
│   ├── Classification Evaluation Metrics (Accuracy, Precision, Recall, F1 Score, ROC-AUC, Log-Loss)
│   ├── Confusion Matrix Analysis & Financial Error Mapping
│   ├── Bias-Variance Decomposition Analysis (Underfitting vs. Overfitting Diagnosis)
│   └── Error Analysis (Manually inspecting top false positives/negatives to spot patterns)-->i.Residual Analysis (Regression) ii.Threshold Analysis (Classification)
│
└── 11. MODEL INTERPRETATION & EXPLAINABLE AI (XAI)
    │
    ├── Global Feature Importance (MDI, Permutation Importance)
    │
    ├── SHAP (Shapley Additive exPlanations - Game Theory foundations)
    │   ├── SHAP Summary Plot (Global directionality and feature impact)
    │   ├── SHAP Dependence Plot (Feature interaction insights)
    │   └── SHAP Force Plot (Instance-level individual prediction breakdown)
    │
    ├── LIME (Local Interpretable Model-agnostic Explanations - Local Surrogates)
    │
    ├── Partial Dependence Plot (PDP - Marginal effects of 1 or 2 features)
    │
    └── Individual Conditional Expectation (ICE - Per-instance trajectory visualization)

"""