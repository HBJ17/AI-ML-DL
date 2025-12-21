import pandas as pd

data = pd.read_csv(r"D:\Studies\Projects\Python\AI-ML-DL\Yt_Ig_Analysis\Yt_Ig_data.csv")
print(data)

data["engagement_rate"] = (data["likes"] + data["comments"] + data["shares"]) / data["views"]

print(data[["platform", "content_type", "engagement_rate"]])

avg_views = data.groupby("platform")["views"].mean()
print("Average Views by Platform:")
print(avg_views)

content_performance = data.groupby("content_type")["views"].mean()
print("Average Views by Content Type:")
print(content_performance)

import matplotlib.pyplot as plt

# Content Type vs Average Views
plt.bar(content_performance.index, content_performance.values)
plt.xlabel("Content Type")
plt.ylabel("Average Views")
plt.title("Content Type vs Average Views")
plt.show()

# Platform vs Average Views
plt.bar(avg_views.index, avg_views.values)
plt.xlabel("Platform")
plt.ylabel("Average Views")
plt.title("Platform vs Average Views")
plt.show()


