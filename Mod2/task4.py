# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    data = input()

# Проверка на натуральное число
is_natural = True
for char in data:
    if char != '\n' and char != ' ' and (char < '0' or char > '9'):
        is_natural = False
        break

if is_natural:
    number = 0
    for char in data:
        if char != '\n' and char != ' ':
            number = number * 10 + int(char)

    if number == 0:  # Если число ноль, то оно не натуральное
        is_natural = False

if not is_natural:
    result = "Неверный ввод"
else:
    # Преобразование в двоичную, восьмеричную и шестнадцатеричную системы
    binary = ""
    octal = ""
    hexadecimal = ""

    n = number

    # Двоичное представление
    if n == 0:
        binary = "0"
    else:
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2

    n = number

    # Восьмеричное представление
    if n == 0:
        octal = "0"
    else:
        while n > 0:
            octal = str(n % 8) + octal
            n //= 8

    n = number

    # Шестнадцатеричное представление
    if n == 0:
        hexadecimal = "0"
    else:
        while n > 0:
            remainder = n % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
            n //= 16

    result = f"{binary}, {octal}, {hexadecimal}"

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(result)
