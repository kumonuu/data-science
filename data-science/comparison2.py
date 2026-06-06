import numpy as np
import pandas as pd
import time

start_time = time.time()
arr = np.arange(1,100001)
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
series = pd.Series(arr)
elapsed_time = time.time() - start_time
print(elapsed_time)

arr2 = np.array([1,2,3])
series2 = pd.Series(arr2)
print(arr2)
arr2[0] = 20
print(arr2)
print(series2)

alphabet = pd.read_excel("alphabet.xlsx")
print(alphabet)
print(type(alphabet))