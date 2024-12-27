import numpy as np
a = np.arange(10)
a.shape = 2,5
# print(a)

b = a.reshape(2,5)
# print(b)

# Использование -1 как колличество от второго числа 
# a = a.reshape(-1,5)
# print(a)

# ravel - представление массива в векторе
# a = a.ravel()
# print(a)

# resize -меняет размерность и может добавлять элементы если refcheck=False
a.resize(4,4,refcheck=False)
# print(a)
# print()
# Транспонирование элементов - T (Разворот матрицы)
a = a.T
# print(a)
# [[0 1 2 3]
#  [4 5 6 7]
#  [8 9 0 0]
#  [0 0 0 0]]

# [[0 4 8 0]
#  [1 5 9 0]
#  [2 6 0 0]
#  [3 7 0 0]]

# К вектору можно применить shape для создания однострочной матрицы и траспонировать эту матрицу 
a = np.arange(1,10)
a.shape = 1,-1
a = a.T
# print(a)


x_test = np.arange(32).reshape(8,2,2)

# print(b.shape)
x_test4 = np.expand_dims(x_test,axis=0)

# print(x_test4.shape)
x_test4[0,0,0,0] = -1

# добавление в матрицу элемент по его адресу и оси x

a = np.append(x_test4,x_test4, axis=0)
# print(a.shape)

# Удаление оси из матрицы по его адресу и оси x
b = np.delete(x_test4,0, axis=0)
# print(x_test.shape)

# x = np.arange(1,11)
# x.shape = 2,5
# print(x)

# a = np.append(x,x,axis=1)
# print(a)

# a = np.delete(a,0,axis=0)
# print(a)

# a = np.arange(10)
# a.shape = 2,5
# print(a.shape)
# a = np.expand_dims(a,axis=0)
# a = np.expand_dims(a,axis=-1)
# print(a)

# squeeze - сжимает матрицу (удаляя матрицу с 1 элементом)
# a = np.squeeze(a)
# print(a)
