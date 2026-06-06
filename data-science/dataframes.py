import pandas as pd

my_dict = {
    "Name": ["Emma","Catherine","Emma","Michael"],
    "Age": [13,15,None,16],
    "Hobbies": ["Singing","Dancing","Writing","Drawing"],
    "Grade": ["C","D","A","F"]
}

my_2dlist = [
    ["hello world", 123, True, '+'],
    ["foo", False, "bar", 84.1],
    ]

my_dataframe = pd.DataFrame(my_dict)
print(my_dataframe)
print(my_dataframe["Name"])
print(my_dataframe.columns)
print(my_dataframe.info())
print(my_dataframe.isnull().sum())
print(my_dataframe[(my_dataframe["Name"] == "Emma") & (my_dataframe["Age"] > 12)])
print(my_dataframe.iloc[2:4,0:2])

my_dataframe2 = pd.DataFrame(my_2dlist,columns=["column 1", "column 2", "column 3", "column 4"])
print(my_dataframe2)
#my_dataframe2 = my_dataframe2.drop(columns=["column 1", "column 2"])
print(my_dataframe2)

print(my_dataframe.dropna())
my_dataframe2["column 5"] = pd.Series([2.1, "jetlearn"])
print(my_dataframe2)
my_dataframe2.insert(0,"column 0",pd.Series(["goodbye world", "bar"]))
print(my_dataframe2)

my_dataframe2.to_csv("my_csvfile.csv",index=False)