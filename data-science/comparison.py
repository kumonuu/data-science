import time, numpy as np
from scipy import stats
from collections import Counter

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

def mode(data):
    arr = np.array(data)
    arr = arr.flatten()

    my_list = arr.tolist()
    freq = Counter(my_list)
    max_freq = max(freq.values())
    
    modes = [value for value, count in freq.items() if count == max_freq]
    modes.sort()

    if len(modes) == 1:
        return (modes[0],max_freq)
    else:
        return (modes, max_freq)

print(mode([2,2,6,9,1,2,4,6,4,3,2,2,4,5]))
print(mode([1,2,1,2]))