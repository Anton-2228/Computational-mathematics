def enter_num_func():
    print("Введите номер функции, которую будем интегрировать:\n"
          "0: x^2+4x+12\n"
          "1: -x^3 + 5.67*x^2 - 7.12*x + 1.34\n"
          "2: x^3 - 2.56*x^2 - 1.325*x + 4.395\n"
          "3: x^4 + 3*x^3 - 12*x^2 - 3*x + 12\n")
    while True:
        ent = input()
        try:
            num = int(ent)
        except:
            print("Введенная строка не является числом\n"
                  "Повторите ввод:")
            continue
        if num != 0 and num != 1 and num != 2 and num != 3 and num != 4:
            print("Введенное число не является 0, 1, 2, 3 или 4\n"
                  "Повторите ввод:")
            continue
        break
    return num

def enter_scope():
    print("Введите 2 числа через пробел: левую и правую границу диапазона, в котором будет интегрироваться функция:")
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
        break
    return [a, b]

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