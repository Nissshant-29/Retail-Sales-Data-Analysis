# Retail Sales Analysis - Python
# Install dependencies: pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv", parse_dates=["order_date"])

# Basic data checks
print("Rows:", len(df))
print("Missing values:\n", df.isna().sum())
print("\nKPI summary:")
print({
    "orders": df["order_id"].nunique(),
    "units_sold": int(df["quantity"].sum()),
    "total_revenue": float(df["revenue"].sum()),
    "average_order_value": round(float(df["revenue"].mean()), 2)
})

# Monthly revenue
monthly = df.assign(month=df["order_date"].dt.to_period("M").astype(str)).groupby("month")["revenue"].sum()
monthly.to_csv("monthly_revenue.csv", header=True)
monthly.plot(kind="line", marker="o", title="Monthly Revenue Trend")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

# Product performance
product_sales = df.groupby("product", as_index=False).agg(
    revenue=("revenue", "sum"),
    units_sold=("quantity", "sum")
).sort_values("revenue", ascending=False)
product_sales.to_csv("product_performance.csv", index=False)
print("\nProduct performance:\n", product_sales)

# Regional performance
region_sales = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
print("\nRegional performance:\n", region_sales)
