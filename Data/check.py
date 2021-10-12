import pandas as pd
df= pd.read_csv("world-happiness-report-2021.csv")
highest=df["Logged_GDP_per_capita"].max()
lowest=df["Logged_GDP_per_capita"].min()
print(highest)
print(lowest)