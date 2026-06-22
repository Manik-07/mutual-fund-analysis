import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    try:
        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        json_data = response.json()

        # NAV history
        nav_df = pd.DataFrame(json_data["data"])

        filename = f"data/raw/{scheme_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"✓ Saved: {filename}")
        print(nav_df.head())

    except Exception as e:
        print(f"✗ Error downloading {scheme_name}: {e}")