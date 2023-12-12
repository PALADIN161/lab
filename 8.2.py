import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

def closest_side_distance(xo, yo, xp, yp):
    AB = distance(xo[0], yo[0], xo[1], yo[1])
    AC = distance(xo[0], yo[0], xo[2], yo[2])
    BC = distance(xo[1], yo[1], xo[2], yo[2])
    p = (AB + AC + BC) / 2
    area = math.sqrt(p * (p - AB) * (p - AC) * (p - BC))
    distances = []
    for i in range(3):
        x1, y1 = xo[i], yo[i]
        x2, y2 = xo[i+1], yo [i+1]
        d = abs((y2-y1)*xp - (x2-x1)*yp + x2*y1 - y2*x1) / distance(x1, y1, x2, y2)
        distances.append(d)
    return min(distances)

# Пример использования
xo = [0, 3, 1]
yo = [0, 0, 2]
xp = 2
yp = 1
print(closest_side_distance(xo, yo, xp, yp)) # находим минимальное расстояние