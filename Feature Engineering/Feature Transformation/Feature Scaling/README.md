# FEATURE SCALING NOTES

## Definition
Feature Scaling = Bringing all independent features into similar range.

Purpose:
- Prevent domination of large-value features
- Improve ML model performance

---

# Why Feature Scaling Needed?

Some ML algorithms depend on:
- Distance calculation
- Gradient updates
- Variance

Example:
Salary = 4,00,000
Age = 25

Salary dominates distance calculations.

---

# Types of Feature Scaling

1. Standardization
2. Normalization

---

# STANDARDIZATION (Z-SCORE SCALING)

## Formula

```math
z = \frac{x-\mu}{\sigma}
```

Where:
- x = value
- μ = mean
- σ = standard deviation

---

## Properties
- Mean = 0
- Standard deviation = 1
- Distribution shape remains same

---

## Algorithms Where Standardization Important
- KNN
- K-Means
- PCA
- Linear Regression
- Logistic Regression
- Neural Networks
- Deep Learning

---

## Algorithms Where Standardization NOT Required
- Decision Tree
- Random Forest
- XGBoost

Reason:
Tree algorithms compare values instead of distances.

---

# NORMALIZATION (MIN-MAX SCALING)

## Formula

```math
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
```

---

## Properties
- Values lie between 0 and 1
- Sensitive to outliers

---

## Used In
- Image Processing
- CNN
- Fixed-range data

Example:
Pixel values = 0 to 255

---

# MEAN NORMALIZATION

## Formula

```math
x' = \frac{x-\bar{x}}{x_{max}-x_{min}}
```

Properties:
- Mean centering
- Usually range between -1 and 1

Rarely used.

---

# MAX ABS SCALING

## Formula

```math
x' = \frac{x}{|x_{max}|}
```

Used for:
- Sparse datasets
- Many zero values

---

# ROBUST SCALING

## Formula

```math
x' = \frac{x-\text{Median}}{IQR}
```

Where:

```math
IQR = Q3 - Q1
```

Used when:
- Dataset has many outliers

---

# STANDARDIZATION vs NORMALIZATION

| Standardization | Normalization |
|---|---|
| Mean = 0 | Range = [0,1] |
| Std = 1 | Uses Min-Max |
| Most commonly used | Used for fixed-range data |
| Better for Gradient Descent | Better for image data |

---

# IMPORTANT ML RULE

Always:
1. Train-test split first
2. Fit scaler only on training data
3. Transform both train and test

---

# Correct Workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

scaler = StandardScaler()

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

# Important Interview Points

## Scaling improves:
- Model convergence
- Optimization
- Distance calculations

---

## Scaling does NOT remove outliers.

Handle outliers separately.

---

## Logistic Regression benefits heavily from scaling.

---

## Tree-based algorithms usually unaffected by scaling.

---

# Practical Placement Tips

## If confused:
Use Standardization first.

---

## Use Normalization when:
- Data range fixed
- Image processing
- CNN inputs

---

## Use Robust Scaling when:
- Outliers present

---

## Use MaxAbs Scaling when:
- Sparse matrix
- Many zeros

---

# One-Line Definitions

## Feature Scaling
Bringing features into similar range.

## Standardization
Transforms data so mean = 0 and std = 1.

## Normalization
Transforms data into fixed range (usually 0–1).

---

# MOST IMPORTANT FORMULAS

## Standardization

```math
z = \frac{x-\mu}{\sigma}
```

---

## Min-Max Scaling

```math
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
```

---

## Robust Scaling

```math
x' = \frac{x-\text{Median}}{IQR}
```