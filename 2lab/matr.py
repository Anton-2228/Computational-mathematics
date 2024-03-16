import sys
def matr(dim, nums, eps):
    #print(nums)
    ret = diag_matr(dim, nums)
    nums = ret[0]
    d = ret[1]
    res = ret[2]

    res_lin = check_lin(dim, nums)

    if res_lin:
        print("Матрица линейно зависима, а значит существует бесконечное число решений, следовательно данный метод не применим.")
        sys.exit()

    if not res:
        print("Для данной матрицы условие преобладания диагональных элементов не выполняется, а значит сходимость не гарантированна. Будет проведено 100 итераций. Если в результате не будет достигнута заданная точность, значит найти решение таким методом невозможно.")

    coef = []
    for i in range(dim):
        coef.append([])
        for z in range(dim):
            if i != z:
                coef[i].append(-nums[i][z] / nums[i][i])
            else:
                coef[i].append(0)
        d[i] /= nums[i][i]

    apr = d.copy()
    for k in range(100):
        next_apr = []
        for i in range(dim):
            next_apr.append(sum((
                coef[i][x]*apr[x] for x in range(dim)
            )) + d[i])
        dif_apr = [abs(next_apr[x]-apr[x]) for x in range(dim)]
        rr = False
        if max(dif_apr) < eps:
            rr = True
            #break
        apr = next_apr.copy()
        if rr:
            break
    return apr

def check_lin(dim, nums):
    res = False
    for i in range(len(nums)):
        loc_res = True
        for z in range(i+1, len(nums)):
            k = ""
            for l in range(len(nums[i])):
                try:
                    if k == "":
                        k = nums[i][l]/nums[z][l]
                    else:
                        if nums[i][l]/nums[z][l] != k:
                            loc_res = False
                            break
                except:
                    if k == "":
                        k = " "
                    elif k != " ":
                        loc_res = False
                        break
                    continue
            if loc_res:
                res = True
                break
        if loc_res:
            break
    return res

def diag_matr(dim, nums):
    d = []
    diag_d = []
    for i in range(dim):
        d.append(nums[i].pop(-1))
        diag_d.append(0)

    sort_nums = []
    diag_nums = []
    for i in range(dim):
        diag_nums.append([])
        sort_nums.append([])
        for z in range(dim):
            sort_nums[i].append((nums[i][z], z))
        sort_nums[i].sort(key=lambda x: x[0], reverse=True)

    for i in range(dim):
        for z in sort_nums[i]:
            if diag_nums[z[1]] == []:
                diag_nums[z[1]] = nums[i]
                diag_d[z[1]] = d[i]
                break
            else:
                continue
    for i in range(dim):
        s = 0
        for z in range(dim):
            if i != z:
                s += abs(diag_nums[i][z])
        if abs(diag_nums[i][i]) < s:
            return [diag_nums, diag_d, False]
    return [diag_nums, diag_d, True]