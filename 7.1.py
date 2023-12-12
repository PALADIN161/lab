from random import randint
try:
    N = int(input('Введите размерность матрицы: '))
    lst=[[randint(-9, 9) for i in range(N)] for i in range(N)]
    for i in lst:
        print()
        for j in i:
            print (j, end=" ")
    sum=0
    for i in range(N):
        for j in range(N):
             if (i<j and lst[i][j]<0):
                sum += 1
             else:
                 pass
    print('\nКолличество отрицательных чисел над главной диагональю', sum)
except:
    print('Значения не верны')