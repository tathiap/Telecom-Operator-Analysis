# Predicting Ultra Plan Subscription & Megaline Plan Revenue Analysis

Welcome to a **multi-project repository** focused on **customer behavior analytics in the telecom sector**.  
This repository contains three major projects:

1. **Predicting Ultra Plan Subscription (ML classification)**  
2. **Megaline Plan Revenue Analysis (EDA, Forecasting, Hypothesis Testing)**  
3. **Megaline SQL Analysis (SQL + Pandas Revenue Insights)**  

---

## **Project 1: Predicting Ultra Plan Subscription (ML)**

### **Objective**
To predict whether a user will subscribe to the **Ultra mobile plan**, using historical usage data (calls, texts, and mobile data).

### **Methods & Tools**
- **Libraries:** `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- **Models Used:**
  - Decision Tree
  - Random Forest
  - Logistic Regression
  - Gradient Boosting
  - Support Vector Machine (SVM)
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, Confusion Matrices
- **Preprocessing:**
  - Train/Validation/Test split
  - Standardization using `StandardScaler`
  - Hyperparameter tuning via `GridSearchCV`

### **Outcome**
- **Random Forest** and **Gradient Boosting** achieved the best performance.
- Feature importance analysis highlighted **key usage variables** influencing subscriptions.
- Models achieved **>80% accuracy** despite class imbalance.

---

## **Project 2: Megaline Plan Revenue Analysis**

### **Objective**
To analyze and forecast **revenue performance** of Surf and Ultimate plans using historical usage patterns.

### **Methods & Tools**
- **Libraries:** `pandas`, `matplotlib`, `seaborn`, `scipy.stats`, `statsmodels`
- **EDA & Statistical Analysis:**
  - Monthly usage patterns by plan
  - Revenue distribution analysis
  - **Independent t-tests** on:
    - Revenue by plan
    - Revenue by region (e.g., NY-NJ vs others)
- **Forecasting:**  
  - Simulated revenue trends
  - Linear regression fits by plan

### **Outcome**
- **Ultimate plan** shows a **clear revenue advantage** over Surf.
- **Statistically significant revenue differences** between plans and some regions.
- Forecasting suggests a **stable upward trend** for Ultimate plan revenue.

---

## **Project 3: Megaline SQL Analysis**

### **Objective**
To replicate the revenue analysis with a **SQL + Pandas pipeline**, showcasing **real-world database querying**.

### **Workflow**
1. **CSV → SQLite Database**:  
   - All datasets (calls, messages, internet, users, plans) are loaded into `megaline2.db`.
2. **SQL Aggregation:**  
   - Calls, messages, and internet usage are aggregated by `user_id` and `month`.
3. **Revenue Calculation in Pandas:**  
   - Overage charges and monthly revenue per user are calculated using plan rules.
4. **Visualization & Insights:**  
   - Revenue distribution by plan (boxplots, barplots).
   - Hypothesis testing (Surf vs Ultimate revenue).

### **Tech Stack**
- **SQLite (SQL queries for data prep).**
- **Python:** `pandas`, `matplotlib`, `seaborn`, `scipy.stats`.

---

## **Key Insights**
- **Ultimate plan generates higher average revenue per user.**
- **Surf users**, while more numerous, contribute less revenue due to lower base plan costs.
- **Hypothesis testing confirms significant revenue difference** (p < 0.05) between Surf and Ultimate.

---

## **How to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/megaline-telecom-analysis.git
   cd megaline-telecom-analysis
