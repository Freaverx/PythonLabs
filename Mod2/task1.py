# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    data = input()

# Извлечение чисел A и B
A = 0
B = 0
i = 0
# Преобразуем строку в числа, вручную извлекая A и B
while i < len(data) and data[i] != ' ':
    A = A * 10 + int(data[i])  # построение числа A
    i += 1

i += 1  # пропускаем пробел

while i < len(data):
    B = B * 10 + int(data[i])  # построение числа B
    i += 1

# Нахождение остатка от деления A на B
remainder = A % B

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(str(remainder))
