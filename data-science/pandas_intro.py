import numpy as np
import pandas as pd

my_list = ["Hello world", 4, None, 's', 9.1]
my_series = pd.Series(my_list)
print(my_series)
print(type(my_series))

int_series = pd.Series([1,2,5,3,8,4,7,2,7])
print(int_series)
print(int_series + 1)
print(int_series.mode())
print(int_series.mean())
print(int_series.median())
print(int_series.std())

print(int_series.describe())
print(my_series.info())

print(my_series.isnull().sum())
my_series = my_series.fillna(6)
print(my_series)
print(my_series.isnull().sum())