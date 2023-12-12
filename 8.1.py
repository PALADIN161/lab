def mean(х, у):
    а_mean = (х + у) / 2
    g_mean = (х * у) ** 0.5
    return а_mean, g_mean
try:
    А = int(input('Введите перменную A: '))
    В = int(input('Введите перменную B: '))
    С = int(input('Введите перменную C: '))
    D = int(input('Введите перменную D: '))

    АВ_а_mean, АВ_g_mean = mean(А, В)
    АС_а_mean, АС_g_mean = mean(А, С)
    АD_а_mean, АD_g_mean = mean(А, D)


    print('Средне арифметическое и среднее геометрическое от A и B: ', round(АВ_а_mean,2), round(АВ_g_mean,2))
    print('Средне арифметическое и среднее геометрическое от A и C: ', round(АС_а_mean,2), round(АС_g_mean,2))
    print('Средне арифметическое и среднее геометрическое от A и D: ', round(АD_а_mean,2), round(АD_g_mean,2))
except:
    print('Неверные данные')