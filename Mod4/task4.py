def can_form_palindrome(s):
    # Словарь для хранения количества каждого символа
    char_count = {}

    # Подсчет количества каждого символа
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Проверка количества символов с нечетным количеством
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Для палиндрома допускается не более одного символа с нечетным количеством
    return odd_count <= 1


def construct_palindrome(s):
    if not can_form_palindrome(s):
        return None

    # Словарь для хранения количества каждого символа
    char_count = {}

    # Подсчет количества каждого символа
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    half_palindrome = []
    middle_char = ""

    # Формирование половины палиндрома и определение среднего символа
    for char, count in char_count.items():
        half_palindrome.append(char * (count // 2))
        if count % 2 != 0:
            middle_char = char

    # Собираем палиндром
    half_palindrome_str = ''.join(half_palindrome)
    palindrome = half_palindrome_str + middle_char + half_palindrome_str[::-1]

    return palindrome


# Чтение входных данных
input_string = input("Введите строку: ").strip()
palindrome = construct_palindrome(input_string)

if palindrome:
    print(f"Составленный палиндром: {palindrome}")
else:
    print("Из данной строки нельзя составить палиндром.")
