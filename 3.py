# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

user_input = int(input('Введите месяц'))
period_list  = []
for n in range(2):
    period_list.append('Зима')
for n in range(3):
    period_list.append('Весна')
for n in range(3):
    period_list.append('Лето')
for n in range(3):
    period_list.append('Осень')
period_list.append('Зима')



try:
    print(period_list[user_input-1])
except IndexError:
    print('месяц вне диапазона')





