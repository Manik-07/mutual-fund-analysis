-- 1. Top 5 Funds by AUM
SELECT scheme_name,
       fund_house,
       aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Per Month
SELECT strftime('%Y-%m', date) AS month,
       ROUND(AVG(nav), 2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- 3. SIP Transaction Volume
SELECT ROUND(SUM(amount_inr), 2) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type = 'SIP';

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio Less Than 1%
SELECT scheme_name,
       expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 10 Funds by 1-Year Return
SELECT scheme_name,
       return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 7. Average Expense Ratio by Category
SELECT category,
       ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM scheme_performance
GROUP BY category
ORDER BY avg_expense_ratio;

-- 8. Transaction Amount by Type
SELECT transaction_type,
       ROUND(SUM(amount_inr), 2) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;

-- 9. Average 3-Year Return by Fund House
SELECT fund_house,
       ROUND(AVG(return_3yr_pct), 2) AS avg_return_3yr
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return_3yr DESC;

-- 10. Investor Distribution by City Tier
SELECT city_tier,
       COUNT(DISTINCT investor_id) AS total_investors
FROM investor_transactions
GROUP BY city_tier
ORDER BY total_investors DESC;