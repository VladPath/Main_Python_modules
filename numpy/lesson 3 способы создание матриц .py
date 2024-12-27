import numpy as np
a = np.empty(4, 'int16')
print('одномерная из рандомных чисел\n', a)

b = np.ones((3,3,3))
print('Трехмерная из единиц\n',b)

c = np.zeros([2,2])
print('Двухмерная из нулей\n',c)

d = np.identity(5)
print('Двумерная квадратная из единиц по главной диаганали\n',d)

e = np.eye(10,10)
print('матрица с единицами по главной диаганали \n',e)

asmatrix = np.asmatrix('1,2;3,4;5,6')
print("На основе строки с разделением ; создает матрицу\n ",asmatrix)

diag = np.diag((1,2,3,4,5))
print('Функция создает матрицу с диаганалью на основе вводных данных\n',diag)



tr = np.tri(5,5)
print("""Создаст матрицу где 
под главной диагональю будут единицы, а над нули\n""",tr)

tru = np.triu([1,2,3])
print("""Создаст матрицу где 
под главной диагональю будут нули, а над значения\n""",tru)


print('arange - Как range, только допускаются вещественные числа\n',np.arange(1,np.pi,0.1))


print("""linspase -  как arange только не с ходом а с делением чисел 
      """,np.linspace(0,10,5) )


print("""logspace - как linspace  но логорифмическое значение!
      """, np.logspace(0,10,5,dtype='int64'))

print("""geaomspace - как linspace  но геометрическаое прогресия!
      """, np.logspace(0,10,5,dtype='int64'))



print('----------\n Копия массива')

a = np.array(([1,2,3],[1,2,3]))
b = np.copy(a)
b[0] = 100

print(a)
print(b)

print('----------\n Массив из функции')

def get_range(x,y):
    return 100*x + y


a = np.fromfunction(get_range,(2,2))
print(a)

print('С помощю лямбда функции \n',np.fromfunction( lambda x,y: 100*x + y, (2,2)))


print('----------\n Массив из Итерации ')
print(""" fromiter - С помощью итерации объектов
      """, np.fromiter('hello', dtype='U1'))


a = np.fromiter([i for i in range(1,11)], dtype='int8')
print(a)


print('----------\n Массив из строк ')
print(""" fromstring - С помощью итерации строк
      """, np.fromstring('1,2,3,4,5,6',sep=','))




