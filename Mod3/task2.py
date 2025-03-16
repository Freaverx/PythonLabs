# Чтение входных данных и вывод представлений числа
print((lambda n: f"{bin(n)[2:]}, {oct(n)[2:]}, {hex(n)[2:]}" if n > 0 else "Неверный ввод")(int(open('input.txt').read().strip())))
