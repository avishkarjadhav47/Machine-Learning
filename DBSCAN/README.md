<pre>

DBSCAN (Density Based Spatial Clustering of Applications with Noise)

--------------------------------------------------
1. WHY DBSCAN?
--------------------------------------------------

Problems with K-Means:
1. Need to specify K beforehand.
2. Cannot handle arbitrary/non-spherical clusters well.
3. Sensitive to outliers.

DBSCAN Solution:
- Finds clusters based on density.
- No need to specify number of clusters.
- Automatically identifies outliers/noise.
- Can detect arbitrary-shaped clusters.

--------------------------------------------------
2. CORE IDEA
--------------------------------------------------

Dense Region  = Cluster
Sparse Region = Separation between clusters

DBSCAN groups points that are densely packed together
and marks isolated points as noise.

--------------------------------------------------
3. HYPERPARAMETERS
--------------------------------------------------

1. Epsilon (ε)
   = Radius around a point.

2. MinPts
   = Minimum number of points required inside ε
     neighbourhood to consider region dense.

Memory Trick:
ε  -> How far to look?
MinPts -> How many points needed?

--------------------------------------------------
4. POINT TYPES
--------------------------------------------------

A. Core Point
--------------
Point having >= MinPts points within ε radius.

Example:
MinPts = 4

If neighbours = 5
→ Core Point

If neighbours = 7
→ Core Point

B. Border Point
---------------
1. Not a Core Point
2. Lies inside ε radius of a Core Point

Example:
Neighbours = 2 (< MinPts)
but inside core point neighbourhood

→ Border Point

C. Noise Point
--------------
Neither Core nor Border.

Completely isolated point.

→ Outlier

--------------------------------------------------
5. DENSITY RELATIONS
--------------------------------------------------

A. Directly Density Reachable
-----------------------------

P is directly density reachable from Q if:

1. P lies inside ε neighbourhood of Q
2. Q is a Core Point

Simple Meaning:
"One hop reachable from a core point"

B. Density Connected
--------------------

P and Q are density connected if there exists
a chain of directly density reachable points
connecting them.

P → A → B → C → Q

Same cluster.

Simple Meaning:
"Connected through a chain of dense points"

--------------------------------------------------
6. DBSCAN ALGORITHM
--------------------------------------------------

Step 1:
Identify each point as:
- Core
- Border
- Noise

Step 2:
For every unclustered Core Point:
    Create New Cluster

Step 3:
Add all density-connected points
to that cluster.

Step 4:
Assign Border Points to nearest
Core Point's cluster.

Step 5:
Leave Noise Points as Noise.

--------------------------------------------------
7. K-MEANS VS DBSCAN
--------------------------------------------------

Feature               K-Means          DBSCAN

Need K?               Yes              No

Cluster Shape         Spherical        Arbitrary

Outlier Handling      Poor             Excellent

Noise Detection       No               Yes

Non-linear Clusters   Poor             Good

Prediction on New     Yes              No
Data

Hyperparameters       K                ε, MinPts

--------------------------------------------------
8. ADVANTAGES
--------------------------------------------------

1. Robust to outliers.
2. No need to specify number of clusters.
3. Finds arbitrary shaped clusters.
4. Only two hyperparameters.
5. Excellent for spatial data.

--------------------------------------------------
9. LIMITATIONS
--------------------------------------------------

1. Sensitive to ε and MinPts selection.
2. Struggles when clusters have different densities.
3. Does not naturally support prediction
   for new unseen points.

One Liner:
"DBSCAN is a clustering algorithm,
not a predictive model."

--------------------------------------------------
10. WHEN TO USE DBSCAN?
--------------------------------------------------

Use DBSCAN when:

✓ Number of clusters unknown
✓ Outliers exist
✓ Non-spherical clusters exist
✓ Density-based grouping required

Avoid when:

✗ Cluster densities vary heavily
✗ Prediction required
✗ Dataset is very high-dimensional

--------------------------------------------------
11. REAL WORLD APPLICATIONS
--------------------------------------------------

1. Anomaly/Fraud Detection
2. Customer Segmentation
3. GIS & Spatial Analysis
4. Image Segmentation
5. Bioinformatics
6. Traffic Analysis
7. Social Network Community Detection
8. Astronomy
9. Environmental Monitoring

--------------------------------------------------
12. IMP QUESTIONS
--------------------------------------------------

Q1. Why DBSCAN over K-Means?
Ans:No need of K, handles outliers,
finds arbitrary shapes.

Q2. What are DBSCAN hyperparameters?
Ans:Epsilon (ε) and MinPts.

Q3. Difference between Core and Border Point?
Ans:Core has >= MinPts neighbours.
    Border has < MinPts neighbours but
    lies near a Core Point.

Q4. What is a Noise Point?
Ans:Neither Core nor Border.

Q5. Can DBSCAN detect outliers?
Ans:Yes, noise points are treated as outliers.

Q6. Biggest drawback?
Ans:Sensitive to ε and MinPts and
    fails with varying density clusters.


</pre>