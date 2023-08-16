# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('new_2.txt', 'r') as file:
    data = file.read()

words = [len(i.split(' ')) for i in data.split('\n')]
sig = len(data.split('\n'))
print(f'Количество строк {sig}, слов в строке {words}')


print(data.split('\n'))
