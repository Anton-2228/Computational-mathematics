from enter_data import *
import sys
sys.setrecursionlimit(100000)

def lagranz(xs, ys, point):

    l = []
    for i in range(len(xs)):
        numerator = 1
        denumerator = 1
        for z in range(len(xs)):
            if (i != z):
                numerator *= (point - xs[z])
                denumerator *= xs[i] - xs[z]
        l_cur = (numerator/denumerator) * ys[i]
        l.append(l_cur)
    l_fin = sum(l)
    print(f"Метод Лагранжа: значение в точке {point} равно {l_fin}")

def newton_razn_mnog(xs, ys):
    if len(xs) == 1:
        return ys[0]
    else:
        return (newton_razn_mnog(xs[1:], ys[1:]) - newton_razn_mnog(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

def newton_razn(xs, ys, point):
    ans = ys[0]
    multiplier = 1
    for i in range(2, len(xs)+1):
        multiplier *= point - xs[i-2]
        newt_cur = newton_razn_mnog(xs[:i], ys[:i]) * multiplier
        ans += newt_cur
    print(f"Метод Ньютона с разделенными разностями: значение в точке {point} равно {ans}")

def newton_ravn_mnog(ys):
    if len(ys) == 1:
        return ys[0]
    else:
        return newton_ravn_mnog(ys[1:]) - newton_ravn_mnog(ys[:-1])

def newton_ravn(xs, ys, point):

    delt_ys = [[]]
    for i in range(len(ys)):
        delt_ys[-1].append(ys[i])
    for i in range(1, len(ys)):
        delt_ys.append([])
        for z in range(len(ys[:-i])):
            delt_ys[-1].append(delt_ys[-2][z+1] - delt_ys[-2][z])

    table = [["xi"], ["yi"]]
    for i in range(1, len(ys)):
        table.append([f"x{i}"])
    for i in range(len(xs)):
        table[0].append(f"Δ{i}yi")
        for z in range(1, len(ys)+1):
            if z <= len(xs)-i:
                table[z].append(str(delt_ys[i][z-1]))
            else:
                table[z].append("-")


    t = (point - xs[0])/(xs[1] - xs[0])
    multiplier = t
    devider = 1
    count = 1
    ans = (ys[0] + multiplier*newton_ravn_mnog(ys[:2])) / devider
    for i in range(len(xs)-2):
        t -= 1
        count += 1
        devider *= count
        multiplier *= t
        newt_cur = delt_ys[i+2][0]
        newt_cur *= multiplier
        newt_cur /= devider
        ans += newt_cur
    print(f"Метод Ньютона с равноотстоящими разностями: значение в точке {point} равно {ans}")
    print("\n")

    col_width = []
    for i in range(len(table[0])):
        ma = 0
        for z in table:
            if len(str(z[i])) > ma:
                ma = len(str(z[i]))
        col_width.append(ma + 4)
    col_width.append(0)

    for i in table:
        print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))
    print("\n")



def main():
    var = enter_var()
    if var == "1":
        xs, ys, point = enter_points()
    elif var == "2":
        xs, ys, point = enter_path_to_points_and_get_points()
    elif var == "3":
        xs, ys, point, xx, yy = enter_path_to_func_and_get_points()

    # print(xs)
    # print(ys)
    # print(point)

    lagranz(xs, ys, point)
    newton_razn(xs, ys, point)
    newton_ravn(xs, ys, point)

    plt.plot(xx, yy)
    plt.show()

if __name__ == "__main__":
    main()