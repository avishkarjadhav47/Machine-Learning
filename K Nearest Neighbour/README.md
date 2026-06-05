<pre>
## K-Nearest Neighbors (KNN)

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for classification and regression tasks. It classifies a new data point based on the majority class among its K nearest neighbors in the feature space.

### How KNN Works
1. Choose the number of neighbors (K).
2. Calculate the distance between the new data point and all training samples.
3. Select the K nearest neighbors.
4. Assign the class that appears most frequently among those neighbors.

### Advantages
- Simple and easy to understand.
- No training phase (instance-based learning).
- Effective for small and medium-sized datasets.

### Disadvantages
- Computationally expensive for large datasets.
- Sensitive to irrelevant features and outliers.
- Requires feature scaling (e.g., Standardization).

### Distance Metric
KNN commonly uses Euclidean Distance:

d(x,y) = √Σ(xi - yi)²
</pre>
