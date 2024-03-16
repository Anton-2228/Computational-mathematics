from funcs import *

def enter_type():
    print("Вы хотите найти решений нелинейного уравнения, или системы нелинейных уравнений?\n"
          "Для нелинейного уравнения введите - 0\n"
          "Для системы нелинейных уравнений введите - 1")
    while True:
        ent = input()
        try:
            type = int(ent)
        except:
            print("Введенная строка не является числом\n"
                  "Повторите ввод:")
            continue
        if type != 0 and type != 1:
            print("Введенное числе не является 0 или 1\n"
                  "Повторите ввод:")
            continue
        break
    return type

def enter_eps():
    print("Введите допустимую погрешность:")
    while True:
        ent = input()
        try:
            eps = float(ent)
        except:
            print("Введенная строка не является числом\n"
                  "Повторите ввод:")
            continue
        if eps <= 0:
            print("Допустимая погрешность должна быть больше 0\n"
                  "Повторите ввод:")
            continue
        break
    return eps

def enter_num_func(funcs):
    print("Введите номер функции, которую будем считать:\n"
          "0: 3*x^3 + 1.7*x^2 - 15.42*x + 6.89\n"
          "1: -x^3 + 5.67*x^2 - 7.12*x + 1.34\n"
          "2: x^3 - 2.56*x^2 - 1.325*x + 4.395")
    while True:
        ent = input()
        try:
            num = int(ent)
        except:
            print("Введенная строка не является числом\n"
                  "Повторите ввод:")
            continue
        if num != 0 and num != 1 and num != 2:
            print("Введенное число не является 0, 1 или 2\n"
                  "Повторите ввод:")
            continue
        break
    return num

def enter_num_system_func(system_funcs):
    print("Введите номер функции, которую будем считать:\n"
          "0: sin(x+y) - 1.2x = 0.2\n"
          "   x^2 + 2y^2 = 1")
    while True:
        ent = input()
        try:
            num = int(ent)
        except:
            print("Введенная строка не является числом\n"
                  "Повторите ввод:")
            continue
        if num != 0 and num != 1 and num != 2:
            print("Введенное число не является 0, 1\n"
                  "Повторите ввод:")
            continue
        break
    return num

def enter_scope(num_func, eps):
    print("Введите 2 числа через пробел: левую и правую границу диапазона, в котором будут искаться корни:")
    while True:
        ent = input().split()
        if len(ent) != 2:
            print("Было введено не 2 числа\n"
                  "Повторите ввод:")
            continue
        try:
            a = float(ent[0])
            b = float(ent[1])
        except:
            print("Одно из введенных чисел не является числом\n"
                  "Повторите ввод:")
            continue
        if a >= b:
            print("Левая граница должна быть меньше правой\n"
                  "Повторите ввод:")
            continue
        if funcs[num_func](a) * funcs[num_func](b) >= 0:
            print("В указанном диапазоне корней либо нет, либо больше 1\n"
                  "Повторите ввод:")
            continue

        break
    return [a, b]

def enter_start_aprox_system():
    print("Введите через пробел стартовое приближение(x y):")
    while True:
        ent = input().split()
        if len(ent) != 2:
            print("Было введено не 2 числа\n"
                  "Повторите ввод:")
            continue
        try:
            x = float(ent[0])
            y = float(ent[1])
        except:
            print("Одно из введенных чисел не является числом\n"
                  "Повторите ввод:")
            continue

        break
    return [x,y]