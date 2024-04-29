import sys

from math import exp, log
from funcs import *
from enter_data import *

def method_sq(xs, ys, m):
    matr = []
    su = [len(xs)]
    for i in range(1, 2*m):
        s = 0
        for z in xs:
            s += z**i
        su.append(s)
    for i in range(0, m):
        matr.append(su[i:i+m])
    v = []
    for i in range(m):
        s = 0
        for z in range(len(xs)):
            s += ys[z]*xs[z]**i
        v.append(s)

    #print(matr)
    #print(v)
    vars = gauss_method(matr, v)
    return vars
    #print(vars)

def lin(xs, ys):

    sr_x = sum(xs)/len(xs)
    sr_y = sum(ys)/len(ys)

    f1 = 0
    f2 = 0
    f3 = 0
    for i in range(len(xs)):
        f1 += (xs[i] - sr_x)*(ys[i] - sr_y)
        f2 += (xs[i] - sr_x)**2
        f3 += (ys[i] - sr_y)**2

    r = f1/(f2*f3)**0.5
    print(f"Коэффициент корреляции: {r}")

    vars = method_sq(xs, ys, 2)
    table = [["№"],["X"],["Y"],["F"],["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[0]*xs[i] + vars[1]))
        table[4].append(str(vars[0]*xs[i] + vars[1] - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*x + b")
    print(f"Коэффициент а = {vars[0]}")
    print(f"Коэффициент b = {vars[1]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i+1])) - float(table[2][i+1]))**2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss/len(xs))**0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss / sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def sq(xs, ys):
    vars = method_sq(xs, ys, 3)
    table = [["№"], ["X"], ["Y"], ["F"], ["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[2] * xs[i]**2 + vars[1]*xs[i] + vars[0]))
        table[4].append(str(vars[2] * xs[i]**2 + vars[1]*xs[i] + vars[0] - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*x^2 + b*x + c")
    print(f"Коэффициент а = {vars[2]}")
    print(f"Коэффициент b = {vars[1]}")
    print(f"Коэффициент c = {vars[0]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i + 1])) - float(table[2][i + 1])) ** 2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss / len(xs)) ** 0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss / sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def cu(xs, ys):
    vars = method_sq(xs, ys, 4)
    table = [["№"], ["X"], ["Y"], ["F"], ["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[3] * xs[i] ** 3 + vars[2] * xs[i]**2 + vars[1]*xs[i] + vars[0]))
        table[4].append(str(vars[3] * xs[i] ** 3 + vars[2] * xs[i]**2 + vars[1]*xs[i] + vars[0] - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*x^3 + b*x^2 + c*x + d")
    print(f"Коэффициент а = {vars[3]}")
    print(f"Коэффициент b = {vars[2]}")
    print(f"Коэффициент c = {vars[1]}")
    print(f"Коэффициент d = {vars[0]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i + 1])) - float(table[2][i + 1])) ** 2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss / len(xs)) ** 0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss/sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def exsp(xs, ys):
    #xs.pop(0)
    #ys.pop(0)
    try:
        YS = list(map(log, ys))
    except:
        print("Для экспоненциальной аппроксимации не должно быть отрицательных значений x")
        return
    vars = method_sq(xs, YS, 2)
    vars[0] = exp(vars[0])
    table = [["№"], ["X"], ["Y"], ["F"], ["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[0]*exp(vars[1]*xs[i])))
        table[4].append(str(vars[0]*exp(vars[1]*xs[i]) - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*e^(bx)")
    print(f"Коэффициент а = {vars[0]}")
    print(f"Коэффициент b = {vars[1]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i + 1])) - float(table[2][i + 1])) ** 2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss / len(xs)) ** 0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss / sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def loga(xs, ys):
    xs.pop(0)
    xs.pop(0)
    try:
        XS = list(map(log, xs))
    except:
        print("Для логарифмической аппроксимации не должно быть отрицательных значений x")
        return
    vars = method_sq(XS, ys, 2)
    vars[0] = exp(vars[0])
    table = [["№"], ["X"], ["Y"], ["F"], ["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[0] * xs[i] + vars[1]))
        table[4].append(str(vars[0] * xs[i] + vars[1] - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*ln(x) + b")
    print(f"Коэффициент а = {vars[0]}")
    print(f"Коэффициент b = {vars[1]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i + 1])) - float(table[2][i + 1])) ** 2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss / len(xs)) ** 0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss / sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def step(xs, ys):
    xs.pop(0)
    xs.pop(0)
    try:
        XS = list(map(log, xs))
        YS = list(map(log, ys))
    except:
        print("Для степенной аппроксимации не должно быть отрицательных значений x и y")
        return
    vars = method_sq(XS, YS, 2)
    vars[0] = exp(vars[0])
    table = [["№"], ["X"], ["Y"], ["F"], ["ei"]]
    for i in range(len(xs)):
        table[0].append(str(i))
        table[1].append(str(xs[i]))
        table[2].append(str(ys[i]))
        table[3].append(str(vars[0] * xs[i]**vars[1]))
        table[4].append(str(vars[0] * xs[i]**vars[1] - ys[i]))

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Уравнение вида y=a*x^b")
    print(f"Коэффициент а = {vars[0]}")
    print(f"Коэффициент b = {vars[1]}")

    sr = 0
    for i in table[3][1:]:
        sr += float(i)
    sr /= len(xs)

    ss = 0
    sss = 0
    for i in range(len(xs)):
        ss += (float((table[3][i + 1])) - float(table[2][i + 1])) ** 2
        sss += (float((table[3][i + 1])) - sr) ** 2
    sigm = (ss / len(xs)) ** 0.5
    print(f"Среднеквадратичное отклонение: {sigm}")

    R = 1 - ss / sss
    print(f"Коэффициент детерминации: {R}")

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")

def main():
    path = enter_path()
    file = open(path, "r")
    try:
        xs = list(map(float, file.readline().split()))
        ys = list(map(float, file.readline().split()))
    except:
        print("Среди введенных значений не только числа")
        sys.exit()
    if len(xs) != len(ys):
        print("Количество значений x не соответствует количеству значений y")
        sys.exit()
    # if len(xs) < 8:
    #     print(f"Значений {len(xs)}, что меньше 8")
    #     sys.exit()
    # if len(xs) > 12:
    #     print(f"Значений {len(xs)}, что больше 12")
    #     sys.exit()
    lin(xs.copy(), ys.copy())
    sq(xs.copy(), ys.copy())
    cu(xs.copy(), ys.copy())
    exsp(xs.copy(), ys.copy())
    loga(xs.copy(), ys.copy())
    step(xs.copy(), ys.copy())


if __name__ == "__main__":
    main()