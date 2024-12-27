import numpy as np 

# ---------- 
# nan - not a number
# inf - infinity number
#  ~ - Инвертация буллевых значение в np был True стал False

a = np.array([1,2,3])
b = [2,3,4]

# Операции сравнения
print(a==b)
print(np.equal(a,b))
# [False False False]
print(a>b)
print(np.greater(a,b))
# [False False False]
print(a<b)
print(np.less(a,b))
# [ True  True  True]
print(a!=b)
# [ True  True  True]

# Какой либо удволетворяет условию
# a == [1,2,3]
print(np.any(a>2))
# True 

# все элементы удволетворяет условию
# a == [1,2,3]
# b == [2,3,4]
print(np.all(a==b))
# False 

c = np.array([1,2, np.nan, np.inf, -np.inf])
d = np.array([1+2.j, 3+1.j, 5])

print(c)
# функция проверка что число inf
print(np.isinf(c))

# функция проверка что число nan
np.isnan(c)
# [False False True  False  False]

# функция проверка что это число
np.isfinite(c)
# [True True False  False  False]

# Инвертируем значения в массиве и выводим все кроме nan
arg = np.isnan(c)
print(c[~arg])
# [  1.   2.  inf -inf]

# Инвертируем значения в массиве и выводим все кроме inf
arg = np.isinf(c)
print(c[~arg])
# [  1.   2.  nan]

# Инвертируем значения в массиве и выводим числа
arg = np.isfinite(c)
print(c[arg])
# [  1.   2.  nan]


# функция проверка что это комплексно число
print(np.iscomplex(d))
# [True True False  False  False]

# функция проверка что это настоящее число
print(np.isreal(d))
# [True True False  False  False]

print(np.isreal(c))

x = np.array([True,False])
y = np.array([False,True])

print(np.logical_and(x,y))
print(np.logical_not(x,y))
print(np.logical_or(x,y))
print(np.logical_xor(x,y))