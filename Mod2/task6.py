# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read().strip()
except FileNotFoundError:
    data = input().strip()

# Проверка на пустую строку
if data == "":
    result = "no"
else:
    count_0 = 0
    count_1 = 0

    # Подсчет нулей и единиц
    for char in data:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1

    # Сравнение количества нулей и единиц
    if count_0 == count_1:
        result = "yes"
    else:
        result = "no"

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(result)
