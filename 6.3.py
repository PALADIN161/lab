import random

a = [ 1.4, 2, 3, 0, 4, 0, 0, 24, 13, 4.5, 3.4]
print('Сумма элементов после 0:',sum(a[a.index(0):]))
b = [random.randint(-100,100) for j in range (10)]
print('Случайная матрица',b)
S = 0
for item in b:
    if item >0:
        S += 1
print('Колличество положительных элементов',S)

