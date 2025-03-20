# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        phonenumber = f.read().strip()
except FileNotFoundError:
    phonenumber = input().strip()

# Инициализация переменной для результата
cleanednumber = ""

# Проход по строке и фильтрация символов
for char in phonenumber:
    if char.isdigit() or char == '+':  # Проверяем, является ли символ цифрой или знаком '+'
        cleanednumber += char  # Добавляем допустимый символ к результату

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(cleanednumber)
