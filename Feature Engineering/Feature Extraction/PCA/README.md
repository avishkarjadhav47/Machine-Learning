# PCA + Dimensionality Reduction Final Revision Notes

--------------------------------------------------
1. Dimensionality
--------------------------------------------------

- Dimensions = Number of features/columns
- More features -> Higher dimensional space

--------------------------------------------------
2. Curse of Dimensionality
--------------------------------------------------

When number of features increases:
- model performance decreases
- computation increases
- overfitting increases
- data becomes sparse

--------------------------------------------------
3. Dimensionality Reduction
--------------------------------------------------

Reducing number of features while preserving important information.

Benefits:
- Faster training
- Less storage
- Better generalization
- Reduced overfitting

--------------------------------------------------
4. Types of Dimensionality Reduction
--------------------------------------------------

A. Feature Selection
- Select important existing columns
- Removes useless features

Example:
- Remove Phone Number column

B. Feature Extraction
- Create new features from old features
- Transform original feature space

Example:
- PCA

--------------------------------------------------
5. PCA (Principal Component Analysis)
--------------------------------------------------

- Unsupervised ML algorithm
- Feature Extraction technique
- Used for Dimensionality Reduction

Goal:
- Reduce dimensions
- Preserve maximum variance

--------------------------------------------------
6. Principal Components
--------------------------------------------------

- New transformed axes/features
- Combination of original features

Important:
- PC1 -> Maximum variance
- PC2 -> Second maximum variance

--------------------------------------------------
7. Core Idea of PCA
--------------------------------------------------

PCA:
- rotates coordinate axes
- finds direction of maximum spread
- projects data onto best directions

--------------------------------------------------
8. Variance
--------------------------------------------------

Variance measures:
- spread of data

Higher variance:
- more information preserved

Formula:

Var(X) = (1/n) * Σ(xi - μ)^2

--------------------------------------------------
9. Covariance
--------------------------------------------------

Covariance measures:
- relationship between variables

Positive Covariance:
- Both increase together

Negative Covariance:
- One increases, other decreases

Formula:

Cov(X,Y) = (1/n) * Σ(xi - x̄)(yi - ȳ)

--------------------------------------------------
10. Covariance Matrix
--------------------------------------------------

Contains:
- variances
- covariances

For 2 features:

| Var(X1)       Cov(X1,X2) |
| Cov(X2,X1)   Var(X2)     |

--------------------------------------------------
11. Eigenvectors & Eigenvalues
--------------------------------------------------

Eigenvector:
- Direction remains unchanged after transformation

Eigenvalue:
- Amount of stretching/compression

Equation:

Av = λv

Where:
A = matrix
v = eigenvector
λ = eigenvalue

--------------------------------------------------
12. PCA Important Fact
--------------------------------------------------

- Eigenvectors of covariance matrix = Principal Components
- Largest eigenvalue -> PC1

--------------------------------------------------
13. PCA Working Steps
--------------------------------------------------

Step 1:
- Standardize / Mean center data

Step 2:
- Compute covariance matrix

Step 3:
- Find eigenvalues & eigenvectors

Step 4:
- Sort by descending eigenvalues

Step 5:
- Select top principal components

Step 6:
- Transform/project data

--------------------------------------------------
14. PCA Transformation
--------------------------------------------------

Xnew = XW

Where:
X = original data
W = principal components

--------------------------------------------------
15. Why Scaling Before PCA?
--------------------------------------------------

PCA is variance-based.

Large-scale features dominate variance.

So:
- always use StandardScaler before PCA

--------------------------------------------------
16. Explained Variance Ratio
--------------------------------------------------

Tells:
- how much variance each PC explains

In sklearn:

pca.explained_variance_ratio_

--------------------------------------------------
17. Choosing Number of Components
--------------------------------------------------

Use:
- cumulative explained variance

Rule:
- retain ~90% variance

--------------------------------------------------
18. Scree Plot
--------------------------------------------------

Graph:
- Number of PCs vs Explained Variance

Used to find:
- optimal components

--------------------------------------------------
19. PCA Benefits
--------------------------------------------------

- Faster computation
- Reduces dimensions
- Better visualization
- Removes redundancy
- Helps KNN/Clustering

--------------------------------------------------
20. PCA Limitations
--------------------------------------------------

PCA fails when:
- all directions have similar variance
- data heavily overlaps
- nonlinear patterns exist

Example:
y = x^2

PCA is:
- linear technique

--------------------------------------------------
21. Important Placement Questions
--------------------------------------------------

Q. What is PCA?
Ans:
Technique for reducing dimensions while preserving maximum variance.

Q. PCA is supervised or unsupervised?
Ans:
Unsupervised.

Q. PCA is Feature Selection or Feature Extraction?
Ans:
Feature Extraction.

Q. What does PCA maximize?
Ans:
Variance.

Q. Why covariance matrix is used?
Ans:
To capture spread + feature relationships.

Q. Why scaling before PCA?
Ans:
PCA is sensitive to feature scales.

Q. What are principal components?
Ans:
Eigenvectors of covariance matrix.

Q. What determines importance of PC?
Ans:
Eigenvalue magnitude.

Q. Why PCA helps KNN?
Ans:
Lower dimensions -> Faster distance calculations.

--------------------------------------------------
22. Super Short Final Revision
--------------------------------------------------

- Dimensions = number of features
- Too many features -> Curse of dimensionality
- PCA = Feature Extraction + Dimensionality Reduction
- PCA creates Principal Components
- PC1 has maximum variance
- Variance = spread of data
- Covariance = relation between variables
- Principal Components = eigenvectors
- Largest eigenvalue -> most important PC
- Always scale before PCA
- Use explained variance ratio to choose PCs
- Keep ~90% variance
- PCA is linear technique