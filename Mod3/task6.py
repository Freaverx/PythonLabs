# Чтение последовательности чисел и вывод True, если есть дубликаты, иначе False
print(len(set(open('input.txt').read().strip().split())) < len(open('input.txt').read().strip().split()))
