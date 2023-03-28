import random

import math


class Cats:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def show_info():
        print(f"{cat1.name} is good boy!!!\n{cat2.name} is good girl!!!")


class Kittens(Cats):
    def __init__(self, gender):
        super().__init__(gender)
        self.name = 'No name'
        self.age = 0

    @staticmethod
    def sex():
        return kats * quantity

    @staticmethod
    def list_num(s):
        math.ceil(len(s))

        for x in range(0, len(s), 3):
            k = s[x: 3 + x]

            if len(k) < 3:
                k = k + [None for _ in range(3 - len(k))]
            yield k

cat1 = Cats('Tom', 2, 'M')
cat2 = Cats('Elsa', 5, 'F')
gen = ['M', 'F']
gender = random.choice(gen)
quantity = random.randint(1, 8)
# print(quantity)
# print(gender)
kats = ('No name', 0, gender)
Cats.show_info()
# x = (kats * quantity)

s = Kittens.sex()

p = list(Kittens.list_num(s))
# for i in p:
#     if p[i] == 'M' or 'F':
#         i = random.choice(gen)

print(p)
