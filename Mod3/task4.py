# Чтение строки и вывод 'yes' или 'no' в зависимости от количества 0 и 1
print('yes' if open('input.txt').read().strip().count('1') == open('input.txt').read().strip().count('0') else 'no')
