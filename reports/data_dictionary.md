# Data Dictionary

## Dataset: nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI code for mutual fund |
| date | DATE | Date of NAV record |
| nav | FLOAT | Net Asset Value of fund |

---

## Dataset: investor_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund AMFI code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | FLOAT | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier 1, Tier 2, Tier 3 city classification |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakhs |
| payment_mode | TEXT | UPI, Net Banking, Card, etc. |
| kyc_status | TEXT | KYC verification status |

---

## Dataset: scheme_performance

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund identifier |
| scheme_name | TEXT | Name of mutual fund scheme |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| plan | TEXT | Regular or Direct plan |
| return_1yr_pct | FLOAT | 1-year return percentage |
| return_3yr_pct | FLOAT | 3-year return percentage |
| return_5yr_pct | FLOAT | 5-year return percentage |
| benchmark_3yr_pct | FLOAT | Benchmark return |
| alpha | FLOAT | Alpha metric |
| beta | FLOAT | Beta metric |
| sharpe_ratio | FLOAT | Risk-adjusted return metric |
| sortino_ratio | FLOAT | Downside risk metric |
| std_dev_ann_pct | FLOAT | Annualized standard deviation |
| max_drawdown_pct | FLOAT | Maximum drawdown |
| aum_crore | FLOAT | Assets Under Management (₹ Crore) |
| expense_ratio_pct | FLOAT | Fund expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk category |