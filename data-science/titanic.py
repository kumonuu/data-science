import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# age analysis
passengers_over_60 = dataframe[dataframe["Age"] > 60].shape[0]
survived_children = dataframe[(dataframe["Age"] < 12) & (dataframe["Survived"] == 1)].shape[0]
average_age_by_class = dataframe.groupby("Pclass")["Age"].mean()
print(passengers_over_60)
print(survived_children)
print(average_age_by_class)

# gender analysis
females_1stclass = dataframe[(dataframe["Sex"] == "female") & (dataframe["Pclass"] == 1)].shape[0]
survived_males_3rdclass = dataframe[(dataframe["Sex"] == "male") & (dataframe["Pclass"] == 3) & (dataframe["Survived"] == 1)].shape[0]
print(females_1stclass)
print(survived_males_3rdclass)

# fare and survival analysis
average_fare_by_class = dataframe.groupby("Pclass")["Fare"].mean()
highest_fare = dataframe[dataframe["Survived"] == 1]["Fare"].max()
print(average_fare_by_class)
print(highest_fare)

def categorise_fare(fare):
    if fare < 20:
        return "Low"
    elif fare > 20 and fare < 50:
        return "Medium"
    else:
        return "High"

dataframe["FareCategory"] = dataframe["Fare"].apply(categorise_fare)
print(dataframe["FareCategory"].value_counts())

# combined conditional filtering
print(dataframe[(dataframe["Sex"] == "female") & (dataframe["Pclass"] == 1) & (dataframe["Age"] > 50)])
print(dataframe[(dataframe["Age"] < 12) & (dataframe["Pclass"] == 3) & (dataframe["Survived"] == 1)])

average_age = dataframe.groupby(["Pclass", "Sex"])["Age"].mean()
print(average_age)

# condition selection and column extraction
print(dataframe[(dataframe["Age"] > 20) & (dataframe["Age"] < 40)][["Name","Fare"]])
print(dataframe[dataframe["Fare"] > 100][["PassengerId","Name","Pclass"]])
print(dataframe[(dataframe["Survived"] == 1) & (dataframe["Pclass"] == 3)]["Name"])

# slicing and value assignment
dataframe.iloc[0:5,3] = "Test Passenger"
print(dataframe.iloc[0:5,3])
dataframe.loc[10:15,"Fare"] = 999
print(dataframe.loc[10:16,"Fare"])

# create derived columns
dataframe["FarePerPerson"] = dataframe["Fare"] / (dataframe["SibSp"] + 1)
print(dataframe["FarePerPerson"])

def group_ages(age):
    if age < 12:
        return "Child"
    elif age > 12 and age < 18:
        return "Teen"
    else:
        return "Adult"
    
dataframe["AgeGroup"] = dataframe["Age"].apply(group_ages)
print(dataframe["AgeGroup"].value_counts())

print(dataframe.groupby("Sex")[["Age","Fare"]].mean())