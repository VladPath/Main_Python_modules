import numpy as np 

# С одинаковыми типамы
# a = np.array([1,2,3])
# b = np.array([1,2,3])
# print(b)

# если объекты разные, то он произойдет формирование в один тик как тут в строки
# a = np.array([1,2,'3', True])
# print(a)

# с помощью True or false мы можем удалять или добавлять елементы 

# b  = b[[True,False,True]]
# print(b)

b = np.array([1,2,3,4,5,6,7,8,9])
print(b)

b = b.reshape(3,3)
print(b)
