import numpy as np 

a = np.arange(0.1,1,0.1)
print(a)

# Изменение типа записи данных
a.dtype = np.float32()
print(a)
a.dtype = np.float64()
print(a)

# размерность
print(a.size)

# Вес переменной в байтах
print(a.itemsize)


a = np.ones((3,3,4))
print(a)

print("ndim - показывает количество осей -", a.ndim)

print('shape - Показывает размерность осей -',a.shape)

"shape - форматирует массив по колличеству объектов!"
a.shape = 36
print(a)

print('Форматирую из одно осевой матрицы в двух осевую')
x = 4
a.shape = x, int(a.shape[0]//x)
print(a)
print(int(a.shape[0]/2))


a = np.arange(1,37)
print('a это одномерная матрица \n',a)
print("reshape - a на двухмерную матрицу ")
b = a.reshape(6,6)
print(b)

print("reshape - a на трехмерную матрицу ")
c = a.reshape(3,3,4)
print(c)

print('--------------------------------------')
# print(a)
d = a
d = a.reshape(6,6)

print(a)
print(d)

