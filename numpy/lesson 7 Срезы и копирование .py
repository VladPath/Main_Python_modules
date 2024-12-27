import numpy as np

a = np.arange(1,11)
a = np.resize(a,(3,3))
# print(a)
# print()
# # print(a[:,0])

# for i in a:
#     for val in i:
#         print(val, end=' ')
#     print()
        #  
        
a = np.arange(1,82).reshape(3,3,3,3)
# print(a[:,1,:,:])
# print(a[1,1,1,1])

# print(a[...,1,1])

a = np.arange(1,11)

# Копирование элемента или среза
v = a[[0,2,4,6]]
v[0] = 2
# print(v)
b_index = [True, False,False,False]

# СОздание списка булевых значений по условию!
# i = v>2
# v = v[i]

# v = v[v>3]
# print(v)

# x = np.array([[10,20],[30,40]])
v = np.arange(2,20)
a = np.array([[1,2],[3,4]])
# print(a)
# print(a[0,1])
# print(v[a])
i1 = [0,1]
i2 = [0,0]
print(a[i1,1])
# print(a)

a[[0,1]] = a[[0,1]] + 1
print(a)

