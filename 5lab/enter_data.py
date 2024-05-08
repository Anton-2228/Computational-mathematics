import os
from math import *

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
plt.grid(True)  # Добавляем сетку на график

def enter_var():
    print("Вы хотите ввести точки в консоль, прочитать их из файла или прочитать из файла функцию:\n"
          "Введите 1 - для ввода точек через консоль\n"
          "Введите 2 - для чтения точек из файла\n"
          "Введите 3 - для чтения функции из файла")
    while True:
        var = input()
        if (not (var == "1" or var == "2" or var == "3")):
            print("Вы должны ввести '1', '2' или '3'")
            continue
        break
    return var


def enter_points():
    while True:
        print("Введите точки в формате:\n"
              "в 1 строке n чисел x\n"
              "во 2 строке n чисел y")
        xs = input().split()
        ys = input().split()
        try:
            xs = list(map(float, xs))
            ys = list(map(float, ys))
        except:
            print("Ввод не соответствует формату")
            continue
        if len(xs) != len(ys):
            print("Количество значений x не соответствует количеству значений y")
            continue
        x_y = []
        for i,z in zip(xs, ys):
            x_y.append((i,z))
        x_y = sorted(x_y, key=lambda x: x[0])
        xs = []
        ys = []
        for i in x_y:
            xs.append(i[0])
            ys.append(i[1])

        if len(xs) < 2:
            print("Точек должно быть 2 или более")
            continue
        print(xs)
        if len(set(xs)) != len(xs):
            print("Точки должны быть разными")
            continue

        break

    while True:
        print("Введите искомую точку(число)")
        try:
            point = float(input())
        except:
            print("Формат ввода неверный")
            continue
        if point < xs[0] or point > xs[1]:
            print("Точка вне диапазона интерполяции, а значит найденное значение может быть некорректным")
        break
    return [xs, ys, point]


def enter_path_to_func_and_get_points():
    print("Введите путь до файла\n"
          "Структура файла должна быть такой:\n"
          "в 1 строке через пробел 2 числа: левый и правый интервал включительно\n"
          "во 2 строке число точек\n"
          "в 3 строке число x - искомая точка"
          "в 4 строке функция")
    while True:
        path = input()
        if not os.path.isfile(path):
            print("Файла по такому пути нет. Повторите ввод:")
            continue

        file = open(path, "r")

        try:
            a, b = map(float, file.readline().split())
        except:
            print("Формат ввода неверен")
            continue

        try:
            n = int(file.readline())
        except:
            print("Формат ввода неверен")

        if n <= 0:
            print("Точек должно быть больше 0")
            continue

        try:
            point = float(file.readline())
        except:
            print("Формат ввода неверный")
            continue
        if point < a or point > b:
            print("Точка вне диапазона интерполяции, а значит найденное значение может быть некорректным")

        ff = file.readline()

        try:
            func = lambda x: eval(ff)
            func(2)
        except Exception as e:
            print("Неверный формат функции")
            print(e)
            continue

        break
    h = (b-a)/(n-1)
    xs = []
    ys = []
    for i in range(n):
        p = i*h + a
        f = func(p)
        xs.append(p)
        ys.append(f)

    xx = np.arange(a,b,(b-a)/1000)
    yy = []
    for i in xx:
        yy.append(func(i))
    # plt.plot(xx, yy)
    # plt.show()

    return [xs, ys, point, xx, yy]


def enter_path_to_points_and_get_points():
    print("Введите путь до файла.\n"
          "Структура файла должна быть такой:\n"
          "в 1 строке n чисел x\n"
          "во 2 строке n чисел y\n"
          "в 3 строке число x - искомая точка")
    while True:
        path = input()
        if not os.path.isfile(path):
            print("Файла по такому пути нет. Повторите ввод:")
            continue

        file = open(path, "r")

        try:
            xs = list(map(float, file.readline().split()))
            ys = list(map(float, file.readline().split()))
        except:
            print("Ввод не соответствует формату")
            continue
        x_y = []
        for i, z in zip(xs, ys):
            x_y.append((i, z))
        x_y = sorted(x_y, key=lambda x: x[0])
        xs = []
        ys = []
        for i in x_y:
            xs.append(i[0])
            ys.append(i[1])

        if len(xs) != len(ys):
            print("Количество значений x не соответствует количеству значений y")
            continue
        if len(xs) < 2:
            print("Точек должно быть 2 или более")
            continue
        if len(set(xs)) != len(xs):
            print("Точки должны быть разными")
            continue

        try:
            point = float(file.readline())
        except:
            print("Формат ввода неверный")
            continue
        if point < xs[0] or point > xs[1]:
            print("Точка вне диапазона интерполяции, а значит найденное значение может быть некорректным")

        break
    return [xs, ys, point]