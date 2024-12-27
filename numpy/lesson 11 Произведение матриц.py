import numpy as np 

a = np.array([1,2,3,4,5,6,7,8,9])
a = a.reshape((3,3))

b = np.array([10,11,12,13,14,15,16,17,18])
b = b.reshape((3,3))

a = np.array([1,2,3])

b = np.array([10,20,30])
"""
Матричное умножение (Размерности должны совпадать!)
вариант 1
print(np.dot(a,b))
[[ 84  90  96]
 [201 216 231]
 [318 342 366]]
вариант 2 (Предпочтительнее!!!)
print(np.matmul(a,b))
[[ 84  90  96]
 [201 216 231]
 [318 342 366]]
"""

"""
Внутреннее и внешнее умножение векторов inner and outer

print(np.inner(a,b))
print(np.outer(a,b))

"""

"""
Умножение вектора на матрицу @ or dot()
"""

a = np.array([1,2])
b = np.array([4,5,6,7,8,9])
b.shape = 3,2
print(a)
print(b)
print(b@a)








