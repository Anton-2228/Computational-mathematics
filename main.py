#def main(dim, map):


def data_entry():
    print("Хотите осуществить ввод с клавиатуры или из файла?\n"
          "Введите 1 если с клавиатуры и 2 если из файла:")
    a = int(input())
    nums = []
    if a == 1:
        print("Вводите размерность матрицы:")
        n = int(input())
        print("Вводите коэффициенты построчно через пробел. Свободный член вводите самым правым элементом:")
        for i in range(n):
            while True:
                line = list(input().split())
                if len(line) != n + 1:
                    print(
                        f"Число введенных чисел равно {len(line)}. В строке должно быть {n} коэффициентов и 1 свободный член.  Повторите ввод этой строки:")
                    continue
                err = []
                for i in line:
                    try:
                        int(i)
                    except:
                        err.append(i)
                if len(err) != 0:
                    print(f"{', '.join(err)} не являются числами. Повторите ввод этой строки:")
                    continue
                break
            nums.append(list(map(int, line)))
    print(n)
    print(nums)

    #main(n, nums)


if __name__ == "__main__":
    data_entry()