# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read().strip()
except FileNotFoundError:
    data = input().strip()

# Инициализация переменной для результата
result = ""

# Индекс начала слова
start_index = 0

# Проход по строке для извлечения последних букв
for index in range(len(data)):
    # Если встречаем пробел или конец строки, берем последнюю букву
    if data[index] == ' ' or index == len(data) - 1:
        if index == len(data) - 1:  # Если это последний символ
            result += data[index]  # Добавляем последний символ
        else:
            result += data[index - 1]  # Добавляем букву перед пробелом
        start_index = index + 1  # Обновляем индекс начала слова

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(result)
