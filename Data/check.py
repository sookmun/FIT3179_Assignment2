import pandas as pd
import csv
df= pd.read_csv("world-happiness-report-2021.csv")
highest=df["Ladder_Score"].max()
lowest=df["Ladder_Score"].min()
print(highest)
print(lowest)
grouped_df = df.groupby("Regional_Indicator")
maximums = grouped_df.max()
minimums =grouped_df.min()
maximums= maximums.filter(["Country_Name","Ladder_Score","Freedom"])
print(maximums)
print(">>>"*20)
minimums= minimums.filter(["Country_Name","Ladder_Score","Freedom"])
print(minimums)
# highest=df.loc[df["Ladder_Score"].max()]
# lowest=df.loc[df["Ladder_Score"].min()]
# # new_dataframe = df.filter(["Country","Year","Both sexes"], axis=1)
# print(highest)
# print(lowest)