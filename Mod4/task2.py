def fastpower(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        halfpower = fastpower(a, n // 2)
        return halfpower * halfpower
    else:
        return a * fast_power(a, n - 1)

# Чтение входных данных
a, n = map(float, input().strip().split())
print(fastpower(a, int(n)))
