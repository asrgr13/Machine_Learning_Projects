## Packages for API and Python packages
import yfinance as yf
import pandas as pd
import os

# Date range
# manual dates for prototype purposes
start_date = "2024-01-01"
end_date = "2025-06-10"

# Path to output CSV in the same folder
output_file = os.path.join(os.path.dirname(__file__), "historical_gold_idr.csv")

# Data 1: fetch gold futures (in USD)
gold_df = yf.download("GC=F", start = start_date, end = end_date)

# Data 2: fetch Indonesian rupiah exchange rate
fx_df = yf.download("IDR=X", start = start_date, end = end_date)

# Combine data into single Dataframe
combined = pd.DataFrame({
    "gold_open_usd": gold_df["Open"],
    "gold_high_usd": gold_df["High"],
    "gold_low_usd": gold_df["Low"],
    "gold_close_usd": gold_df["Close"],
    "usd_idr_rate": fx_df["Close"]
})

# Drop rows with missing data
combined.dropna(inplace=True)

# Convert to IDR
combined["gold_open_idr"] = combined["gold_open_usd"] * combined["usd_idr"]
combined["gold_high_idr"] = combined["gold_high_usd"] * combined["usd_idr"]
combined["gold_low_idr"] = combined["gold_low_usd"] * combined["usd_idr"]
combined["gold_close_idr"] = combined["gold_close_usd"] * combined["usd_idr"]

# Reset index to expose 'Date'
combined.reset_index(inplace=True)

# Keep selected columns
combined = combined[[
    "Date",
    "gold_open_idr",
    "gold_high_idr",
    "gold_low_idr",
    "gold_close_idr",
    "usd_idr"
]]

# Save to CSV in the same folder
combined.to_csv(output_file, index=False)
print(f"Saved data to {output_file}")