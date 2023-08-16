# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

while True:
    user_text = input('Введите данные, пустую строку для завершения')
    if user_text == '':
        break
    else:
        with open('new_2.txt', 'a', encoding='UTF8') as file:
            file.writelines(user_text)


