# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    data = input()

# Извлечение чисел a, b и c
a = 0
b = 0
c = 0
i = 0

# Преобразуем строку в числа, вручную извлекая a, b и c
while i < len(data) and data[i] != ' ':
    a = a * 10 + int(data[i])
    i += 1

i += 1  # пропускаем пробел

while i < len(data) and data[i] != ' ':
    b = b * 10 + int(data[i])
    i += 1

i += 1  # пропускаем пробел

while i < len(data):
    c = c * 10 + int(data[i])
    i += 1

# Находим число, которое будет стоять между двумя другими
if (a <= b <= c) or (c <= b <= a):
    middle = b
elif (b <= a <= c) or (c <= a <= b):
    middle = a
else:
    middle = c

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(str(middle))
