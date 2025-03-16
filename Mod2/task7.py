# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read().strip()
except FileNotFoundError:
    data = input().strip()

# Разделение строки и символа
separator_index = data.find(',')
if separator_index == -1:
    result = 0  # Если запятая не найдена, возвращаем 0
else:
    s = data[:separator_index]  # Строка
    i = data[separator_index + 1:]  # Символ

    # Проверка, что символ i состоит из одного символа
    if len(i) != 1:
        result = 0
    else:
        count = 0
        # Подсчет символов i в начале строки
        for char in s:
            if char == i:
                count += 1
            else:
                break  # Прерываем, если встречаем другой символ
        result = count

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(str(result))
