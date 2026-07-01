import pandas as pd

df = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High): "
)

recommendations = (
    df[
        df['risk_grade']
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print(
    recommendations[
        [
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]
)