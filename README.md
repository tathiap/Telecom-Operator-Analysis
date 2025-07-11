# Predicting Ultra Plan Subscription & Megaline Plan Revenue Analysis

Welcome to a dual-project repository focused on customer behavior analytics in the telecom sector. This repository contains:

  1. Predicting Ultra Plan Subscription Behavior — a classification-based machine learning project.

  2. Megaline Plan Revenue Analysis — a forecasting and statistical analysis project.


---
## Project 1: Predicting Ultra Plan Subscription

### Objective:
To predict whether a user is subscribed to the 'Ultra' mobile plan using historical usage data including calls, texts, and mobile data.

### Methods & Tools
* Libraries: pandas, scikit-learn, matplotlib, seaborn

* Models:
  * Decision Tree
  * Random Forest
  * Logistic Regression
  * Gradient Boosting
  * Support Vector Machine (SVM)

* Evaluation Metrics:
  * Accuracy
  * Precision, Recall, F1-score (specifically for the Ultra class)
  * Confusion Matrices
  * Feature Importance Analysis

* Preprocessing:
  * Train/Validation/Test split
  * Standardization using StandardScaler
  * Hyperparameter tuning using GridSearchCV

### Outcome
Random Forest and Gradient Boosting yielded the best performance. Feature importance analysis highlighted key usage variables influencing subscription behavior. Despite the class imbalance, fine-tuned models achieved over 80% accuracy on validation and test sets.

---

## Project 2: Megaline Plan Revenue Analysis

### Objective
To understand and forecast revenue performance of the Megaline telecom plans using historical usage patterns and plan preferences.

### Methods & Tools
Libraries: pandas, matplotlib, seaborn, scipy.stats, statsmodels

* EDA & Statistical Analysis:
  * Monthly usage patterns by plan
  * Revenue distribution analysis

* Independent t-tests on:
  * Revenue by plan
  * Revenue by region (e.g., NY-NJ vs others)

* Forecasting:
  * Simulated revenue trend lines
  * Linear regression fits by plan

### Outcome
* Clear revenue advantage for the Ultimate plan over the Surf plan.
* Statistically significant revenue differences were observed between regions and plans.
* Forecasting models suggest a stable upward trend in revenue for both plans, particularly Ultimate.


