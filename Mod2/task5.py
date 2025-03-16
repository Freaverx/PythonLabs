# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read().strip()
except FileNotFoundError:
    data = input().strip()

# Проверка на наличие доменного имени
if data == "":
    result = ""
else:
    # Разделение доменного имени на части
    domain_parts = []
    current_part = ""

    for char in data:
        if char == '.':
            if current_part:  # Если есть текущая часть
                domain_parts.append(current_part)
                current_part = ""
        else:
            current_part += char

    # Добавляем последнюю часть, если она не пустая
    if current_part:
        domain_parts.append(current_part)

    # Переворачиваем список, чтобы начать с домена первого уровня
    result = ""
    for i in range(len(domain_parts) - 1, -1, -1):
        result += domain_parts[i] + "\n"

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(result.strip())  # Удаляем последний перевод строки
