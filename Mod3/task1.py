# Чтение входных данных, упорядочивание и вывод среднего числа
with open('input.txt', 'r') as f: a, b, c = map(int, f.read().strip().split()); print(sorted([a, b, c])[1]) if a and b and c else print('0')
