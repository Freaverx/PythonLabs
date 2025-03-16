# Чтение строки, составление нового слова из последних букв и вывод результата
print(''.join(word[-1] for word in open('input.txt').read().strip().split()))
