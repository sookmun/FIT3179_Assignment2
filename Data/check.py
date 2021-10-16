import pandas as pd
import csv
# df= pd.read_csv("world-happiness-report-2021.csv")
# df= pd.read_csv("world-happiness-report-2021.csv")
# highest=df["Healthy_Life_Expectancy"].max()
# lowest=df["Healthy_Life_Expectancy"].min()
df= pd.read_csv("WHOdata.csv")
# new_dataframe = df.filter(["Country","Year","Both sexes"], axis=1)
new_dataframe = df[df.Year.eq(2015)]
# newdf=df[df["Country","Year","Both sexes"]]
# newdf=df["Country","Year","Both sexes"].head()
print(new_dataframe)
new_dataframe.to_csv('2015lifeexpect.csv')