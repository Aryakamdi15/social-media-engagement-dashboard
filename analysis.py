import pandas as pd

# Load the dataset
df = pd.read_csv("data/youtube_data.csv")

# Convert numeric columns
df["Views"] = pd.to_numeric(df["Views"])
df["Likes"] = pd.to_numeric(df["Likes"])
df["Comments"] = pd.to_numeric(df["Comments"])

# Calculate engagement rate
df["Engagement Rate (%)"] = (
    (df["Likes"] + df["Comments"]) / df["Views"] * 100
).round(2)

# Convert published date
df["Published"] = pd.to_datetime(df["Published"])

# Extract day and hour
df["Day"] = df["Published"].dt.day_name()
df["Hour"] = df["Published"].dt.hour

print("\n===== SUMMARY =====")
print("Total Videos :", len(df))
print("Total Views :", df["Views"].sum())
print("Total Likes :", df["Likes"].sum())
print("Total Comments :", df["Comments"].sum())

print("\nAverage Engagement Rate:")
print(df["Engagement Rate (%)"].mean())

print("\nBest Posting Day:")
print(df.groupby("Day")["Engagement Rate (%)"].mean().sort_values(ascending=False))

print("\nBest Posting Hour:")
print(df.groupby("Hour")["Engagement Rate (%)"].mean().sort_values(ascending=False))