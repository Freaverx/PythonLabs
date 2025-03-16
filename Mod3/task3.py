# Чтение доменного имени и вывод его частей в обратном порядке
print('\n'.join(reversed(open('input.txt').read().strip().split('.'))))
