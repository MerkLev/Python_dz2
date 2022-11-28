# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

N = int(input('Введите число N: '))
rangeNumbers = []
for i in range(1, N+1):
    Number = (1+1/i)**i
    rangeNumbers.append(Number)
print(f'Последовательность =  {rangeNumbers}')
print(f' Сумма = {sum(rangeNumbers)}')

