import matplotlib.pyplot as plt
import pandas as pd

values = pd.read_csv("data-science/expenses.csv")
colors = ["blue","hotpink","red","yellow","cyan"]
explode = [0.1,0.1,0.1,0.1,0.1]

print(values)

plt.figure(figsize=(5,5))
plt.title("Monthly Household Expense Breakdown")
plt.pie(values["Amount"],autopct='%.1f%%',
labels=values["Expense"],startangle=90,shadow=True,colors=colors,explode=explode)
plt.show()