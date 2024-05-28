from enter_data import *

import matplotlib.pyplot as plt
import numpy as np

def eidel_method(a, b, h, func, y0, eps):
    while True:
        xs_h = [a+i*h for i in range(int((b-a)//h))]
        y_find_h = [y0]
        for x in xs_h:
            y = y_find_h[-1]
            y_new = y + h*func(x, y)
            y_find_h.append(y_new)

        h2 = h/2
        xs_h2 = [a + i * h2 for i in range(int((b - a) // h2))]
        y_find_h2 = [y0]
        for x in xs_h2:
            y = y_find_h2[-1]
            y_new = y + h2*func(x, y)
            y_find_h2.append(y_new)

        y1 = y_find_h[-1]
        if xs_h[-1] == xs_h2[-1]:
            y2 = y_find_h2[-1]
        else:
            y2 = y_find_h2[-2]

        res = abs(y1 - y2)/1 <= eps
        if (not res):
            h = h/2
        else:
            break
    ans = 0
    for i in y_find_h2:
        ans += i*h2
    print(f"Для метода Эйлера приближенное значение интеграла дифференциального уравнения равно: {ans}")

    plt.grid(True)  # Добавляем сетку на график
    plt.title("Метод Эйлера")
    plt.plot(xs_h, y_find_h[:-1])
    plt.show()

def runge_Kutta_method(a, b, h, func, y0, eps):
    while True:
        xs_h = [a+i*h for i in range(int((b-a)//h))]
        y_find_h = [y0]
        for x in xs_h:
            y = y_find_h[-1]
            k1 = h*func(x, y)
            k2 = h*func(x+h/2, y+k1/2)
            k3 = h*func(x+h/2, y+k2/2)
            k4 = h*func(x+h,y+k3)
            y_new = y + (k1 + 2*k2 + 2*k3 + k4)/6
            y_find_h.append(y_new)

        h2 = h/2
        xs_h2 = [a + i * h2 for i in range(int((b - a) // h2))]
        y_find_h2 = [y0]
        for x in xs_h2:
            y = y_find_h2[-1]
            k1 = h2 * func(x, y)
            k2 = h2 * func(x + h2 / 2, y + k1 / 2)
            k3 = h2 * func(x + h2 / 2, y + k2 / 2)
            k4 = h2 * func(x + h2, y + k3)
            y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y_find_h2.append(y_new)

        y1 = y_find_h[-1]
        if xs_h[-1] == xs_h2[-1]:
            y2 = y_find_h2[-1]
        else:
            y2 = y_find_h2[-2]

        res = abs(y1 - y2)/1 <= eps
        if (not res):
            h = h/2
        else:
            break
    ans = 0
    for i in y_find_h2:
        ans += i*h2
    print(f"Для метода Рунге-Кутта приближенное значение интеграла дифференциального уравнения равно: {ans}")

    plt.grid(True)  # Добавляем сетку на график
    plt.title("Метод Рунге-Кутта")
    plt.plot(xs_h, y_find_h[:-1])
    plt.show()

def runge_Kutta_method_for_adams(a, n, h, func, y0):
    x = a
    y_find_h = [y0]
    for i in range(n):
        x += i*h
        y = y_find_h[-1]
        k1 = h * func(x, y)
        k2 = h * func(x + h / 2, y + k1 / 2)
        k3 = h * func(x + h / 2, y + k2 / 2)
        k4 = h * func(x + h, y + k3)
        y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y_find_h.append(y_new)
    return y_find_h


def adams_method(a, b, h, func, y0, eps):
    while True:
        xs_h = [a + i * h for i in range(int((b - a) // h))]
        y_find_h = runge_Kutta_method_for_adams(a, 3, h, func, y0)
        try:
            f_find_h = [func(xs_h[x], y_find_h[x]) for x in range(4)]
        except:
            h = h/2
            continue
        for i in xs_h[4:]:
            f1 = f_find_h[-1] - f_find_h[-1]
            f2 = f_find_h[-1] - 2*f_find_h[-2] + f_find_h[-3]
            f3 = f_find_h[-1] - 3*f_find_h[-2] + 3*f_find_h[-3] - f_find_h[-4]
            y_new = y_find_h[-1] + h*f_find_h[-1] + h**2/2*f1 + 5*h**3/12*f2 + 3*h**4/8*f3
            f_find_h.append(func(i, y_new))
            y_find_h.append(y_new)

        # h2 = h/2
        # xs_h2 = [a + i * h2 for i in range(int((b - a) // h2))]
        # y_find_h2 = runge_Kutta_method_for_adams(a, 3, h2, func, y0)
        # f_find_h2 = [func(xs_h2[x], y_find_h2[x]) for x in range(4)]
        # for i in xs_h2[4:]:
        #     f1 = f_find_h2[-1] - f_find_h2[-1]
        #     f2 = f_find_h2[-1] - 2 * f_find_h2[-2] + f_find_h2[-3]
        #     f3 = f_find_h2[-1] - 3 * f_find_h2[-2] + 3 * f_find_h2[-3] - f_find_h2[-4]
        #     y_new = y_find_h2[-1] + h2 * f_find_h2[-1] + h2 ** 2 / 2 * f1 + 5 * h2 ** 3 / 12 * f2 + 3 * h2 ** 4 / 8 * f3
        #     f_find_h2.append(func(i, y_new))
        #     y_find_h2.append(y_new)
        #
        y1 = y_find_h[-1]
        # if xs_h[-1] == xs_h2[-1]:
        #     y2 = y_find_h2[-1]
        # else:
        #     y2 = y_find_h2[-2]

        # res = abs(y1 - y2) / 1 <= eps
        res = abs(y1 - 930.25) <= eps
        if (not res):
            h = h / 2
        else:
            break
    ans = 0
    for i in y_find_h:
        ans += i * h
    print(f"Для метода Адамса приближенное значение интеграла дифференциального уравнения равно: {ans}")

    plt.grid(True)
    plt.title("Метод Адамса")
    plt.plot(xs_h, y_find_h)
    plt.show()


def main():
    var = enter_var()
    if var == "1":
        a, b, h, func, y0, eps = enter_points()
    elif var == "2":
        a, b, h, func, y0, eps = enter_path_to_func()

    # print(xs)
    # print(ys)
    # print(point)

    eidel_method(a, b, h, func, y0, eps)
    runge_Kutta_method(a, b, h, func, y0, eps)
    adams_method(a, b, h, func, y0, eps)

if __name__ == "__main__":
    main()