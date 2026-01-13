import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD & CLEAN DATA
# =========================
df = pd.read_csv("temperature_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Fix temperature values like "(0.3)"
df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
    .astype(float)
)

# Create date column
df["date"] = pd.to_datetime(df["year"].astype(str) + "/" + df["day"])
df["month"] = df["date"].dt.month

# =========================
# 1. OVERALL AVERAGE TEMP
# =========================
overall_avg = df["temperature"].mean()
print(f"\nAverage temperature (entire dataset): {overall_avg:.2f}°C")

# =========================
# 2. MONTHLY AVERAGE TEMP
# =========================
monthly_avg = df.groupby("month")["temperature"].mean()
print("\nMonthly average temperatures:")
print(monthly_avg)

# Bar plot
plt.figure(figsize=(10,5))
monthly_avg.plot(kind="bar", color="skyblue")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()

# =========================
# 3. HOTTEST & COLDEST DAY
# =========================
hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\nHottest Day (Full Row):")
print(hottest_day)

print("\nColdest Day (Full Row):")
print(coldest_day)

# =========================
# 4. TEMPERATURE TREND
# =========================
plt.figure(figsize=(12,5))
plt.plot(df["date"], df["temperature"], color="orange")
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# =========================
# 5. SEASONAL AVERAGES
# =========================
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["month"].apply(get_season)

seasonal_avg = df.groupby("season")["temperature"].mean()
print("\nSeasonal average temperatures:")
print(seasonal_avg)
