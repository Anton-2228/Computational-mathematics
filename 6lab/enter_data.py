import os
from math import *

# print(e)

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
plt.grid(True)  # Добавляем сетку на график

def enter_var():
    print("Вы хотите ввести уравнение в консоль или прочитать его из файла?\n"
          "Введите 1 - для ввода уравнения через консоль\n"
          "Введите 2 - для чтения уравнения из файла")
    while True:
        var = input()
        if (not (var == "1" or var == "2")):
            print("Вы должны ввести '1' или '2'")
            continue
        break
    return var


def enter_points():
    while True:
        print("Введите уравнение без левой части:")
        ff = input()
        try:
            func = lambda x, y: eval(ff)
            func(2, 2)
        except Exception as e:
            print("Неверный формат функции")
            continue
        break

    while True:
        print("Введите 2 числа - левый x0 и правый xn интервалы включительно")
        try:
            a, b = map(float, input().split())
        except:
            print("Формат ввода неверен")
            continue

        if a >= b:
            print("x0 должен быть меньшее xn")
            continue

        break

    while True:
        print("Введите шаг h:")
        try:
            h = float(input())
        except:
            print("Формат ввода неверен")

        if h <= 0:
            print("Значение h должно быть больше 0")
            continue

        break

    while True:
        print("Введите число y0 - значение в точке x0")
        try:
            y0 = float(input())
        except:
            print("Формат ввода y0 неверный")
            continue
        break

    while True:
        print("Введите число eps - погрешность")
        try:
            eps = float(input())
        except:
            print("Формат ввода eps неверный")
            continue

        if eps <= 0:
            print("Значение eps должно быть больше 0")
            continue
        break


    return a, b, h, func, y0, eps


def enter_path_to_func():
    print("Введите путь до файла\n"
          "Структура файла должна быть такой:\n"
          "в 1 строке через пробел 2 числа: левый x0 и правый xn интервалы включительно\n"
          "во 2 строке шаг h\n"
          "в 3 строке число y0 - значение в точке x0\n"
          "в 4 строке числе eps - погрешность\n"
          "в 5 строке дифференциальное уравнение без левой части")
    while True:
        path = input()
        if not os.path.isfile(path):
            print("Файла по такому пути нет. Повторите ввод:")
            continue

        file = open(path, "r")

        try:
            a, b = map(float, file.readline().split())
        except:
            print("Формат ввода диапазона неверен")
            continue

        if a >= b:
            print("x0 должен быть меньшее xn")
            continue

        try:
            h = float(file.readline())
        except:
            print("Формат ввода шага неверен")
            continue

        if h <= 0:
            print("Значение h должно быть больше 0")
            continue

        try:
            y0 = float(file.readline())
        except:
            print("Формат ввода y0 неверный")
            continue

        try:
            eps = float(file.readline())
        except:
            print("Формат ввода eps неверный")
            continue

        if eps <= 0:
            print("Значение eps должно быть больше 0")
            continue

        ff = file.readline()

        try:
            func = lambda x,y: eval(ff)
            func(2,2)
        except Exception as e:
            print("Неверный формат функции")
            continue
        break

    # xs = []
    # ys = []
    # for i in range((b-a)//h):
    #     p = i*h + a
    #     f = func(p)
    #     xs.append(p)
    #     ys.append(f)

    # xx = np.arange(a,b,(b-a)/1000)
    # yy = []
    # for i in xx:
    #     yy.append(func(i))
    # plt.plot(xx, yy)
    # plt.show()

    return a, b, h, func, y0, eps