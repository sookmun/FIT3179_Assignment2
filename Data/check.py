import pandas as pd
# df= pd.read_csv("world-happiness-report-2021.csv")
df= pd.read_csv("2020.csv")
highest=df["Healthy life expectancy"].max()
lowest=df["Healthy life expectancy"].min()
print(highest)
print(lowest)