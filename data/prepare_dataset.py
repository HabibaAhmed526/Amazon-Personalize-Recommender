import pandas as pd

# Load original MovieLens u.data file
# It's tab-separated with no header
df = pd.read_csv("u.data", sep="\t", header=None)

# Original columns in u.data
df.columns = ["user_id", "item_id", "rating", "timestamp"]

# Select first 1000 rows
df_sample = df.head(1000).copy()

# Add event_type column with value "watch"
df_sample["event_type"] = "watch"

# Select only the required columns for Amazon Personalize
df_final = df_sample[["user_id", "item_id", "timestamp", "event_type"]]

# Save to CSV (no index)
df_final.to_csv("interactions.csv", index=False)

print("Sample saved to interactions_sample.csv")
