# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

import random
N = int(input())
rangeNumbers = []
for i in range(N):
    Number = random.randint(-N, N)
    rangeNumbers.append(Number)
with open('file.txt', 'r') as f:
    nums = f.read().splitlines()
pos1 = int(nums[0])
pos2 = int(nums[1])
print(rangeNumbers)
print(rangeNumbers[pos1]*rangeNumbers[pos2])
