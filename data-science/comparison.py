import numpy as np
from scipy import stats
import time

# list
start_time = time.time()
my_list = []

for i in range(1,100001):
    my_list.append(i)

current_time = time.time() - start_time
print(current_time)

# array
start_time = time.time()
my_arr = np.arange(1,100001)

current_time = time.time() - start_time
print(current_time)

# mathematical operations
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print(np.pi)
print(np.sqrt(4))
print(np.cbrt(8))

print(stats.mode([2,2,6,9,1,2,4,6,4,3,2,2,4,5]))