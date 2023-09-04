import numpy as np

x = [1, 2, 3, 4, 5]
print(type(x))

# to convert list into array
arr = np.array(x)
print(type(arr))
print(arr)

print(np.arange(1, 13))
print(np.arange(1, 13, 2))

print(np.zeros((5,4)))
print(np.ones((3, 4)))

np.random.seed(51)
arr1 = np.random.randint(10, 9999, 50)
print(arr1)
print(arr1.reshape(10, 5))
arr1 = arr1.reshape(10, 5)

# to find max of an array
print(arr1.max())
# to find min of an array
print(arr1.min())
# to find mean of an array
print(arr1.mean())
# to find index of max in an array
print(arr1.argmax())
# to find index of min in an array
print(arr1.argmin())

print(arr1.shape)

row = 3
col = 2
print(arr1[row, col])

# print whole column
print(arr1[:,3])

# print whole row
print(arr1[3,:])

# range of rows and col
print(arr1[0:4,0:3])
print(arr1[0:5 , 0:5])

# modify the range
arr1[0:5, 0:5] = 1
print(arr1)

arr4 = arr1.copy()
print(arr4)