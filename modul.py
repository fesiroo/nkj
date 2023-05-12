# import random as r
# s = [1, 2, 3, 4, 5]
# # print(r.choice(s))
# r.shuffle(s)
# print(s)
# a = r.randrange(1, 40)
# print(a)

import random as r
startr = int(input("Введите начало диапозона "))
endr = int(input("Введите конец диапозона "))
a = r.randrange(startr, endr)
print("Ваше случайное число =", a)
