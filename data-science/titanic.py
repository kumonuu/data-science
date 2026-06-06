import pandas as pd

dataframe = pd.read_csv("titanic.csv")
#print(dataframe)
print(dataframe.info())
print(dataframe.tail(-1))