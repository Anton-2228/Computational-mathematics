from math import tan, sin, cos

def func1(x):
    return x**3-0.5*x**2+0.6
    #return 3*x**3 + 1.7*x**2 - 15.42*x + 6.89

def func2(x):
    return -x**3 + 5.67*x**2 - 7.12*x + 1.34

def func3(x):
    return x**3 - 2.56*x**2 - 1.325*x + 4.395

def deriv_func1(x):
    return 9*x**2 + (17/5)*x - 771/50

def deriv_func2(x):
    return -3*x**2 + (567/50)*x - 178/25

def deriv_func3(x):
    return 3*x**2 - (128/25)*x - 53/40

def deriv_deriv_func1(x):
    return 18*x + 17/5

def deriv_deriv_func2(x):
    return -6*x + 567/50

def deriv_deriv_func3(x):
    return 6*x - 128/25

def system_func1(x, y):
    #nums = []
    #nums.append([])
    #nums[-1].append(cos(x+y) - 6/5)
    #nums[-1].append(cos(x+y))
    ##nums[-1].append(sin(x+y) - 1.2*x - 0.2)
    #nums[-1].append(-sin(x+y) + 1.2*x + 0.2)

    #nums.append([])
    #nums[-1].append(2*x)
    #nums[-1].append(4*y)
    ##nums[-1].append(x**2 + 2*y**2 - 1)
    #nums[-1].append(-x**2 - 2*y**2 + 1)

    #return [2, nums]

    if x == 0:
        x += 1
    if y == 0:
        y += 1

    dy = (-sin(x+y)*2*x + 2.4*x**2 + 0.4*x + cos(x+y)*x**2 + cos(x+y)*2*y**2 - cos(x+y) - (6/5)*x**2 - (12/5)*y**2 + 6/5)   /   ((24/5)*y - cos(x+y)*4*y + 2*x*cos(x+y))
    dx = (-x**2 - 2*y**2 + 1 - dy*4*y) / (2*x)
    return [dx, dy]

def system_func2(x, y):
    # nums = []
    # nums.append([])
    # nums[-1].append(2*x)
    # nums[-1].append(2*y)
    # nums[-1].append(-x**2 - y**2 + 4)
    #
    # nums.append([])
    # nums[-1].append(-6*x)
    # nums[-1].append(1)
    # nums[-1].append(3*x**2 - y)
    #
    # return [2, nums]
    if x == 0:
        x += 1
    if y == 0:
        y += 1


    dy = (6*x**3 - 2*x*y + 24*x - 6*x**3 - 6*x*y**2)   /   (12*x*y + 2*x)
    dx = (4 - x**2 - y**2 - 2*y*dy) / (2*x)
    return [dx, dy]

funcs = [func1, func2, func3]
deriv_funcs = [deriv_func1, deriv_func2, deriv_func3]
deriv_deriv_funcs = [deriv_deriv_func1, deriv_deriv_func2, deriv_deriv_func3]

system_funcs = [system_func1, system_func2]