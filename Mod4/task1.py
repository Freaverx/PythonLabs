def checknumbers(numbers):
    if all(x == numbers[0] for x in numbers):
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

# Чтение списка чисел из ввода
numbers = input().strip().split()
print(checknumbers(numbers))
