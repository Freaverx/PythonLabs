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
    domainparts = []
    currentpart = ""

    for char in data:
        if char == '.':
            if currentpart:  # Если есть текущая часть
                domainparts.append(currentpart)
                currentpart = ""
        else:
            currentpart += char

    # Добавляем последнюю часть, если она не пустая
    if currentpart:
        domainparts.append(currentpart)

    # Переворачиваем список, чтобы начать с домена первого уровня
    result = ""
    for i in range(len(domainparts) - 1, -1, -1):
        result += domainparts[i] + "\n"

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(result.strip())  # Удаляем последний перевод строки
