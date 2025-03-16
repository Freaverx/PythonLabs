def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Чтение входных данных
a, b = map(int, input("Введите два числа через пробел: ").strip().split())
print(f"Наибольший общий делитель: {gcd(a, b)}")
