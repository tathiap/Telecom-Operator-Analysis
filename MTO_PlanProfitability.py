import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import os

# -------------------------------
# Load Data
# -------------------------------
def load_data():
    base_path = "dataset"
    calls = pd.read_csv(os.path.join(base_path, "megaline_calls.csv"))
    internet = pd.read_csv(os.path.join(base_path, "megaline_internet.csv"))
    messages = pd.read_csv(os.path.join(base_path, "megaline_messages.csv"))
    plans = pd.read_csv(os.path.join(base_path, "megaline_plans.csv"))
    users = pd.read_csv(os.path.join(base_path, "megaline_users.csv"))
    return calls, internet, messages, plans, users

# -------------------------------
# Preprocess and Transform Data
# -------------------------------
def preprocess_data(calls, internet, messages, users):
    # Clean calls
    calls['call_date'] = pd.to_datetime(calls['call_date'])
    calls['duration'] = calls['duration'].apply(np.ceil).replace(0, 1)
    
    # Clean internet
    internet['session_date'] = pd.to_datetime(internet['session_date'])
    
    # Clean messages
    messages['message_date'] = pd.to_datetime(messages['message_date'])

    # Add month
    calls['month'] = calls['call_date'].dt.month
    internet['month'] = internet['session_date'].dt.month
    messages['month'] = messages['message_date'].dt.month
    
    return calls, internet, messages, users

# -------------------------------
# Monthly Aggregation
# -------------------------------
def aggregate_usage(calls, internet, messages):
    calls_monthly = calls.groupby(['user_id', 'month'])['duration'].sum().reset_index(name='total_minutes')
    messages_monthly = messages.groupby(['user_id', 'month']).size().reset_index(name='messages_sent')
    internet_monthly = internet.groupby(['user_id', 'month'])['mb_used'].sum().reset_index(name='data_volume_mb')
    
    # Merge
    df = calls_monthly.merge(messages_monthly, on=['user_id', 'month'], how='outer')
    df = df.merge(internet_monthly, on=['user_id', 'month'], how='outer')
    df = df.fillna(0)
    return df

# -------------------------------
# Merge with User and Plan Info
# -------------------------------
def enrich_with_metadata(df, users, plans):
    df = df.merge(users[['user_id', 'plan', 'city']], on='user_id', how='left')
    df = df.merge(plans, left_on='plan', right_on='plan_name', how='left').drop(columns='plan_name')
    return df

# -------------------------------
# Revenue Calculation
# -------------------------------
def calculate_revenue(df):
    df['excess_minutes'] = (df['total_minutes'] - df['minutes_included']).clip(lower=0)
    df['excess_messages'] = (df['messages_sent'] - df['messages_included']).clip(lower=0)
    df['excess_data_gb'] = ((df['data_volume_mb'] - df['mb_per_month_included']) / 1024).clip(lower=0)

    df['monthly_revenue'] = df['usd_monthly_pay'] + \
        df['excess_minutes'] * df['usd_per_minute'] + \
        df['excess_messages'] * df['usd_per_message'] + \
        df['excess_data_gb'] * df['usd_per_gb']
    
    return df

# -------------------------------
# Revenue Comparison & A/B Test
# -------------------------------
def perform_ab_testing(df):
    surf = df[df['plan'] == 'surf']['monthly_revenue']
    ultimate = df[df['plan'] == 'ultimate']['monthly_revenue']
    t_stat, p_val = ttest_ind(surf, ultimate, equal_var=False)

    print(f"[A/B Test - Plan Revenue] T-statistic: {t_stat:.2f}, p-value: {p_val:.4f}")
    if p_val < 0.05:
        print("✅ Reject H0: Significant difference in revenue between Surf and Ultimate plans.")
    else:
        print("❌ Fail to reject H0: No significant difference in revenue.")

    ny = df[df['city'].str.contains("NY-NJ", na=False)]['monthly_revenue']
    other = df[~df['city'].str.contains("NY-NJ", na=False)]['monthly_revenue']
    t_stat2, p_val2 = ttest_ind(ny, other, equal_var=False)

    print(f"[A/B Test - Region Revenue] T-statistic: {t_stat2:.2f}, p-value: {p_val2:.4f}")
    if p_val2 < 0.05:
        print("✅ Reject H0: Significant revenue difference between NY-NJ and other regions.")
    else:
        print("❌ Fail to reject H0: No significant revenue difference by region.")

# -------------------------------
# Optional: Revenue Distribution Plot
# -------------------------------
def plot_revenue_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='monthly_revenue', hue='plan', kde=True, bins=30, alpha=0.7)
    plt.title('Revenue Distribution by Plan')
    plt.xlabel('Monthly Revenue ($)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    calls, internet, messages, plans, users = load_data()
    calls, internet, messages, users = preprocess_data(calls, internet, messages, users)
    
    usage_df = aggregate_usage(calls, internet, messages)
    enriched_df = enrich_with_metadata(usage_df, users, plans)
    final_df = calculate_revenue(enriched_df)

    print("\n📊 Average Revenue by Plan:")
    print(final_df.groupby('plan')['monthly_revenue'].agg(['mean', 'median', 'sum']))

    perform_ab_testing(final_df)
    plot_revenue_distribution(final_df)
