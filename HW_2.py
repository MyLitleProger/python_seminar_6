# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
start = -10
end = 10

num_list = [randint(start, end) for _ in range(20)]
first, second = None, None
# проверка на ввод, что бы в диапазоне не было логических ошибок
# и вылета при вводе некорректных данных
while True:
    if first is None or first >= end:
        try:
            first = int(input(f'Введите начальное значение в диапазоне от {start} до {end-1}: '))
        except ValueError:
            continue
        if first >= end:
            continue
    if second is None or second <= first or second > end:
        try:
            second = int(input(f'Введите конечное значение от {first} до {end}: '))
        except ValueError:
            continue
        if first < second <= end:
            break

print(f'Начальный список: {num_list}')
print(f'Интервал: от {first} до {second}')
result_list = []
# решение
for index, value in enumerate(num_list):
    if first <= value <= second:
        result_list.append(index)
print(f'Номера элементов подходящих под интервал: {result_list}')
