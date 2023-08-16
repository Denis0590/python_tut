# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
# из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import re

with open('new_3.txt', 'r', encoding='UTF8') as file:
    data = file.read()

print(data.split('\n'))

employers = [name.split(' ')[0] for name in data.split('\n')]
value = [int(re.findall(r'\d+', words)[0]) for words in  data.split('\n')]
employe_dict = dict(zip(employers, value))
small_salary = [name for name in employe_dict.keys() if employe_dict[name] <2000]
print(f'Сотрудники с низким окладом {small_salary}, средний окладн {sum(employe_dict.values()) / len(employe_dict.values())}')