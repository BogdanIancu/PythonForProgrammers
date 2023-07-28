import numpy as np

array1 = np.array([4, 5, 6])
array2 = np.zeros(3)
print(np.sum(array1))
array2[1] = 9.99999999
array2[2] = 7.2
print(np.round(array2))
print(np.std(array1))
print(array1 + array2)

my_matrix = np.array([[1, 2, 3, 4], [8, 9, 10, 11]])

print(my_matrix)
print(my_matrix * my_matrix)
print(my_matrix - my_matrix)
print(1 / my_matrix)
print(my_matrix ** 3)
