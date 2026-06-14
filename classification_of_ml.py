"""
Machine Learning:-"Machine Learning is a field of AI where systems learn patterns from data and make predictions or decisions without being explicitly programmed."


1. By Supervision
   ├── Supervised
   ├── Unsupervised
   ├── Semi-Supervised
   └── Reinforcement

2. By Generalization Strategy
   ├── Instance-Based
   └── Model-Based

3. By Learning Style
   ├── Batch Learning
   └── Online Learning

4. By Output Certainty
   ├── Deterministic
   └── Probabilistic

5. By Statistical Assumptions
   ├── Parametric
   └── Non-Parametric

6. By Training Strategy
   ├── Eager Learner
   └── Lazy Learner

7. By Interpretability
   ├── White Box
   ├── Gray Box
   └── Black Box

8. By Ensemble Structure
   ├── Single Model
   └── Ensemble Model

9. By Objective
   ├── Regression
   ├── Classification
   ├── Clustering
   ├── Dimensionality Reduction
   └── Recommendation

10. By Model Family (HOW solved?)
    ├── Linear Models
    ├── Distance-Based Models
    ├── Probabilistic Models
    ├── Tree-Based Models
    ├── Boosting Models
    ├── Margin-Based Models
    ├── Matrix Factorization Models
    ├── Graph-Based Models
    └── Neural Network Models
   

11. By Data Type
    ├── Tabular
    ├── Time Series
    ├── Text
    ├── Image
    ├── Audio
    └── Graph


===============================================================
#1-By Supervision
├── 1. SUPERVISED LEARNING
│   │
│   ├── Idea:
│   │   Data contains Inputs (X) and Labels (Y).
│   │   Model learns X → Y mapping.
│   │
│   ├── Used For:
│   │   Predicting known target values.
│   │
│   ├── Regression
│   │   Predict Continuous Values
│   │   Example: House Price, Salary, Sales
│   │
│   │   ├── Linear Regression       → Linear relationship
│   │   ├── Ridge Regression        → L2 regularization
│   │   ├── Lasso Regression        → L1 regularization
│   │   ├── Elastic Net             → L1 + L2
│   │   ├── Decision Tree Regressor → Rule-based prediction
│   │   ├── Random Forest Regressor → Multiple trees
│   │   ├── XGBoost Regressor       → Boosted trees
│   │   ├── LightGBM Regressor      → Fast boosting
│   │   ├── CatBoost Regressor      → Handles categorical data
│   │   ├── SVR                     → SVM for regression
│   │   └── KNN Regressor           → Nearest neighbors
│   │
│   └── Classification
│       Predict Categories
│       Example: Spam/Not Spam, Disease/No Disease
│
│       ├── Logistic Regression → Linear classifier
│       ├── Naive Bayes         → Probability-based
│       ├── KNN                 → Neighbor-based
│       ├── Decision Tree       → Rule-based
│       ├── Random Forest       → Multiple trees
│       ├── SVM                 → Maximum margin classifier
│       ├── AdaBoost            → Sequential weak learners
│       ├── Gradient Boosting   → Error correction boosting
│       ├── XGBoost             → Optimized boosting
│       ├── LightGBM            → Fast boosting
│       ├── CatBoost            → Categorical boosting
│       └── Neural Networks     → Multi-layer learning
│
├── 2. UNSUPERVISED LEARNING
│   │
│   ├── Idea:
│   │   No labels available.
│   │   Model discovers hidden patterns.
│   │
│   ├── Clustering
│   │   Group Similar Data Points
│   │   Example: Customer Segmentation
│   │
│   │   ├── K-Means               → Centroid-based clustering
│   │   ├── Hierarchical          → Tree-like clustering
│   │   ├── DBSCAN                → Density-based clustering
│   │   ├── Mean Shift            → Mode-based clustering
│   │   └── Gaussian Mixture      → Probabilistic clusters
│   │
│   ├── Dimensionality Reduction
│   │   Reduce Features While Preserving Information
│   │   Example: Visualization, Compression
│   │
│   │   ├── PCA    → Maximum variance directions
│   │   ├── SVD    → Matrix decomposition
│   │   ├── LDA    → Class-separation projection
│   │   ├── t-SNE  → Visualization technique
│   │   └── UMAP   → Fast manifold learning
│   │
│   └── Association Rules
│       Find Item Relationships
│       Example: Market Basket Analysis
│
│       ├── Apriori  → Frequent itemsets
│       ├── Eclat    → Vertical itemset mining
│       └── FP-Growth→ Fast pattern mining
│
├── 3. SEMI-SUPERVISED LEARNING
│   │
│   ├── Idea:
│   │   Few labeled samples +
│   │   Many unlabeled samples
│   │
│   ├── Used When:
│   │   Labeling data is expensive.
│   │
│   ├── Self Training      → Model labels new data itself
│   ├── Label Propagation  → Spread labels through graph
│   └── Pseudo Labeling    → Use predictions as labels
│
├── 4. REINFORCEMENT LEARNING
│   │
│   ├── Idea:
│   │   Learn by trial and error using rewards.
│   │
│   ├── Components:
│   │
│   ├── Agent       → Learner
│   ├── Environment → World
│   ├── State       → Current situation
│   ├── Action      → Decision taken
│   └── Reward      → Feedback signal
│   │
│   ├── Q-Learning  → Value-based RL
│   ├── SARSA       → On-policy learning
│   ├── DQN         → Deep Q Network
│   ├── PPO         → Stable policy optimization
│   └── Actor-Critic→ Policy + Value learning


===============================================================

 #2. GENERALIZATION STRATEGY
├── Definition:
│   "How a model uses past training data to make predictions
│    on unseen data."
│
├── Goal:
│   Learn patterns that work on new data,
│   not just memorize training data.
│
├── 1. INSTANCE-BASED LEARNING
│   │
│   ├── Idea:
│   │   Store training examples and compare
│   │   new data with previously seen data.
│   │
│   ├── How It Works:
│   │   Learn → Store Data
│   │   Predict → Find Similar Instances
│   │
│   ├── Characteristics:
│   │   ✔ Little training time
│   │   ✔ Adapts easily to new data
│   │   ✔ No explicit model
│   │   ✘ Slow prediction
│   │   ✘ High memory usage
│   │
│   ├── Examples:
│   │
│   │   ├── K-Nearest Neighbors (KNN)
│   │   │   → Uses nearest samples
│   │
│   │   ├── Weighted KNN
│   │   │   → Closer neighbors get more weight
│   │
│   │   ├── Case-Based Reasoning
│   │   │   → Solve using similar past cases
│   │
│   │   └── Memory-Based Collaborative Filtering
│   │       → Recommendation systems
│   │
│   └── One-Liner:
│       "Learns by remembering training examples."
│
├── 2. MODEL-BASED LEARNING
│   │
│   ├── Idea:
│   │   Learn a mathematical model from data
│   │   and use that model for prediction.
│   │
│   ├── How It Works:
│   │   Learn Pattern → Build Model
│   │   Use Model → Predict New Data
│   │
│   ├── Characteristics:
│   │   ✔ Fast prediction
│   │   ✔ Lower memory usage
│   │   ✔ Better scalability
│   │   ✘ Requires training
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Learns equation
│   │
│   │   ├── Logistic Regression
│   │   │   → Learns probability boundary
│   │
│   │   ├── Decision Tree
│   │   │   → Learns decision rules
│   │
│   │   ├── Random Forest
│   │   │   → Learns multiple trees
│   │
│   │   ├── Naive Bayes
│   │   │   → Learns probability model
│   │
│   │   ├── SVM
│   │   │   → Learns optimal boundary
│   │
│   │   ├── Neural Networks
│   │   │   → Learns weights & representations
│   │
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   └── CatBoost
│   │
│   └── One-Liner:
│       "Learns a generalized mathematical model from data."
│
└── QUICK DIFFERENCE

    Instance-Based
    ├── Memorizes examples
    ├── Lazy learning
    ├── Slow prediction
    ├── High memory
    └── Example: KNN

    Model-Based
    ├── Learns a model
    ├── Eager learning
    ├── Fast prediction
    ├── Lower memory
    └── Example: Linear Regression, Tree, SVM

===============================================================

#3. LEARNING STYLE
├── Definition:
│   "How and when a model learns from incoming data."
│
├── Goal:
│   Decide whether the model learns from
│   the entire dataset at once or continuously
│   as new data arrives.
│
├── 1. BATCH LEARNING (Offline Learning)
│   │
│   ├── Idea:
│   │   Train using the complete dataset at once.
│   │
│   ├── How It Works:
│   │   Collect Data
│   │        ↓
│   │   Train Model
│   │        ↓
│   │   Deploy
│   │        ↓
│   │   Retrain When New Data Arrives
│   │
│   ├── Characteristics:
│   │   ✔ Stable training
│   │   ✔ Usually higher accuracy
│   │   ✔ Easier evaluation
│   │   ✔ Simpler implementation
│   │   ✘ Cannot adapt automatically
│   │   ✘ Requires retraining
│   │
│   ├── Best For:
│   │   - Static datasets
│   │   - Academic projects
│   │   - Most ML applications
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   ├── Logistic Regression
│   │   ├── Decision Tree
│   │   ├── Random Forest
│   │   ├── SVM
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   ├── CatBoost
│   │   └── Neural Networks (traditional training)
│   │
│   └── One-Liner:
│       "Learns from the entire dataset at once."
│
├── 2. ONLINE LEARNING
│   │
│   ├── Idea:
│   │   Learn continuously as new data arrives.
│   │
│   ├── How It Works:
│   │   New Data
│   │       ↓
│   │   Update Model
│   │       ↓
│   │   New Data
│   │       ↓
│   │   Update Again
│   │
│   ├── Characteristics:
│   │   ✔ Adapts to changing patterns
│   │   ✔ Works with data streams
│   │   ✔ Less memory usage
│   │   ✔ Real-time learning
│   │   ✘ Can be unstable
│   │   ✘ Sensitive to noisy data
│   │
│   ├── Best For:
│   │   - Stock markets
│   │   - Recommendation systems
│   │   - Fraud detection
│   │   - Real-time analytics
│   │
│   ├── Examples:
│   │
│   │   ├── Online SGD
│   │   ├── Perceptron
│   │   ├── Passive Aggressive
│   │   ├── Online Naive Bayes
│   │   ├── Hoeffding Tree
│   │   └── Streaming ML Algorithms
│   │
│   └── One-Liner:
│       "Learns incrementally from incoming data."
│
├── RELATED CONCEPTS
│
├── Mini-Batch Learning
│   │
│   ├── Hybrid Approach
│   ├── Data processed in small chunks
│   ├── Most Deep Learning uses this
│   │
│   └── Example:
│       Batch Size = 32, 64, 128, 256
│
└── QUICK DIFFERENCE

    Batch Learning
    ├── Entire dataset together
    ├── Offline training
    ├── Requires retraining
    ├── Stable
    └── Example: Random Forest

    Online Learning
    ├── One sample/chunk at a time
    ├── Continuous training
    ├── Self-updating
    ├── Adaptive
    └── Example: Online SGD

===============================================================

#4. OUTPUT CERTAINTY
├── Definition:
│   "How a model expresses its prediction."
│
├── Goal:
│   Determine whether the model gives
│   a fixed answer or a probability-based answer.
│
├── 1. DETERMINISTIC MODELS
│   │
│   ├── Idea:
│   │   Same input always produces
│   │   the same output.
│   │
│   ├── Characteristics:
│   │   ✔ Predictable
│   │   ✔ Consistent
│   │   ✔ Easy to interpret
│   │   ✘ No uncertainty information
│   │
│   ├── Output Example:
│   │   Student Features
│   │       ↓
│   │   Placement = YES
│   │
│   │   (No confidence score given)
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Predicts a fixed value
│   │
│   │   ├── Decision Tree
│   │   │   → Fixed decision path
│   │
│   │   ├── Random Forest*
│   │   │   → Usually used deterministically
│   │
│   │   ├── KNN*
│   │   │   → Majority vote prediction
│   │
│   │   ├── SVM
│   │   │   → Class prediction
│   │
│   │   └── Rule-Based Systems
│   │
│   └── Interview One-Liner:
│       "Produces a fixed prediction without
│        explicitly modeling uncertainty."
│
├── 2. PROBABILISTIC MODELS
│   │
│   ├── Idea:
│   │   Predicts probabilities along with
│   │   the final prediction.
│   │
│   ├── Characteristics:
│   │   ✔ Measures uncertainty
│   │   ✔ Better decision making
│   │   ✔ Useful in risk-sensitive problems
│   │   ✘ More computationally complex
│   │
│   ├── Output Example:
│   │   Placement = YES
│   │   Probability = 92%
│   │
│   │   Placement = NO
│   │   Probability = 8%
│   │
│   ├── Examples:
│   │
│   │   ├── Logistic Regression
│   │   │   → Predicts class probabilities
│   │
│   │   ├── Naive Bayes
│   │   │   → Based on probability theory
│   │
│   │   ├── Bayesian Networks
│   │   │   → Graphical probability models
│   │
│   │   ├── Gaussian Mixture Models
│   │   │   → Probabilistic clustering
│   │
│   │   ├── Hidden Markov Models
│   │   │   → Probabilistic sequences
│   │
│   │   └── Bayesian Regression
│   │
│   └── One-Liner:
│       "Produces predictions along with
│        confidence or probability estimates."
│
├── IMPORTANT FACTS
│
├── Some Algorithms Can Be Both
│   │
│   ├── Random Forest
│   │   ├── Deterministic → Final class prediction
│   │   └── Probabilistic → predict_proba()
│   │
│   ├── KNN
│   │   ├── Deterministic → Majority vote
│   │   └── Probabilistic → Neighbor proportions
│   │
│   ├── Neural Networks
│   │   ├── Deterministic → Direct output
│   │   └── Probabilistic → Softmax probabilities
│   │
│   └── SVM
│       ├── Deterministic → Class label
│       └── Probabilistic → Probability calibration
│
└── QUICK  DIFFERENCE

    Deterministic
    ├── Fixed answer
    ├── No uncertainty estimate
    ├── Same input → Same output
    └── Example: Decision Tree

    Probabilistic
    ├── Gives confidence score
    ├── Models uncertainty
    ├── Probability distribution output
    └── Example: Naive Bayes

===============================================================

#5. STATISTICAL ASSUMPTIONS
├── Definition:
│   "How much the model assumes about the underlying
│    data distribution and relationship between variables."
│
├── Goal:
│   Determine whether the model learns using a fixed
│   set of parameters or lets complexity grow with data.
│
├── 1. PARAMETRIC MODELS
│   │
│   ├── Idea:
│   │   Assume a specific form/structure for data.
│   │   Number of parameters remains fixed
│   │   regardless of dataset size.
│   │
│   ├── Characteristics:
│   │   ✔ Faster training
│   │   ✔ Less data required
│   │   ✔ Simpler models
│   │   ✔ More interpretable
│   │   ✘ Strong assumptions
│   │   ✘ Can underfit complex patterns
│   │
│   ├── How It Works:
│   │   Data
│   │    ↓
│   │ Learn Fixed Parameters
│   │    ↓
│   │ Prediction
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Fixed coefficients (β)
│   │
│   │   ├── Logistic Regression
│   │   │   → Fixed weights
│   │
│   │   ├── Naive Bayes
│   │   │   → Assumes probability distribution
│   │
│   │   ├── Linear Discriminant Analysis (LDA)
│   │   │   → Assumes Gaussian classes
│   │
│   │   └── Perceptron
│   │
│   └── One-Liner:
│       "Uses fixed parameters and strong assumptions
│        about the data."
│
├── 2. NON-PARAMETRIC MODELS
│   │
│   ├── Idea:
│   │   Make fewer assumptions about data.
│   │   Model complexity can grow as data grows.
│   │
│   ├── Characteristics:
│   │   ✔ Flexible
│   │   ✔ Captures complex patterns
│   │   ✔ Fewer distribution assumptions
│   │   ✘ More data required
│   │   ✘ Higher computation
│   │   ✘ Can overfit
│   │
│   ├── How It Works:
│   │   More Data
│   │      ↓
│   │ More Complexity
│   │      ↓
│   │ Better Pattern Capture
│   │
│   ├── Examples:
│   │
│   │   ├── KNN
│   │   │   → Stores training examples
│   │
│   │   ├── Decision Tree
│   │   │   → Grows with data
│   │
│   │   ├── Random Forest
│   │   │   → Multiple growing trees
│   │
│   │   ├── SVM (RBF Kernel)
│   │   │   → Flexible decision boundary
│   │
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   ├── CatBoost
│   │
│   └── One-Liner:
│       "Makes minimal assumptions and allows
│        complexity to grow with data."
│
├── INTUITION EXAMPLE
│
├── House Price Prediction
│   │
│   ├── Parametric
│   │
│   │   Price = β₀ + β₁(Area) + β₂(Rooms)
│   │
│   │   Assumes relationship follows
│   │   a predefined equation.
│   │
│   └── Non-Parametric
│
│       Decision Tree
│       Random Forest
│       KNN
│
│       Learns shape directly from data
│       without assuming a fixed equation.
│
├── QUICK  DIFFERENCE
    Parametric
    ├── Fixed number of parameters
    ├── Strong assumptions
    ├── Fast training
    ├── Less data needed
    └── Example: Linear Regression

    Non-Parametric
    ├── Complexity grows with data
    ├── Fewer assumptions
    ├── More flexible
    ├── More data needed
    └── Example: KNN
    
    BIAS-VARIANCE TRADE-OFF DIRECTIVE
    ├── Parametric models → High Bias / Low Variance (simpler, strict assumptions).
    └── Non-Parametric models → Low Bias / High Variance (flexible, customizes to data patterns).

===============================================================

#6. TRAINING STRATEGY
├── Definition:
│   "When does the model perform learning?"
│
├── Goal:
│   Determine whether learning happens
│   before prediction or during prediction.
│
├── 1. EAGER LEARNERS
│   │
│   ├── Idea:
│   │   Learn a model during training phase
│   │   before any prediction is made.
│   │
│   ├── How It Works:
│   │   Training Data
│   │         ↓
│   │   Learn Model
│   │         ↓
│   │   Store Parameters
│   │         ↓
│   │   Prediction
│   │
│   ├── Characteristics:
│   │   ✔ High training time
│   │   ✔ Fast prediction
│   │   ✔ Lower memory usage
│   │   ✔ Good scalability
│   │   ✘ Requires retraining for new data
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Learns coefficients
│   │
│   │   ├── Logistic Regression
│   │   │   → Learns weights
│   │
│   │   ├── Naive Bayes
│   │   │   → Learns probabilities
│   │
│   │   ├── Decision Tree
│   │   │   → Learns rules
│   │
│   │   ├── Random Forest
│   │   │   → Learns multiple trees
│   │
│   │   ├── SVM
│   │   │   → Learns decision boundary
│   │
│   │   ├── Neural Networks
│   │   │   → Learns weights
│   │
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   └── CatBoost
│   │
│   └── One-Liner:
│       "Learns a model before making predictions."
│
├── 2. LAZY LEARNERS
│   │
│   ├── Idea:
│   │   Do not build an explicit model during training.
│   │   Learning happens when prediction is requested.
│   │
│   ├── How It Works:
│   │   Training Data
│   │         ↓
│   │     Store Data
│   │         ↓
│   │   New Query Arrives
│   │         ↓
│   │   Learn / Compare
│   │         ↓
│   │   Prediction
│   │
│   ├── Characteristics:
│   │   ✔ Almost no training time
│   │   ✔ Easy to update with new data
│   │   ✔ Flexible
│   │   ✘ Slow prediction
│   │   ✘ High memory usage
│   │   ✘ Poor scalability
│   │
│   ├── Examples:
│   │
│   │   ├── K-Nearest Neighbors (KNN)
│   │   │   → Stores training examples
│   │
│   │   ├── Weighted KNN
│   │   │   → Distance-weighted neighbors
│   │
│   │   ├── Case-Based Reasoning
│   │   │   → Uses similar past cases
│   │
│   │   └── Memory-Based Collaborative Filtering
│   │       → Recommendation systems
│   │
│   └── One-Liner:
│       "Delays learning until prediction time."
│
├── TRAINING vs PREDICTION TIME
│
├── Eager Learner
│   │
│   ├── Training Time   → High
│   ├── Prediction Time → Low
│   └── Example         → Logistic Regression
│
└── Lazy Learner
    │
    ├── Training Time   → Very Low
    ├── Prediction Time → High
    └── Example         → KNN


    QUICK DIFFERENCE
    Eager Learner
    ├── Learns before prediction
    ├── Builds model
    ├── High training cost
    ├── Fast prediction
    └── Example: Decision Tree

    Lazy Learner
    ├── Learns during prediction
    ├── Stores data
    ├── Low training cost
    ├── Slow prediction
    └── Example: KNN

──────────────────────────────────────

IMPORTANT RELATIONSHIP

    Instance-Based  ≈ Usually Lazy Learner
    Model-Based     ≈ Usually Eager Learner

Examples:

    KNN
    ├── Instance-Based
    ├── Non-Parametric
    └── Lazy Learner

    Linear Regression
    ├── Model-Based
    ├── Parametric
    └── Eager Learner

    Decision Tree
    ├── Model-Based
    ├── Non-Parametric
    └── Eager Learner


──────────────────────────────────────

===============================================================

#7. INTERPRETABILITY
├── Definition:
│   "How easily humans can understand and explain
│    why a model made a particular prediction."
│
├── Goal:
│   Determine whether model decisions are
│   transparent, partially explainable,
│   or difficult to understand.
│
├── 1. WHITE BOX MODELS
│   │
│   ├── Idea:
│   │   Internal logic is completely visible
│   │   and understandable.
│   │
│   ├── Characteristics:
│   │   ✔ Highly interpretable
│   │   ✔ Easy to explain
│   │   ✔ Easy debugging
│   │   ✔ Regulatory friendly
│   │   ✘ May miss complex patterns
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Coefficients are interpretable
│   │
│   │   ├── Logistic Regression
│   │   │   → Feature impact visible
│   │
│   │   ├── Decision Tree (Small)
│   │   │   → Rules can be traced
│   │
│   │   ├── Rule-Based Systems
│   │   │   → Explicit IF-THEN rules
│   │
│   │   └── Simple Naive Bayes
│   │
│   └── One-Liner:
│       "Model decisions can be fully explained."
│
├── 2. GRAY BOX MODELS
│   │
│   ├── Idea:
│   │   Partially understandable but not
│   │   completely transparent.
│   │
│   ├── Characteristics:
│   │   ✔ Moderate interpretability
│   │   ✔ Better accuracy than simple models
│   │   ✔ Some explainability tools available
│   │   ✘ Internal logic not fully obvious
│   │
│   ├── Examples:
│   │
│   │   ├── Random Forest
│   │   │   → Many trees make reasoning difficult
│   │
│   │   ├── Gradient Boosting
│   │   │   → Ensemble of trees
│   │
│   │   ├── XGBoost
│   │   │   → Feature importance available
│   │
│   │   ├── LightGBM
│   │   │   → Partial interpretability
│   │
│   │   ├── CatBoost
│   │   │   → Feature importance available
│   │
│   │   └── Large Decision Trees
│   │
│   └── One-Liner:
│       "Somewhat explainable but not fully transparent."
│
├── 3. BLACK BOX MODELS
│   │
│   ├── Idea:
│   │   Inputs and outputs are visible,
│   │   but internal reasoning is difficult
│   │   to understand.
│   │
│   ├── Characteristics:
│   │   ✔ High predictive power
│   │   ✔ Captures complex patterns
│   │   ✔ Excellent for large datasets
│   │   ✘ Difficult to explain
│   │   ✘ Hard to debug
│   │   ✘ Regulatory concerns
│   │
│   ├── Examples:
│   │
│   │   ├── Deep Neural Networks
│   │   │   → Millions of parameters
│   │
│   │   ├── CNN
│   │   │   → Image learning
│   │
│   │   ├── RNN / LSTM
│   │   │   → Sequence learning
│   │
│   │   ├── Transformers
│   │   │   → GPT, BERT, etc.
│   │
│   │   ├── Deep Reinforcement Learning
│   │   │   → Complex decision policies
│   │
│   │   └── Very Deep Ensembles
│   │
│   └── Interview One-Liner:
│       "Produces predictions but internal logic
│        is difficult to explain."
│
├── EXPLAINABILITY TOOLS
│
├── Used Mainly For Gray/Black Box Models
│
├── Feature Importance
├── SHAP
├── LIME
├── Partial Dependence Plots
└── Permutation Importance
│
├── REAL-WORLD USAGE
│
├── White Box
│   ├── Banking
│   ├── Insurance
│   ├── Healthcare
│   └── Government Systems
│
├── Gray Box
│   ├── Business Analytics
│   ├── Customer Churn
│   └── Credit Risk
│
└── Black Box
    ├── Computer Vision
    ├── NLP
    ├── Speech Recognition
    └── Autonomous Systems

    QUICK  DIFFERENCE
    White Box
    ├── Fully explainable
    ├── High transparency
    ├── Lower complexity
    └── Example: Linear Regression

    Gray Box
    ├── Partially explainable
    ├── Moderate transparency
    ├── Ensemble models
    └── Example: Random Forest

    Black Box
    ├── Hard to explain
    ├── Low transparency
    ├── High complexity
    └── Example: Neural Network

===============================================================

#8. ENSEMBLE STRUCTURE
├── Definition:
│   "How predictions are generated:
│    using a single model or multiple models."
│
├── Goal:
│   Determine whether prediction comes from
│   one learner or a combination of learners.
│
├── 1. SINGLE MODEL
│   │
│   ├── Idea:
│   │   One model makes the final prediction.
│   │
│   ├── Characteristics:
│   │   ✔ Simple
│   │   ✔ Fast training
│   │   ✔ Easy interpretation
│   │   ✔ Low computation
│   │   ✘ Lower accuracy in complex problems
│   │   ✘ Less robust
│   │
│   ├── Examples:
│   │
│   │   ├── Linear Regression
│   │   │   → Single equation
│   │
│   │   ├── Logistic Regression
│   │   │   → Single classifier
│   │
│   │   ├── KNN
│   │   │   → Single neighbor-based model
│   │
│   │   ├── Naive Bayes
│   │   │   → Single probabilistic model
│   │
│   │   ├── SVM
│   │   │   → Single decision boundary
│   │
│   │   ├── Decision Tree
│   │   │   → Single tree
│   │
│   │   └── Neural Network
│   │       → Single network architecture
│   │
│   └── One-Liner:
│       "Prediction comes from one model."
│
├── 2. ENSEMBLE MODEL
│   │
│   ├── Idea:
│   │   Multiple models work together
│   │   to produce the final prediction.
│   │
│   ├── Why Use It?
│   │
│   │   Weak Models
│   │        ↓
│   │   Combine Predictions
│   │        ↓
│   │   Better Accuracy
│   │        ↓
│   │   Better Generalization
│   │
│   ├── Characteristics:
│   │   ✔ Higher accuracy
│   │   ✔ Better robustness
│   │   ✔ Reduced overfitting
│   │   ✔ Better generalization
│   │   ✘ More computation
│   │   ✘ Less interpretable
│   │
│   ├── Types of Ensemble
│   │
│   ├── A. Bagging
│   │   │
│   │   ├── Idea:
│   │   │   Train models independently
│   │   │   and combine predictions.
|   |   |
│   │   ├── Strategy: Parallel independent training on bootstrapped samples.
|   │   ├Math Goal: Aggressively reduces VARIANCE without shifting bias.
|   │   └ Example: Random Forest, Extra Trees
│   │  
│   │   
│   │   ├── Examples:
│   │   │   ├── Random Forest
│   │   │   └── Extra Trees
│   │   │
│   │   └── Goal:
│   │       Reduce Variance
│   │
│   ├── B. Boosting
│   │   │
│   │   ├── Idea:
│   │   │   Models learn sequentially.
│   │   │   Each model fixes previous errors.
|   |   |
│   │   ├── Strategy: Sequential training. Each sequential learner corrects errors of the predecessor.
|   │   ├ Math Goal: Aggressively reduces BIAS.
|   │   └ Example: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost
│   │   
│   │   ├── Examples:
│   │   │   ├── AdaBoost
│   │   │   ├── Gradient Boosting
│   │   │   ├── XGBoost
│   │   │   ├── LightGBM
│   │   │   └── CatBoost
│   │   │
│   │   └── Goal:
│   │       Reduce Bias
│   │
│   └── C. Stacking
│       │
│       ├── Idea:
│       │   Predictions of multiple models
│       │   become inputs to another model.
|       |
│       ├── Strategy: Heterogeneous base models feed their predictions into a meta-learner.
|       └── Math Goal: Leverages different architectural spaces simultaneously.
│       
│       ├── Example:
│       │   Random Forest │
|       |
│       │   XGBoost         ├── Meta Model
│       │         
│       │   SVM           │
│       │         
│       │                 Final Prediction
│       │
│       └── Goal:
│           Use strengths of different algorithms
│
├── QUICK DIFFERENCE
    Single Model
    ├── One learner
    ├── Simpler
    ├── Faster
    ├── More interpretable
    └── Example: Decision Tree

    Ensemble Model
    ├── Multiple learners
    ├── More accurate
    ├── More robust
    ├── Higher computation
    └── Example: Random Forest

===============================================================

├── 9. BY OBJECTIVE (WHAT problem are we solving?)
│
├── Definition:
│   "Classification based on the business problem
│    or task the model is trying to solve."
│
├── 1. REGRESSION
│   │
│   ├── Goal:
│   │   Predict continuous numerical values.
│   │
│   ├── Examples:
│   │   - House Price Prediction
│   │   - Salary Prediction
│   │   - Delivery Time Prediction
│   │   - Sales Forecasting
│   │
│   └── Output:
│       Numeric Value
│
├── 2. CLASSIFICATION
│   │
│   ├── Goal:
│   │   Predict categories or classes.
│   │
│   ├── Types:
│   │   ├── Binary Classification
│   │   ├── Multi-Class Classification
│   │   └── Multi-Label Classification
│   │
│   ├── Examples:
│   │   - Spam Detection
│   │   - Disease Prediction
│   │   - Customer Churn Prediction
│   │   - Sentiment Analysis
│   │
│   └── Output:
│       Class Label
│
├── 3. CLUSTERING
│   │
│   ├── Goal:
│   │   Group similar observations together.
│   │
│   ├── Examples:
│   │   - Customer Segmentation
│   │   - Document Grouping
│   │   - Market Segmentation
│   │
│   └── Output:
│       Cluster Assignment
│
├── 4. DIMENSIONALITY REDUCTION
│   │
│   ├── Goal:
│   │   Reduce the number of features while
│   │   preserving important information.
│   │
│   ├── Examples:
│   │   - Data Compression
│   │   - Feature Extraction
│   │   - Data Visualization
│   │
│   └── Output:
│       Reduced Feature Space
│
├── 5. RECOMMENDATION
│   │
│   ├── Goal:
│   │   Suggest relevant items to users.
│   │
│   ├── Examples:
│   │   - Netflix Movie Recommendation
│   │   - Amazon Product Recommendation
│   │   - YouTube Video Recommendation
│   │
│   └── Output:
│       Ranked Item List
│
├── 6. ANOMALY DETECTION
│   │
│   ├── Goal:
│   │   Identify rare or abnormal observations.
│   │
│   ├── Examples:
│   │   - Fraud Detection
│   │   - Network Intrusion Detection
│   │   - Manufacturing Defect Detection
│   │
│   └── Output:
│       Normal / Anomaly
│
├── 7. FORECASTING (TIME SERIES)
│   │
│   ├── Goal:
│   │   Predict future values using historical
│   │   time-dependent observations.
│   │
│   ├── Examples:
│   │   - Stock Price Forecasting
│   │   - Demand Forecasting
│   │   - Weather Forecasting
│   │   - Traffic Forecasting
│   │
│   └── Output:
│       Future Value(s)
│
└── ONE-LINERS
    Regression               → Predict numbers
    Classification           → Predict categories
    Clustering               → Group similar data
    Dimensionality Reduction → Reduce features
    Recommendation           → Suggest items
    Anomaly Detection        → Find unusual cases
    Forecasting             → Predict future values

*Linear Discriminant Analysis (LDA) is listed under Dimensionality Reduction. While true, remember that LDA is fundamentally a supervised technique (unlike PCA)
===============================================================

# 10. BY MODEL FAMILY

├── Definition:
│   "Classification based on the mathematical approach
│    or architecture used by the algorithm."
│
├── Goal:
│   Group algorithms that solve problems using
│   similar mathematical principles.
│
├── 1. LINEAR MODELS
│   │
│   ├── Core Idea:
│   │   Learn a linear relationship between variables.
│   │
│   ├── Models:
│   │   ├── Linear Regression
│   │   ├── Ridge Regression
│   │   ├── Lasso Regression
│   │   ├── Elastic Net
│   │   └── Logistic Regression
│   │
│   └── One-Liner:
│       "Models relationships using linear equations."
│
├── 2. DISTANCE-BASED MODELS
│   │
│   ├── Core Idea:
│   │   Similar observations lie close together.
│   │
│   ├── Models:
│   │   ├── KNN
│   │   ├── KNN Regressor
│   │   ├── K-Means
│   │   ├── DBSCAN
│   │   └── Mean Shift
│   │
│   └── One-Liner:
│       "Learns using similarity and distance metrics."
│
├── 3. PROBABILISTIC MODELS
│   │
│   ├── Core Idea:
│   │   Model uncertainty using probability.
│   │
│   ├── Models:
│   │   ├── Naive Bayes
│   │   ├── Gaussian Mixture Models
│   │   ├── Bayesian Networks
│   │   ├── Hidden Markov Models
│   │   └── Bayesian Regression
│   │
│   └── One-Liner:
│       "Uses probability distributions to learn patterns."
│
├── 4. TREE-BASED MODELS
│   │
│   ├── Core Idea:
│   │   Learn decision rules using hierarchical trees.
│   │
│   ├── Models:
│   │   ├── Decision Tree
│   │   ├── CART
│   │   ├── Random Forest
│   │   └── Extra Trees
│   │
│   └── One-Liner:
│       "Uses decision rules organized as trees."
│
├── 5. BOOSTING MODELS
│   │
│   ├── Core Idea:
│   │   Sequentially correct previous model mistakes.
│   │
│   ├── Models:
│   │   ├── AdaBoost
│   │   ├── Gradient Boosting
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   └── CatBoost
│   │
│   └── One-Liner:
│       "Builds strong models from weak learners."
│
├── 6. MARGIN-BASED MODELS
│   │
│   ├── Core Idea:
│   │   Maximize separation between classes.
│   │
│   ├── Models:
│   │   ├── SVM
│   │   ├── SVR
│   │   └── One-Class SVM
│   │
│   └── One-Liner:
│       "Finds the optimal separating boundary."
│
├── 7. MATRIX FACTORIZATION MODELS
│   │
│   ├── Core Idea:
│   │   Decompose data into lower-dimensional factors.
│   │
│   ├── Models:
│   │   ├── PCA
│   │   ├── SVD
│   │   ├── NMF
│   │   └── LDA*
│   │
│   └── One-Liner:
│       "Compresses data into latent components."
│
├── 8. GRAPH-BASED MODELS
│   │
│   ├── Core Idea:
│   │   Learn from nodes and relationships.
│   │
│   ├── Models:
│   │   ├── PageRank
│   │   ├── Node2Vec
│   │   ├── DeepWalk
│   │   ├── GCN
│   │   ├── GraphSAGE
│   │   └── GAT
│   │
│   └── One-Liner:
│       "Learns from interconnected entities."
│
└── 9. NEURAL NETWORK MODELS
    │
    ├── Core Idea:
    │   Learn hierarchical representations using layers.
    │
    ├── Models:
    │   ├── ANN
    │   ├── CNN
    │   ├── RNN
    │   ├── LSTM
    │   ├── GRU
    │   ├── Autoencoder
    │   ├── GAN
    │   └── Transformer
    │
    └── One-Liner:
        "Learns complex patterns through layered networks."

────────────────────────────

SPECIAL NOTES

LDA
├── Objective → Dimensionality Reduction
├── Family → Matrix Factorization / Linear Methods
└── Uses Labels (Supervised)

Autoencoder
├── Objective → Dimensionality Reduction / Anomaly Detection
└── Family → Neural Networks

LSTM
├── Objective → Forecasting
└── Family → Neural Networks

K-Means
├── Objective → Clustering
└── Family → Distance-Based

ARIMA
├── Objective → Forecasting
└── Family → Statistical Time-Series Models
│
└── (Can be treated as a specialized statistical family
    rather than a universal ML family.)
===============================================================

#11. BY DATA TYPE
├── Definition:
│   "Classification based on the type of data
│    being analyzed or processed."
│
├── Goal:
│   Different data types require different
│   algorithms, architectures and feature engineering.
│
├── 1. TABULAR DATA
│   │
│   ├── Structure:
│   │   Rows * Columns
│   │
│   ├── Examples:
│   │   Customer Data
│   │   Sales Data
│   │   Banking Data
│   │   Excel / CSV Files
│   │
│   ├── Common Models:
│   │
│   │   ├── Linear Regression
│   │   ├── Logistic Regression
│   │   ├── Decision Tree
│   │   ├── Random Forest
│   │   ├── XGBoost
│   │   ├── LightGBM
│   │   ├── CatBoost
│   │   ├── SVM
│   │   └── KNN
│   │
│   ├── Industry Champion:
│   │   XGBoost / LightGBM
│   │
│   └──  One-Liner:
│       "Structured rows and columns data."
│
├── 2. TIME SERIES DATA
│   │
│   ├── Structure:
│   │   Data indexed by time.
│   │
│   ├── Examples:
│   │   Stock Prices
│   │   Weather Data
│   │   Sales Forecasting
│   │   Sensor Readings
│   │
│   ├── Common Models:
│   │
│   │   ├── ARIMA
│   │   ├── SARIMA
│   │   ├── Prophet
│   │   ├── LSTM
│   │   ├── GRU
│   │   └── Transformers
│   │
│   ├── Special Characteristic:
│   │   Order Matters
│   │
│   └── One-Liner:
│       "Data where time order is important."
│
├── 3. TEXT DATA
│   │
│   ├── Structure:
│   │   Natural Language
│   │
│   ├── Examples:
│   │   Emails
│   │   Reviews
│   │   Tweets
│   │   Documents
│   │
│   ├── Common Tasks:
│   │
│   │   ├── Sentiment Analysis
│   │   ├── Spam Detection
│   │   ├── Text Classification
│   │   ├── Translation
│   │   └── Question Answering
│   │
│   ├── Common Models:
│   │
│   │   ├── Naive Bayes
│   │   ├── Logistic Regression
│   │   ├── RNN
│   │   ├── LSTM
│   │   ├── GRU
│   │   ├── BERT
│   │   └── Transformers
│   │
│   ├── Industry Champion:
│   │   Transformers
│   │
│   └──  One-Liner:
│       "Machine learning on human language."
│
├── 4. IMAGE DATA
│   │
│   ├── Structure:
│   │   Pixels
│   │
│   ├── Examples:
│   │   Medical Images
│   │   Face Recognition
│   │   Object Detection
│   │   Satellite Images
│   │
│   ├── Common Tasks:
│   │
│   │   ├── Classification
│   │   ├── Detection
│   │   ├── Segmentation
│   │   └── Image Generation
│   │
│   ├── Common Models:
│   │
│   │   ├── CNN
│   │   ├── ResNet
│   │   ├── EfficientNet
│   │   ├── YOLO
│   │   ├── U-Net
│   │   └── Vision Transformer (ViT)
│   │
│   ├── Industry Champion:
│   │   CNN / Vision Transformers
│   │
│   └── One-Liner:
│       "Machine learning on pixel data."
│
├── 5. AUDIO DATA
│   │
│   ├── Structure:
│   │   Sound Signals / Waveforms
│   │
│   ├── Examples:
│   │   Speech Recognition
│   │   Voice Assistants
│   │   Music Classification
│   │   Speaker Identification
│   │
│   ├── Common Models:
│   │
│   │   ├── HMM
│   │   ├── RNN
│   │   ├── LSTM
│   │   ├── GRU
│   │   ├── CNN
│   │   └── Transformers
│   │
│   ├── Industry Champion:
│   │   Transformers
│   │
│   └── One-Liner:
│       "Machine learning on sound signals."
│
├── 6. GRAPH DATA
│   │
│   ├── Structure:
│   │
│   │   Nodes ── Edges
│   │
│   ├── Examples:
│   │   Social Networks
│   │   Recommendation Systems
│   │   Fraud Networks
│   │   Knowledge Graphs
│   │
│   ├── Common Tasks:
│   │
│   │   ├── Node Classification
│   │   ├── Link Prediction
│   │   ├── Community Detection
│   │   └── Graph Classification
│   │
│   ├── Common Models:
│   │
│   │   ├── Node2Vec
│   │   ├── DeepWalk
│   │   ├── GraphSAGE
│   │   ├── GCN
│   │   ├── GAT
│   │   └── Graph Neural Networks (GNN)
│   │
│   ├── Industry Champion:
│   │   GNNs
│   │
│   └──  One-Liner:
│       "Machine learning on interconnected entities."


Data Type Classification is:

Tabular Data
├── Linear Models
├── Trees
├── Boosting

Time Series Data
├── ARIMA
├── Prophet
├── LSTM

Text Data
├── Naive Bayes
├── RNN
├── Transformer

Image Data
├── CNN
├── Vision Transformer

Graph Data
├── Node2Vec
├── Graph Neural Networks

"""