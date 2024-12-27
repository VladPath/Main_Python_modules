import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
a = a.reshape(3,3)

# Уникальные значения из массива A! unique
print(np.unique(a))

# возвращает два массива Уникальные значения и колличество повторения значений!
print(np.unique(a, return_counts=True))

# Можно сохранить уникальные значения и вид этого массива из реверса и 
# вернуть обратно этот массив в первоезданный вид!

"""
uniqA, indexA =  np.unique(a, return_inverse=True)
print(uniqA)
print(indexA)

print(uniqA[indexA])
    
"""
a = np.array([0,1,3,4])
b = np.array([1,2,3,4])

# Вхождение множества a в множество b
print(np.isin(a,b))
# [False  True  True  True]

# Пересечение множества а и множества b
print(np.intersect1d(a,b))
# [1 3 4]

# Объединение множества а и множества b
print(np.union1d(a,b))
# [0 1 2 3 4]

# Вычитание множества а и множества b
print(np.setdiff1d(b,a))
# [2]
# 
# Ассимитричная разность XOR уникальные значения а и б
print(np.setxor1d(a,b))
# [0 2]




