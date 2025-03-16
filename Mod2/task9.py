# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        phone_number = f.read().strip()
except FileNotFoundError:
    phone_number = input().strip()

# Инициализация переменной для результата
cleaned_number = ""

# Проход по строке и фильтрация символов
for char in phone_number:
    if char.isdigit() or char == '+':  # Проверяем, является ли символ цифрой или знаком '+'
        cleaned_number += char  # Добавляем допустимый символ к результату

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(cleaned_number)
