# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list)
list2 = []
i = 0
Rand = random.randint(0, (len(list)-1))
while i != 8:
    x = random.choice(list)
    doubles = False
    for k in list2:
        if (x == k):
            doubles = True
    if (doubles is False):
        list2.append(x)
        i += 1
print(list2)

# ну или random.shuffle(list)
