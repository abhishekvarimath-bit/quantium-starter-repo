import pandas as pd
import glob

files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    all_data.append(df)

# Combine all files
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("formatted_sales_data.csv", index=False)

print("Task completed successfully!")