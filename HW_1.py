# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

start_element = []
# проверка на ввод
while True:
    try:
        if not start_element:
            start_element.append(int(input('Введите начальный элемент арифметической прогрессии: ')))
        if len(start_element) < 2:
            start_element.append(int(input('Введите шаг арифметической прогрессии: ')))
        if len(start_element) < 3:
            start_element.append(int(input('Введите количество элементов арифметической прогрессии: ')))
        break
    except ValueError:
        pass
# решение
arithmetic_progression = []
for quantity in range(start_element[2] - 1, -1, -1):
    if quantity == 0:
        arithmetic_progression.append(start_element[0])
        break
    arithmetic_progression.append(start_element[0] + quantity * start_element[1])

arithmetic_progression.sort()
print(arithmetic_progression)
