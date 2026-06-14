<pre>

═══════════════════════════════════════════════════════════════
                        NAIVE BAYES 
═══════════════════════════════════════════════════════════════

NAIVE BAYES
│
├── Bayes Theorem
│
├── Assumption
│   └── Features are conditionally independent
│
├── Training
│   ├── Calculate Prior P(Y)
│   ├── Calculate Likelihood P(Xi|Y)
│   └── Store probabilities
│
├── Prediction
│   └── MAP (Maximum A Posteriori)
│
├── Problems
│   ├── Underflow
│   │    └── Log Probabilities
│   │
│   └── Zero Frequency Problem
│        └── Laplace Smoothing
│
└── Types
    │
    ├── Gaussian NB
    │     └── Continuous Numerical Data
    │
    ├── Categorical NB
    │     └── Categorical Features
    │
    ├── Bernoulli NB
    │     └── Binary Features (0/1)
    │
    ├── Multinomial NB
    │     └── Count/Frequency Data
    │
    └── Complement NB
          └── Imbalanced Text Classification



---------------------------------------------------------------
1. WHAT IS NAIVE BAYES?
---------------------------------------------------------------

Naive Bayes is a Probabilistic Classification Algorithm based on:

1. Bayes Theorem
2. Conditional Independence Assumption

Used for:
- Spam Detection
- Sentiment Analysis
- Text Classification
- Document Classification
- Medical Diagnosis

---------------------------------------------------------------
2. BAYES THEOREM
---------------------------------------------------------------

P(A|B) = P(B|A)P(A)/P(B)

For Naive Bayes:

P(Y|X) = P(X|Y)P(Y)/P(X)

Where:

P(Y|X) = Posterior
P(X|Y) = Likelihood
P(Y)   = Prior
P(X)   = Evidence

---------------------------------------------------------------
3. NAIVE ASSUMPTION
---------------------------------------------------------------

All features are conditionally independent.

P(X1,X2,X3,...,Xn|Y)=P(X1|Y)P(X2|Y)P(X3|Y)...P(Xn|Y)

Reality:
Features may be correlated.

Naive Bayes assumes:
Features are independent.

Hence called "Naive".

---------------------------------------------------------------
4. FINAL FORMULA
---------------------------------------------------------------

P(Y|X)∝P(Y) × Π P(Xi|Y)
where
X = (X1,X2,X3,...,Xn)

---------------------------------------------------------------
5. TRAINING PHASE
---------------------------------------------------------------

No Gradient Descent
No Cost Function
No Optimization

Training Means:

1. Calculate Prior Probabilities
P(Y)

2. Calculate Likelihoods
P(Xi|Y)

3. Store Probabilities

Example:
P(Sunny|Yes)
P(Hot|Yes)
P(Normal|Yes)

---------------------------------------------------------------
6. PREDICTION PHASE
---------------------------------------------------------------

Compute:P(Class1|X)P(Class2|X)...P(ClassK|X)

Choose Maximum.
ŷ = argmax(P(Y|X))

Called:
MAP
(Maximum A Posteriori)

---------------------------------------------------------------
7. UNDERFLOW PROBLEM
---------------------------------------------------------------

Suppose:0.01 × 0.001 × 0.0001 × ...
After many multiplications:0.000000000000...

Computer stores:0
This is called:UNDERFLOW

Definition:
A number becomes so small that floating-point
representation stores it as zero.

---------------------------------------------------------------
8. SOLUTION → LOG PROBABILITIES
---------------------------------------------------------------

Instead of:P(Y)P(X1|Y)P(X2|Y)...
Take Log.

Because:
log(ab) = log(a)+log(b)

Therefore:
log(P(Y))
+
log(P(X1|Y))
+
log(P(X2|Y))
+ ...

Advantages:
✓ Avoid Underflow
✓ Faster Computation
✓ Numerical Stability

---------------------------------------------------------------
9. ZERO FREQUENCY PROBLEM
---------------------------------------------------------------

Suppose:P(excellent|Positive)=0

Then:
P(Positive|Review)=0
because multiplication contains zero.

This is called:
Zero Frequency Problem

---------------------------------------------------------------
10. LAPLACE SMOOTHING
---------------------------------------------------------------

Solution:
P = (count + α)/(N + αd)

Where:
α = Smoothing Parameter
N = Total Count
d = Number of Categories

Default:
α = 1
Called:
Laplace Additive Smoothing

---------------------------------------------------------------
11. ROLE OF α
---------------------------------------------------------------
Small α
✓ Low Bias
✓ High Variance
✓ Overfitting Risk

Example:
α = 0.0001

--------------------------------------------------
Large α
✓ High Bias
✓ Low Variance
✓ Underfitting Risk

Example:
α = 1000

---------------------------------------------------------------
12. TYPES OF NAIVE BAYES
---------------------------------------------------------------

1. Gaussian NB
2. Categorical NB
3. Bernoulli NB
4. Multinomial NB
5. Complement NB

---------------------------------------------------------------
13. GAUSSIAN NAIVE BAYES
---------------------------------------------------------------

Data Type:
Continuous Numerical Data

Examples:
Age
Salary
CGPA
Height
Weight
IQ

Assumption:
Feature follows Gaussian Distribution.
X ~ N(μ,σ²)

Training:
For every class calculate:
μ (Mean)
σ (Standard Deviation)

Prediction:
Use Gaussian PDF
f(x)=1/(σ√2π) exp(-(1/2)((x-μ)/σ)^2)

Workflow:
Calculate μ and σ
      ↓
Use Gaussian PDF
      ↓
Get P(Xi|Y)
      ↓
Apply Naive Bayes Formula

Laplace Smoothing?
NO

Reason:
No count-based probabilities.

---------------------------------------------------------------
14. CATEGORICAL NAIVE BAYES
---------------------------------------------------------------

Data Type:
All Features Categorical

Examples:
Gender
City
Department
Color
Marital Status

Training:
Calculate:
P(Category|Class)

Examples:
P(Male|Placed)
P(Female|Placed)

Uses:
Frequency Counts
+
Laplace Smoothing

---------------------------------------------------------------
15. BERNOULLI NAIVE BAYES
---------------------------------------------------------------

Data Type:
Binary Features

Values:
0/1
True/False
Yes/No

Underlying Distribution:
Bernoulli Distribution
X ∈ {0,1}

PMF:
P(X=k)=p^k(1-p)^(1-k)

Example:
Vocabulary:
good
movie
bad

Review:
good movie

Vector:
[1,1,0]
Only Presence Matters.

Example:
good good good movie

Still:
[1,1,0]

Counts Ignored.

Applications:
Spam Detection
Binary Text Classification

---------------------------------------------------------------
16. MULTINOMIAL NAIVE BAYES
---------------------------------------------------------------

MOST IMPORTANT FOR NLP

Data Type:
Counts / Frequencies

Examples:
BOW
CountVectorizer
Word Frequency
TF-IDF

Underlying Distribution:
Multinomial Distribution

Example:
Review:
good good movie actor

Vector:
[2,1,1]

Count Matters.

Unlike Bernoulli NB.

PMF:

P(X)=(n!/(n1!n2!...nk!))×Π(pi^ni)

Applications:
✓ Sentiment Analysis
✓ Spam Detection
✓ Document Classification
✓ News Classification

---------------------------------------------------------------
17. COMPLEMENT NAIVE BAYES
---------------------------------------------------------------

Purpose:
Handle Class Imbalance

Problem:
Positive = 95%
Negative = 5%

Multinomial NB may become biased.

Solution:
Instead of learning:
P(word|Positive)

Learn from complement class:
P(word|Not Positive)

Idea:
Use information from
"all other classes"

Advantages:
✓ Better for imbalanced datasets
✓ More stable
✓ Better text classification

Applications:
Spam Detection
Rare Event Classification
Imbalanced Text Data

---------------------------------------------------------------
18. DISTRIBUTIONS BEHIND NAIVE BAYES
---------------------------------------------------------------

A) Bernoulli Distribution

One Trial
Two Outcomes

Example:
Placed / Not Placed

X ∈ {0,1}

↓

Bernoulli NB

--------------------------------------------------

B) Binomial Distribution

Multiple Bernoulli Trials

Example:
10 Students
3 Placed

Formula:
P(X=k)=nCk p^k (1-p)^(n-k)

--------------------------------------------------

C) Categorical Distribution

One Trial
Multiple Categories

Example:
Placed
Not Placed
Opt Out
↓
Categorical NB

--------------------------------------------------

D) Multinomial Distribution

Multiple Trials
Multiple Categories

Example:
3 Placed
1 Opt Out
6 Not Placed
↓
Multinomial NB

--------------------------------------------------

E) Gaussian Distribution

Continuous Numerical Data

Age
Salary
CGPA
↓
Gaussian NB

---------------------------------------------------------------
19. DISTRIBUTION HIERARCHY
---------------------------------------------------------------

Multinomial Distribution
│
├── k = 2, n > 1
│       ↓
│    Binomial
│
├── k > 2, n = 1
│       ↓
│   Categorical
│
└── k = 2, n = 1
        ↓
     Bernoulli

---------------------------------------------------------------
20. WHICH NB SHOULD I USE?
---------------------------------------------------------------

Numerical Features
(Age, Salary, CGPA)
→ Gaussian NB

--------------------------------------------------

Categorical Features
(Gender, City)
→ Categorical NB

--------------------------------------------------

Binary Features
(0/1)
→ Bernoulli NB

--------------------------------------------------

Word Counts
(BOW, CountVectorizer)
→ Multinomial NB

--------------------------------------------------

Imbalanced Text Data
→ Complement NB

---------------------------------------------------------------
21. INTERVIEW QUESTIONS
---------------------------------------------------------------

Q1. Why is Naive Bayes called Naive?

Ans:
Assumes all features are conditionally independent.

--------------------------------------------------

Q2. What is the formula?

P(Y|X)∝P(Y) × ΠP(Xi|Y)

--------------------------------------------------

Q3. What is MAP?

Maximum A Posteriori
Choose class having highest posterior probability.

--------------------------------------------------

Q4. What is Underflow?

Very small probabilities become zero due to
floating-point limitations.

--------------------------------------------------

Q5. How is Underflow solved?

Log Probabilities
log(ab)=log(a)+log(b)

--------------------------------------------------

Q6. What is Laplace Smoothing?

Technique used to solve Zero Frequency Problem.

--------------------------------------------------

Q7. Why Laplace Smoothing not used in Gaussian NB?

Because Gaussian NB uses PDF instead of counts.

--------------------------------------------------

Q8. Difference Between Bernoulli NB and Multinomial NB?

Bernoulli:
Presence/Absence

Multinomial:
Frequency/Count

--------------------------------------------------

Q9. Best NB for Text Classification?

Multinomial NB

--------------------------------------------------

Q10. Best NB for Numerical Data?

Gaussian NB

--------------------------------------------------

Q11. Best NB for Binary Features?

Bernoulli NB

--------------------------------------------------

Q12. Best NB for Imbalanced Text Data?

Complement NB

---------------------------------------------------------------
22. 30-SECOND FINAL REVISION
---------------------------------------------------------------

NAIVE BAYES

Formula:
P(Y|X) ∝ P(Y)ΠP(Xi|Y)

Assumption:
Features Independent

Prediction:
MAP

Problems:
1. Underflow → Log Probabilities
2. Zero Frequency → Laplace Smoothing

Types:
Gaussian → Numerical
Categorical → Categories
Bernoulli → Binary
Multinomial → Counts/Text
Complement → Imbalanced Text

Most Used:
Multinomial NB + TF-IDF

Most Asked Interview Question:
Why is Naive Bayes called Naive?

Answer:
Because it assumes features are conditionally independent.
═══════════════════════════════════════════════════════════════          