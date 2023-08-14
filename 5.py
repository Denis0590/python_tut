# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.

raiting = [8, 5, 3,2]
user_input = int(input('Введите число'))
for val in raiting:
    if user_input > val:
        raiting.insert(raiting.index(val), user_input)
        break
    elif user_input < raiting[-1]:
        raiting.append(user_input)
    else:
        pass

print(raiting)