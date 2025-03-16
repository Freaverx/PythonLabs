# Чтение номера телефона и вывод его без лишних символов
print(''.join(c for c in open('input.txt').read().strip() if c.isdigit() or c == '+'))
