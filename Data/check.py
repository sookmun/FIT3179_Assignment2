import pandas as pd
# df= pd.read_csv("world-happiness-report-2021.csv")
df= pd.read_csv("world-happiness-report-2021.csv")
highest=df["Healthy_Life_Expectancy"].max()
lowest=df["Healthy_Life_Expectancy"].min()
print(highest)
print(lowest)