def poly_eval(n, a, x):
    if n == 0:
        return a[n]
    else:
        term = a[n] * x**n
        return poly_eval(n-1, a, x) + term
try:
    n = int(input("Введите степень полинома: "))
    a = tuple(map(int, input("Введите коэффициенты полинома через пробел: ").split()))
    x = int(input("Введите значение x: "))
    print(poly_eval(n-1, a, x))
except:
    print('Неверные данные')