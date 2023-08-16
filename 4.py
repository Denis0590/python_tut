# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


replace_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('new_4.txt', 'r', encoding='UTF8') as file:
    for line in file.readlines():
        for key, item in replace_dict.items():
            if key in line:
                new_line =  line.replace(key, item)
                with open('extra_4.txt', 'a', encoding='UTF8') as new_file:
                    new_file.write(new_line)
            else:
                pass
        #
