from random import randint
try:
    R = int(input('Введите кол-во строк в матрице: '))
    N = int(input('Введите кол-во столбцов в матрице: '))
    lst=[[randint(0, 5) for i in range(N)] for i in range(R)]
    for i in lst:
        for j in i:
            print (j, end=" ")
        print()
        kol = 0

    for j in range(N):
        for i in range(R):
            if lst[i][j] == 0:
                kol += 1
                break
            else:
                pass
    a = N - kol
    print('Колличесво столбцов не содержащих 0: ',a)
except:
    print('Неверные данные')