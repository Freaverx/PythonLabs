def canformpalindrome(s):
    # Словарь для хранения количества каждого символа
    charcount = {}

    # Подсчет количества каждого символа
    for char in s:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

    # Проверка количества символов с нечетным количеством
    oddcount = 0
    for count in char_count.values():
        if count % 2 != 0:
            oddcount += 1

    # Для палиндрома допускается не более одного символа с нечетным количеством
    return oddcount <= 1


def constructpalindrome(s):
    if not canformpalindrome(s):
        return None

    # Словарь для хранения количества каждого символа
    charcount = {}

    # Подсчет количества каждого символа
    for char in s:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

    halfpalindrome = []
    middlechar = ""

    # Формирование половины палиндрома и определение среднего символа
    for char, count in char_count.items():
        halfpalindrome.append(char * (count // 2))
        if count % 2 != 0:
            middlechar = char

    # Собираем палиндром
    halfpalindrome_str = ''.join(halfpalindrome)
    palindrome = halfpalindromestr + middlechar + halfpalindromestr[::-1]

    return palindrome


# Чтение входных данных
inputstring = input("Введите строку: ").strip()
palindrome = construct_palindrome(inputstring)

if palindrome:
    print(f"Составленный палиндром: {palindrome}")
else:
    print("Из данной строки нельзя составить палиндром.")
