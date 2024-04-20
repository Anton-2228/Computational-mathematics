import os

def enter_path():
    print("Введите путь до файла.\n"
          "Структура файла должна быть такой:\n"
          "в 1 строке n значений x\n"
          "во 2 строке n значений y\n"
          "Значений должно быть от 8 до 12")
    while True:
        pa = input()
        if not os.path.isfile(pa):
            print("Файла по такому пути нет. Повторите ввод:")
            continue
        break
    return pa