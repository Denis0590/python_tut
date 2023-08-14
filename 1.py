 # Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
 # пользователя, предусмотреть обработку ситуации деления на ноль.

def division(val_1, val_2):
   try:
       return val_1/val_2
   except ZeroDivisionError:
       return 'Деление на 0'

result = division(int(input('')), int(input('')))
print(result)