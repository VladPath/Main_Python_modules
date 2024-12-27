import numpy as np
# Операции арифметического вычисления

a = np.arange(1,5).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
# Размерности должны совпадать
# объединение горизонтальное - hstack
c = np.hstack((a,b))
# print(c)
# объединение вертикальное - vstack
c = np.vstack((a,b))
# print(c)

# объединение коллонами - column_stack

# a = np.fromiter([1,2,3,4,5],dtype='int32').reshape(1,-1)
# b = np.fromiter(range(6,11),dtype='int32').reshape(1,-1)

# c = np.column_stack((a,b))
# print(c)
# c = np.row_stack((a,b))
# print(c)

a = np.arange(1,31)
b = np.arange(31,61)
a.resize(3,3,2)
b.resize(3,3,2)
# print(a)
# print(b)
# concatenate((a,b), axis=0) - Объединение матрицы с любой размерностью по её оси
c = np.concatenate((a,b),axis=2)
# print(c)

# r_ - делает объединение по 0 оси 
a = np.r_[1:11,100,200]
# print(a)

a = np.r_[[(1,2,3),(4,5,6)],[(7,8,9)]]
# print(a)

# с_ - Делает объединение по 1 оси
a = np.c_[1:5]
b = np.c_[5:9]

c = np.concatenate((a,b),axis=1)
c = np.column_stack((a,b))
# print(c)


# hsplit/vsplit/array_split - делит матрицу пополам 
a = np.r_[1:11]
a = np.resize(a,(2,2,3,2))
# c = np.vstack(np.split(a,2))
# c = np.array_split(a,5,axis=0)
print(c)


