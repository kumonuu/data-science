import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr2 = np.arange(1,6,2)
print(arr2)

arr3 = np.linspace(1,10,3)
print(arr3)

arr4 = np.random.randint(5,11,(2,4))
print(arr4)
print(arr4.ndim)

arr5 = np.random.randint(1,31,(4,2,5))
print(arr5)
print(arr5.reshape(20,2))
print(arr5.reshape(40))

arr6 = np.zeros((5),dtype=int)
print(arr6)

arr7 = np.ones((5))
print(arr7)

print(arr5.shape)
print(arr5.size)

# slicing
print(arr[2:4])
print(arr4)
print(arr4[0:1,2:4])