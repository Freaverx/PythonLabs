# Чтение входных данных
try:
    with open('input.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    data = input()

# Преобразование строки в число
sidelength = 0
for char in data:
    if char != '\n' and char != ' ':
        sidelength = sidelength * 10 + int(char)

# Расчет периметра, площади и диагонали
perimeter = 4 * side_length
area = sidelength * side_length
diagonal = (sidelength ** 2 + sidelength ** 2) ** 0.5  # Пифагорова теорема

# Форматирование результатов с округлением до 2 знаков
perimeter_str = f"{perimeter:.2f}"
area_str = f"{area:.2f}"
diagonal_str = f"{diagonal:.2f}"

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(f"{perimeter_str}, {area_str}, {diagonal_str}")
