import os
import random
import sys

from enter_data import *
from funcs import *
from matr import matr

import numpy as np
import matplotlib.pyplot as plt


def chord(num_func, scope, eps):
    table = [["№ шага", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|xk+1 - xk|"]]
    xs = []
    step = 1
    while True:
        table.append([])
        table[-1].append(str(step))
        table[-1].append(str(scope[0]))
        table[-1].append(str(scope[1]))
        x = scope[0] - ((scope[1] - scope[0]) / (funcs[num_func](scope[1]) - funcs[num_func](scope[0]))) * funcs[
            num_func](scope[0])
        xs.append(x)
        table[-1].append(str(x))
        y = funcs[num_func](x)
        if funcs[num_func](scope[0]) * y < 0:
            scope[1] = x
        elif funcs[num_func](scope[1]) * y < 0:
            scope[0] = x
            # scope[0] = scope[1]
            # scope[1] = x
        table[-1].append(str(funcs[num_func](scope[0])))
        table[-1].append(str(funcs[num_func](scope[1])))
        table[-1].append(str(y))
        if len(table) == 2:
            table[-1].append("-")
        else:
            table[-1].append(str(abs(x - xs[-2])))
        if abs(y) <= eps:
            break
        step += 1

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Метод хорд:")
    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))

    print(f"Число итераций: {len(xs)}\n")
    return [table[-1][3], table[-1][6]]


def secant(num_func, scope, eps):
    table = [["№ итерации", "xk-1", "xk", "xk+1", "f(xk+1)", "|xk+1 - xk|"]]
    xs = [scope[0] + (scope[1] - scope[0]) / 3, scope[1] - (scope[1] - scope[0]) / 3]
    step = 1
    while True:
        table.append([])
        table[-1].append(str(step))
        x = xs[-1] - ((xs[-1] - xs[-2]) / (funcs[num_func](xs[-1]) - funcs[num_func](xs[-2]))) * funcs[num_func](xs[-1])
        table[-1].append(str(xs[-2]))
        table[-1].append(str(xs[-1]))
        table[-1].append(str(x))
        xs.append(x)
        y = funcs[num_func](x)
        table[-1].append(str(y))
        if len(table) == 2:
            table[-1].append("-")
        else:
            table[-1].append(str(abs(x - xs[-2])))
        if abs(y) < eps:
            break
        step += 1

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Метод секущих:")
    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))

    print(f"Число итераций: {len(xs) - 2}\n")


def simple_iter(num_func, scope, eps):
    table = [["№ итерации", "xk", "xk+1", "f(xk+1)", "|xk+1 - xk|"]]
    # if deriv_funcs[num_func]((scope[0] + scope[1]) / 2) < 0:
    if deriv_funcs[num_func](scope[0]) < 0:
        lamb = -1 / max(deriv_funcs[num_func](scope[0]), deriv_funcs[num_func](scope[1]))
    else:
        lamb = 1 / max(deriv_funcs[num_func](scope[0]), deriv_funcs[num_func](scope[1]))

    der = abs(deriv_funcs[num_func](scope[0]) * lamb + 1)
    if der >= 2:
        print("Условие сходимости для метода простых итераций не выполняется")
        return
    der = abs(deriv_funcs[num_func](scope[1]) * lamb + 1)
    if der >= 2:
        print("Условие сходимости для метода простых итераций не выполняется")
        return

    xs = []
    if deriv_funcs[num_func](scope[0]) > deriv_funcs[num_func](scope[1]):
        xs.append(scope[0])
    else:
        xs.append(scope[1])
    step = 1
    while True:
        table.append([])
        table[-1].append(str(step))
        x = funcs[num_func](xs[-1]) * lamb + xs[-1]
        table[-1].append(str(xs[-1]))
        table[-1].append(str(x))
        xs.append(x)
        y = funcs[num_func](x)
        table[-1].append(str(y))
        table[-1].append(str(xs[-1] - xs[-2]))
        if abs(y) <= eps:
            break
        step += 1

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Метод простых итераций:")
    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))

    print(f"Число итераций: {len(xs)}\n")


def newton(num_func, start_aprox, eps):
    table = [["№ итерации", "xk-1", "xk", "yk-1", "yk", "|xk - xk-1|", "|yk - yk-1|"]]
    xs = [start_aprox[0]]
    ys = [start_aprox[1]]
    step = 1
    while True:
        table.append([])
        table[-1].append(str(step))
        ma = system_funcs[num_func](xs[-1], ys[-1])
        # apr = matr(ma[0], ma[1], 0.01)
        # left_side = np.array([ma[1][0][:-1], ma[1][1][:-1]])
        # right_side = np.array([ma[1][0][-1], ma[1][1][-1]])
        # apr = np.linalg.inv(left_side).dot(right_side)
        apr = ma.copy()
        x = xs[-1] + apr[0]
        y = ys[-1] + apr[1]
        table[-1].append(str(xs[-1]))
        table[-1].append(str(x))
        table[-1].append(str(ys[-1]))
        table[-1].append(str(y))
        xs.append(x)
        ys.append(y)
        table[-1].append(str(abs(xs[-1] - xs[-2])))
        table[-1].append(str(abs(ys[-1] - ys[-2])))
        if abs(ys[-1] - ys[-2]) <= eps:
            break
        step = + 1

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)
    print("Метод Ньютона для системы:")
    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))

    print(f"Число итераций: {len(xs)}\n")


def data_entry():
    type = enter_type()
    if type == 0:
        num_func = enter_num_func(funcs)
        eps = enter_eps()
        scope = enter_scope(num_func, eps)

        ans = chord(num_func, scope.copy(), eps)
        secant(num_func, scope.copy(), eps)
        simple_iter(num_func, scope.copy(), eps)

        # graph(scope, num_func, eps, ans)

    elif type == 1:
        num_func = enter_num_system_func(system_funcs)
        start_aprox = enter_start_aprox_system()
        eps = enter_eps()

        newton(num_func, start_aprox, eps)

if __name__ == "__main__":
    data_entry()
