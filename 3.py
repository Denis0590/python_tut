# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

def new_division_1(x, y):
    return x ** y

def new_division_2(x, y):
    new_x = x
    while True:
        if y ==-1:
            break
        else:
            new_x*=x
            y+=1
    return 1/new_x



result_1 = new_division_1(2, -5)
result_2 = new_division_2(2, -5)
print(result_2, result_1)