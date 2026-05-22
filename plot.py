import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load results (if needed)
result_df = pd.read_csv("results.csv")

# ensure proper datetime type
result_df["date"] = pd.to_datetime(result_df["date"])

# sort (important for time series)
result_df = result_df.sort_values("date")

# set style
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))

sns.lineplot(
    data=result_df,
    x="date",
    y="diacritics_percentage",
    marker="o"
)

plt.title("Share of Diacritics in Personal Names in Latvia’s Population Register")
plt.xlabel("Date")
plt.ylabel("Diacritics Percentage (%)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()