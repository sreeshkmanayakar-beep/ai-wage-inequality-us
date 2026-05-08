import pandas as pd
import numpy as np
from statsmodels.api import OLS, add_constant
from pathlib import Path

OUT = Path("output")
OUT.mkdir(exist_ok=True)

def build_panel():
    years = list(range(2010, 2025))
    ai = [0.05, 0.09, 0.13, 0.18, 0.24, 0.30, 0.36, 0.42, 0.47, 0.52, 0.57, 0.60, 0.61, 0.63, 0.65]
    wage_gap = [4.70, 4.66, 4.61, 4.55, 4.48, 4.42, 4.35, 4.30, 4.27, 4.28, 4.24, 4.22, 4.20, 4.19, 4.19]
    high = [34.32, 35.10, 36.00, 37.05, 38.10, 39.10, 40.25, 41.20, 42.30, 43.35, 44.35, 45.55, 46.65, 48.10, 49.65]
    middle = [17.53, 18.15, 18.90, 19.55, 20.20, 20.85, 21.50, 22.10, 22.75, 23.30, 23.95, 24.45, 25.05, 25.55, 26.02]
    low = [11.30, 11.85, 12.40, 13.00, 13.55, 14.10, 14.75, 15.40, 15.95, 16.55, 17.10, 17.55, 17.95, 18.12, 18.24]
    p10 = [8.51, 8.78, 9.05, 9.34, 9.72, 10.10, 10.55, 11.05, 11.55, 12.10, 12.60, 13.10, 13.75, 14.10, 14.42]
    p90 = [39.97, 40.60, 41.25, 42.10, 43.05, 44.10, 45.00, 46.00, 47.10, 48.25, 49.50, 51.00, 53.25, 56.10, 60.44]

    df = pd.DataFrame({
        "year": years,
        "ai_index": ai,
        "wage_gap": wage_gap,
        "high_skill": high,
        "middle_skill": middle,
        "low_skill": low,
        "p10_wage": p10,
        "p90_wage": p90
    })

    df["ai_lag1"] = df["ai_index"].shift(1)
    df["high_growth_pct"] = (df["high_skill"] / df["high_skill"].iloc[0] - 1) * 100
    df["middle_growth_pct"] = (df["middle_skill"] / df["middle_skill"].iloc[0] - 1) * 100
    df["low_growth_pct"] = (df["low_skill"] / df["low_skill"].iloc[0] - 1) * 100
    df["p10_growth_pct"] = (df["p10_wage"] / df["p10_wage"].iloc[0] - 1) * 100
    df["p90_growth_pct"] = (df["p90_wage"] / df["p90_wage"].iloc[0] - 1) * 100
    return df

def main():
    df = build_panel()
    df.to_csv(OUT / "ai_wage_inequality_panel.csv", index=False)

    m1 = OLS(df["wage_gap"], add_constant(df["ai_index"])).fit(cov_type="HC1")
    m2 = OLS(df["wage_gap"].iloc[1:], add_constant(df["ai_lag1"].iloc[1:])).fit(cov_type="HC1")

    reg = pd.DataFrame([
        {
            "model": "current_ai",
            "coef": m1.params["ai_index"],
            "robust_se": m1.bse["ai_index"],
            "r2": m1.rsquared,
            "n": int(m1.nobs)
        },
        {
            "model": "lagged_ai",
            "coef": m2.params["ai_lag1"],
            "robust_se": m2.bse["ai_lag1"],
            "r2": m2.rsquared,
            "n": int(m2.nobs)
        }
    ])

    reg.to_csv(OUT / "ai_wage_regression_results.csv", index=False)
    df.to_csv(OUT / "ai_wage_figure_data.csv", index=False)

    print(reg.round(4).to_string(index=False))

if __name__ == "__main__":
    main()
