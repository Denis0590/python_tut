# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_fuck(val_1, val_2, val_3):
    return sum(sorted([val_1, val_2, val_3], reverse=True)[:-1])


if __name__=='__main__':
    print(my_fuck(10, 2, 5))

