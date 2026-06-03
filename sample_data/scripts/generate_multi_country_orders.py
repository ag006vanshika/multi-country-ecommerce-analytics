import pandas as pd
import random
import numpy as np

# ==========================================
# CONFIG
# ==========================================

INPUT_FILE = "sample_data/source/Amazon_4_Raw.xlsx"
OUTPUT_FILE = "sample_data/orders/orders_multicountry.csv"

random.seed(42)

# ==========================================
# REGION DATA
# ==========================================

india_states = [
    "Delhi",
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "Gujarat"
]

uk_counties = [
    "London",
    "Manchester",
    "Liverpool",
    "Leeds",
    "Birmingham"
]

canada_provinces = [
    "Ontario",
    "Quebec",
    "British Columbia",
    "Alberta",
    "Manitoba"
]

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_excel(INPUT_FILE)

# ==========================================
# COUNTRY DISTRIBUTION
# ==========================================

countries = np.random.choice(
    ["India", "UK", "Canada"],
    size=len(df),
    p=[0.4, 0.3, 0.3]
)

df["country"] = countries

# ==========================================
# SCHEMA EVOLUTION
# ==========================================

df["state"] = None
df["county"] = None
df["province"] = None

for idx, row in df.iterrows():

    if row["country"] == "India":
        df.at[idx, "state"] = random.choice(india_states)

    elif row["country"] == "UK":
        df.at[idx, "county"] = random.choice(uk_counties)

    elif row["country"] == "Canada":
        df.at[idx, "province"] = random.choice(canada_provinces)

# ==========================================
# RENAME COLUMNS
# ==========================================

rename_map = {
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Ship Date": "ship_date",
    "EmailID": "customer_id",
    "Geography": "geography",
    "Category": "category",
    "Product Name": "product_name",
    "Sales": "sales",
    "Quantity": "quantity",
    "Profit": "profit"
}

df.rename(columns=rename_map, inplace=True)

# ==========================================
# CREATE BAD RECORDS (1%)
# For Glue Validation Demo
# ==========================================

bad_records_count = max(1, int(len(df) * 0.01))

bad_indices = random.sample(
    list(df.index),
    bad_records_count
)

for idx in bad_indices:

    error_type = random.choice([
        "negative_sales",
        "missing_customer",
        "missing_country"
    ])

    if error_type == "negative_sales":
        df.at[idx, "sales"] = -100

    elif error_type == "missing_customer":
        df.at[idx, "customer_id"] = None

    elif error_type == "missing_country":
        df.at[idx, "country"] = None

# ==========================================
# SAVE
# ==========================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("Multi-country dataset generated successfully")
print(f"Records: {len(df)}")
print(f"Output: {OUTPUT_FILE}")
print("=" * 50)