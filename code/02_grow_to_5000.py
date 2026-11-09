# EC2, step 2: grow from 4 rows to 5,000+ real StatCan points
# Grade 11 code, simple steps, plain comments.
# Source: Statistics Canada Table 20-10-0008-01
# Retail trade sales by industry, monthly
# File: data_full/20100008.csv, downloaded from
# https://www150.statcan.gc.ca/n1/tbl/csv/20100008-eng.zip
# Scope I chose, and why:
# - Seasonally adjusted only, so months can be compared fairly
# - Jan 2012 to Dec 2022, 11 years, monthly
# - Canada, provinces, territories, and big cities, all retail industries
# That scope gives 5,991 rows. That is the number I count.

import pandas as pd
import json

# 1. Load the full StatCan table
df = pd.read_csv("data_full/20100008.csv", low_memory=False)

# 2. Keep only my scope
clean = df[
    (df["Adjustments"] == "Seasonally adjusted")
    & (df["REF_DATE"] >= "2012-01")
    & (df["REF_DATE"] <= "2022-12")
].copy()

# 3. Keep only the columns I need, and give them short names
clean = clean[["REF_DATE", "GEO", "North American Industry Classification System (NAICS)", "VALUE"]]
clean.columns = ["month", "place", "industry", "sales_thousands"]
clean = clean.dropna(subset=["sales_thousands"])

print("Data points in my cleaned dataset:", len(clean))
print("Months:", clean["month"].min(), "to", clean["month"].max())
print("Places:", clean["place"].nunique())
print("Industries:", clean["industry"].nunique())

# 4. Save the cleaned dataset
clean.to_csv("data/retail_2012_2022_clean.csv", index=False)

# 5. March 2020 panic, Canada only, by industry
# Panic score = industry change - total retail change, Feb to Mar 2020
canada = clean[clean["place"] == "Canada"].copy()
pivot = canada.pivot(index="industry", columns="month", values="sales_thousands")
feb = pivot["2020-02"]
mar = pivot["2020-03"]
apr = pivot["2020-04"]
change_mar = (mar - feb) / feb * 100
change_apr = (apr - feb) / feb * 100
total_mar = change_mar["Retail trade [44-45]"]
total_apr = change_apr["Retail trade [44-45]"]
march = pd.DataFrame({
    "change_feb_to_mar_2020_percent": change_mar.round(2),
    "change_feb_to_apr_2020_percent": change_apr.round(2),
    "panic_score_mar": (change_mar - total_mar).round(2),
})
march = march.dropna().sort_values("panic_score_mar", ascending=False)
print("\nTotal retail, Feb to Mar 2020:", round(total_mar, 2), "%")
print("Total retail, Feb to Apr 2020:", round(total_apr, 2), "%")
print(march.head(10))
print(march.tail(10))
march.to_csv("data/march_april_2020_panic_by_industry.csv")

# 6. March 2020 by place, total retail only
total = canada[canada["industry"] == "Retail trade [44-45]"]
place_pivot = clean[clean["industry"] == "Retail trade [44-45]"].pivot(index="place", columns="month", values="sales_thousands")
place_change = ((place_pivot["2020-03"] - place_pivot["2020-02"]) / place_pivot["2020-02"] * 100).round(2)
place_change = place_change.sort_values(ascending=False)
print("\nTotal retail, Feb to Mar 2020, by place:")
print(place_change)
place_change.to_csv("data/march_2020_by_place.csv", header=["change_feb_to_mar_2020_percent"])

# 7. Save the headline numbers
results = {
    "data_points": int(len(clean)),
    "months": "2012-01 to 2022-12",
    "places": int(clean["place"].nunique()),
    "industries": int(clean["industry"].nunique()),
    "total_retail_change_feb_to_mar_2020_percent": round(float(total_mar), 2),
    "total_retail_change_feb_to_apr_2020_percent": round(float(total_apr), 2),
    "top_panic_industry_mar_2020": str(march.index[0]),
    "top_panic_score_mar_2020": float(march.iloc[0]["panic_score_mar"]),
    "top_panic_change_mar_2020_percent": float(march.iloc[0]["change_feb_to_mar_2020_percent"]),
    "lowest_panic_industry_mar_2020": str(march.index[-1]),
    "lowest_panic_score_mar_2020": float(march.iloc[-1]["panic_score_mar"]),
    "source": "Statistics Canada Table 20-10-0008-01, https://www150.statcan.gc.ca/n1/tbl/csv/20100008-eng.zip",
}
with open("data/grown_dataset_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nSaved results:", results)
