import pandas as pd

df = pd.read_csv("titanic.csv")

print(df["Pclass"])

print(df.groupby("Pclass").count())
print(df.groupby("Pclass").get_group(1))
print(df.groupby(["Pclass","Sex"]).get_group((1,"female")))

#print(df["Age"].min())
#df = df.sort_values(["Pclass","Age"],ascending=)
#print(df[["Age","Pclass"]])

df["Sex"] = df["Sex"].replace({
    "male": 0,
    "female": 1
})

df.rename(columns={
    "Sex": "Gender"
})

print(df.agg({
    "Age": ["mean","median"],
    "Fare": ["mean","median"]
}))

df["Fare"] = df["Pclass"] * df["Fare"]
print(df["Fare"])

print(df["Name"])
surnames = df["Name"].str.split(',').str.get(0)
surnames = surnames.value_counts()
print(surnames)