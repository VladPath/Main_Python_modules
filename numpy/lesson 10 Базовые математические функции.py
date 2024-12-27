import numpy as np

#  Базовые математические функции по умолчанию всей матрицы 
# с парраметром axis=0 можно выбирать сумму всех столбцов!
# с парраметром axis=1 можно выбирать сумму всех строк!

a = np.array([1,2,3,4,5,6])

# Сумма
print(np.sum(a))
# 21
# средняя арифметическая всего массива
print(np.mean(a))
# 3.5


# минимум и максимум
print(np.min(a))
print(np.max(a))
# 1
# 6

a.resize((3,2))
print(a)
print(np.mean(a))
# [[1 2]
#  [3 4]
#  [5 6]]
# 3.5

print(np.sum(a,axis=0))
# [ 9 12]
print(np.sum(a,axis=1))
# [ 3  7 11]

a = np.array([1,2,-3,4,-5,6.7])
a = a.reshape((3,2))

print(a)
# [[ 1  2]
#  [-3  4]
#  [-5  6]]
print(np.abs(a))
# [[1 2]
#  [3 4]
#  [5 6]]

# arg____ - Возвращение индекса найденного элемента!

# Наибольший и наименьший элемент(его индекс)
print(np.argmax(a))
print(np.argmin(a))
# 5
# 4
print(np.round(0.9))
print(np.round(a))
# 1.0
# [[ 1.  2.]
#  [-3.  4.]
#  [-5.  7.]]

print(np.argmax(a))
print(np.amax(a, axis=0))
print(a)
# 5
# [1.  6.7]
# [[ 1.   2. ]
#  [-3.   4. ]
#  [-5.   6.7]]

# Нахождение синуса по точкам  Быстрее чем встроинные в библиотеку пайтон!!!!1!

points = np.array([0.4, 0.2, 0.4, 0.8])
print(np.sin(points))
# [0.38941834 0.19866933 0.38941834 0.71735609]
print(np.cos(points))
# [0.92106099 0.98006658 0.92106099 0.69670671]

# randint - целое число до x  в параметре size можно указывать размерность!
a = np.random.randint(10)
print(a)
a = np.random.randint(10, size=(2,3))
print(a)
# rand десятичное рандомное число до 1 не включительно и записывая оси матрицы 
a = np.random.rand(2,3,3)
print(a)

# randn

print(np.random.randn(3,2))


# seed позволяет повторять предыдущую генерацию сохраняя её значения

print(np.random.randint(10, size=5))
# [1 4 8 5 6]
np.random.seed(1)
print(np.random.randint(10, size=5))
# [5 8 9 5 0]
np.random.seed(1)
print(np.random.randint(10, size=5))
# [5 8 9 5 0]

a = np.array([1,2,-3,4,-5,6.7])
a = a.reshape((3,2))
print(a)
np.random.shuffle(a)
print(a)

print(np.random.permutation(10))
# [ 9 5 3 0 8 4 2 1 6 7]

a = np.random.randint(20, size=10)
b = np.random.randint(20, size=10)
print(np.median(a))
print(np.var(a))
print(np.std(a))






