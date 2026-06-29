<pre>

HIERARCHICAL CLUSTERING 

--------------------------------------------------
1. WHAT IS HIERARCHICAL CLUSTERING?
--------------------------------------------------

Hierarchical Clustering is an unsupervised clustering
algorithm that builds a hierarchy (tree structure)
of clusters.

Output:
Dendrogram (tree-like structure)

Main Idea:
Create nested clusters and visualize how clusters
merge or split over time.

--------------------------------------------------
2. TYPES OF HIERARCHICAL CLUSTERING
--------------------------------------------------

A. Agglomerative Clustering (Bottom-Up)
---------------------------------------

Most Important for Placements

Start:
Each point = separate cluster

N points → N clusters

Process:
Merge nearest clusters repeatedly

End:
1 giant cluster

Memory Trick:
"Small → Big"


B. Divisive Clustering (Top-Down)
---------------------------------

Start:
All points in one cluster

Process:
Keep splitting clusters

End:
Each point becomes its own cluster

Memory Trick:
"Big → Small"

Less common in practice.

--------------------------------------------------
3. AGGLOMERATIVE ALGORITHM
--------------------------------------------------

Step 1:
Treat every point as separate cluster.

Step 2:
Compute distance matrix.

Step 3:
Find closest clusters.

Step 4:
Merge them.

Step 5:
Update distance matrix using linkage rule.

Step 6:
Repeat until only one cluster remains.

--------------------------------------------------
4. DENDROGRAM
--------------------------------------------------

Definition:
Tree representation showing how clusters
merge together.

Y-axis:
Distance at which clusters merge.

X-axis:
Data points.


HOW TO FIND NUMBER OF CLUSTERS?-->
Rule:
Draw a horizontal line through dendrogram.
Count how many vertical branches it cuts.
That count = Number of clusters.

Interview Line:
"Cut the dendrogram at the largest vertical gap."

Reason:
Largest gap indicates strongest cluster separation.

--------------------------------------------------
5. LINKAGE (MOST IMPORTANT TOPIC)
--------------------------------------------------

Linkage decides:
"How distance between two clusters is measured"


A. SINGLE LINKAGE
(Nearest Point Method)
--------------------------------------------------

Distance between clusters =
Minimum distance between any pair of points.

Formula:
distance(C1,C2)= minimum(point distance)

Memory:
Single = Smallest

Advantages:
Finds non-spherical clusters
Detects arbitrary shapes

Disadvantages:
Sensitive to noise
Chaining effect

One Liner:
Nearest Neighbor


B. COMPLETE LINKAGE
(Farthest Point Method)
--------------------------------------------------

Distance between clusters =Maximum distance between any pair of points.

Formula:
distance(C1,C2)= maximum(point distance)

Memory:
Complete = Maximum

Advantages:
Less affected by outliers
Produces compact clusters

Disadvantages:
Poor for elongated clusters

One Linear:
Farthest Neighbor


C. AVERAGE LINKAGE
--------------------------------------------------

Distance between clusters =Average of all pairwise distances.

Formula:(d1+d2+d3+...+dn)/n

Memory:
Average = Mean Distance

Advantages:
Balanced approach

Disadvantages:
Computationally heavier


D. WARD LINKAGE
(MOST IMPORTANT)
--------------------------------------------------

Idea:
Merge clusters causing minimum increase
in within-cluster variance.

Goal:
Keep clusters compact and tight.

Memory:
Ward = Variance Minimization

Advantages:
Usually best practical choice
Compact clusters
Robust to noise

Disadvantages:
Prefers spherical clusters

One Linear:
Minimum Variance Method

--------------------------------------------------
6. LINKAGE COMPARISON
--------------------------------------------------

Single Linkage→ MIN distance

Complete Linkage→ MAX distance

Average Linkage→ AVG distance

Ward Linkage→ MIN variance increase

--------------------------------------------------
7. TIME & SPACE COMPLEXITY
--------------------------------------------------

Space Complexity:O(n²)

Time Complexity:O(n² log n) to O(n³)

One Linear:
"Hierarchical clustering is expensive and
not suitable for very large datasets."

--------------------------------------------------
8. ADVANTAGES
--------------------------------------------------

1. Produces hierarchy of clusters.
2. Dendrogram gives visualization.
3. Works with any distance metric.
4. Does not assume spherical clusters.
5. Easy to understand.
6. Ward linkage can handle noise well.

--------------------------------------------------
9. DISADVANTAGES
--------------------------------------------------

1. High computational cost.
2. Sensitive to outliers
   (especially Single Linkage).
3. Dendrogram cutting is subjective.
4. Results depend heavily on linkage.
5. No global objective function.
6. Poor scalability.

--------------------------------------------------
10. K-MEANS VS HIERARCHICAL
--------------------------------------------------

Feature               K-Means      Hierarchical

Need K beforehand?    Yes          No

Output                Clusters     Dendrogram

Scalability           Better       Poor

Interpretability      Lower        Higher

Cluster Hierarchy     No           Yes

Computation           Faster       Slower

--------------------------------------------------
11. DBSCAN VS HIERARCHICAL
--------------------------------------------------

Feature             DBSCAN        Hierarchical

Need K?             No            No

Outlier Detection   Yes           Limited

Arbitrary Shape     Excellent     Good

Dendrogram          No            Yes

Large Dataset       Better        Poor

Hyperparameters     ε,MinPts      Linkage


--------------------------------------------------
12. MOST ASKED INTERVIEW QUESTIONS
--------------------------------------------------

Q1. What is Agglomerative Clustering?
Ans:
Bottom-up hierarchical clustering where
each point starts as its own cluster and
nearest clusters are repeatedly merged.

--------------------------------------------------

Q2. What is a Dendrogram?
Ans:
Tree structure showing cluster merging process.

--------------------------------------------------

Q3. How to find number of clusters?
Ans:
Cut dendrogram horizontally and count
intersected branches.

--------------------------------------------------

Q4. Difference between Single and Complete Linkage?
Ans:
Single uses minimum distance.
Complete uses maximum distance.

--------------------------------------------------

Q5. Which linkage is generally preferred?
Ans:
Ward Linkage.

Reason:
Produces compact clusters and minimizes
within-cluster variance.

--------------------------------------------------

Q6. Biggest drawback?
Ans:
High computational complexity O(n²)-O(n³).

--------------------------------------------------

Q7. Why not use Hierarchical for huge datasets?
Ans:
Requires O(n²) memory and O(n³) time.


</pre>