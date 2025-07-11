# Megaline Plan Revenue Analysis: EDA, Forecasting & A/B Testing

This project analyzes customer behavior and revenue performance for a telecom provider, **Megaline**, to determine which of its two prepaid mobile plans — **Surf** and **Ultimate** — is more profitable. Using user activity data from 500 clients across calls, messages, and internet usage, we perform a complete data workflow including cleaning, analysis, forecasting, and hypothesis testing.

---

## Project Objectives

* Identify which plan (Surf or Ultimate) generates more **average** and **total revenue**
* Understand usage patterns in **calls, messages, and data**
* Detect **statistically significant differences** in revenue across plans and regions
* Explore **monthly trends** to support future **forecasting and strategic planning**
* Deliver **actionable recommendations** for business and marketing decisions

---

##  Tools & Technologies

- **Python (Pandas, NumPy)** – Data manipulation and aggregation  
- **Matplotlib / Seaborn** – Data visualization  
- **SciPy** – Statistical hypothesis testing (Welch’s t-test)  
- **Jupyter Notebook** – Interactive analysis and documentation  

---

##  Key Findings

- **Ultimate plan users** have higher average monthly revenue (~$72) than Surf users (~$58), but the **Surf plan generated more total revenue** due to a larger user base.
- **Ultimate users consistently consume more data and call minutes**, indicating high engagement and stability.
- **Surf users exhibit more variable usage**, often exceeding included limits driving overage fees and revenue spikes.
- A **t-test confirmed a statistically significant difference** in average revenue between plans (p < 0.0001).
- Users from the **NY-NJ region also showed significantly different revenue behavior** compared to users in other regions.
- Trend analysis suggested **Ultimate plan revenue is stable or increasing**, while Surf shows flatter or declining patterns.

---

## Visual Insights

The project includes:
- Line plots of **monthly internet, call, and message usage** by plan
- Revenue distribution histograms by plan
- Linear regression trendlines for **forecasting revenue over time**
- Boxplots and summary tables for visualizing variability
- T-test results for **A/B testing-style comparisons**

---

## Dataset Overview

- `megaline_users.csv` – User demographics and assigned plan  
- `megaline_calls.csv` – Call logs with duration and timestamps  
- `megaline_messages.csv` – SMS usage  
- `megaline_internet.csv` – Internet traffic data per session  
- `megaline_plans.csv` – Plan pricing and allowances  

---

## Business Recommendations

- Promote the **Ultimate plan to high-usage customers** for better revenue stability
- Monitor and optimize **Surf overage pricing**, as it contributes significantly to total revenue
- Explore **region-specific marketing** strategies based on geographic revenue patterns
- Consider adding predictive models for **usage-based churn or plan upgrade targeting**

---
