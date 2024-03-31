from funcs import *
from enter_data import *

def rect_method(data):
    num = data[0]
    a = data[1][0]
    b = data[1][1]
    eps = data[2]
    n = 4
    ans_l = []
    ans_r = []
    ans_av = []
    for i in range(20000):
        l = (b - a) / n
        su_l = 0
        su_r = 0
        su_av = 0
        a_l = a
        b_l = b
        while b_l - a_l > 0:
            f = funcs[num](a_l)*l
            su_l += f
            f = funcs[num](a_l+l)*l
            su_r += f
            f = funcs[num](a_l+l/2)*l
            su_av += f
            a_l += l
        ans_l.append(su_l)
        ans_r.append(su_r)
        ans_av.append(su_av)
        if len(ans_r) >= 8 and len(ans_r)%2==0:
            if (ans_r[len(ans_r)//2] - ans_r[-1]) / 3 < eps:
                if (ans_l[len(ans_l) // 2] - ans_l[-1]) / 3 < eps:
                    if (ans_av[len(ans_av) // 2] - ans_av[-1]) / 3 < eps:
                        break
        n += 1
    if i == 19999:
        print("Найти интеграл методами прямоугольника с заданной точносью не вышло:(")
        return
    print(f"Значение интеграла, вычисленное с помощью метода левых прямоугольников при n равном {len(ans_l)//2+4}: {ans_l[len(ans_l) // 2]}")
    print(f"Значение интеграла, вычисленное с помощью метода срединных прямоугольников при n равном {len(ans_av)//2+4}: {ans_av[len(ans_av) // 2]}")
    print(f"Значение интеграла, вычисленное с помощью метода правых прямоугольников при n равном {len(ans_r)//2+4}: {ans_r[len(ans_r) // 2]}")
def trapez_method(data):
    num = data[0]
    a = data[1][0]
    b = data[1][1]
    eps = data[2]
    n = 4
    ans = []
    for i in range(20000):
        l = (b - a) / n
        su = 0
        a_l = a
        b_l = b
        while b_l - a_l > 0:
            f1 = funcs[num](a_l) * l
            if a_l + l <= b_l:
                f2 = funcs[num](a_l+l) * l
            else:
                f2 = funcs[num](b_l) * l
            su += (f1+f2)/2
            a_l += l
        ans.append(su)
        if len(ans) >= 8 and len(ans) % 2 == 0:
            if (ans[len(ans) // 2] - ans[-1]) / 3 < eps:
                break
        n += 1
    if i == 19999:
        print("Найти интеграл методом трапеции с заданной точносью не вышло:(")
        return
    print(f"Значение интеграла, вычисленное с помощью метода трапеций при n равном {len(ans)//2+4}: {ans[len(ans) // 2]}")

def simpson_method(data):
    num = data[0]
    a = data[1][0]
    b = data[1][1]
    eps = data[2]
    n = 4
    ans = []
    for i in range(20000):
        l = (b - a) / n
        su = 0
        a_l = a
        b_l = b
        while b_l - a_l > 0:
            f1 = funcs[num](a_l)
            if a_l + l <= b_l and a_l + 2*l <= b_l:
                f2 = funcs[num](a_l + l)
                f3 = funcs[num](a_l + 2*l)
            else:
                f2 = funcs[num]((b_l + a_l) / 2)
                f3 = funcs[num](b_l)
            su += (l/3)*(f1 + 4*f2 + f3)
            a_l += 2*l
        ans.append(su)
        if len(ans) >= 8 and len(ans) % 2 == 0:
            if (ans[len(ans) // 2] - ans[-1]) / 15 < eps:
                break
        n += 1
    print(ans)
    if i == 19999:
        print("Найти интеграл методом Симпсона с заданной точносью не вышло:(")
        return
    print(f"Значение интеграла, вычисленное с помощью метода Симпсона при n равном {len(ans)//2+4}: {ans[len(ans) // 2]}")

def data_entry():
    num = enter_num_func()
    scope = enter_scope()
    eps = enter_eps()
    return [num, scope, eps]

def main():
    data = data_entry()
    rect_method(data)
    trapez_method(data)
    simpson_method(data)

if __name__ == "__main__":
    main()