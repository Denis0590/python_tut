# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.



values  = '1 2 35 56 67 3 0'
with open('new_5.txt', 'w') as file:
    file.write(values)

with open('new_5.txt') as file:
    print(sum([int(val) for val in file.read().split(' ')]))
