import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science/titanic.csv")
group_by_sex = df.groupby(["Sex","Survived"]).size().unstack()
print(group_by_sex[0])
print(group_by_sex[1])

# plt.figure(figsize=(5,5))
# plt.title("Survival Comparison")
# plt.bar([0,1],group_by_sex[0],width=0.5,label="Did not survive")
# plt.bar([2,3],group_by_sex[1],width=0.5,label="Survived")
# plt.legend()

# plt.show()

values = df["Sex"].value_counts()
print(values)

plt.figure(figsize=(5,5))
plt.title("Pie Chart")
print(values.index)
plt.pie(values,autopct='%.1f%%',labels=values.index)
plt.show()