n = int(input('Введите количество элементов: '))

numbers = []

for i in range(1, n+1):
    num = int(input(f'Введите {i} элемент: '))
    numbers.append(num)

unique_numbers = sorted(set(numbers))

print('Вывод:', unique_numbers)