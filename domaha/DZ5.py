import math


class Table:
    def __init__(self, weight,length,radius):
        self._weight = weight
        self._length = length
        self._radius = radius

class Rectangle(Table):
    def __init__(self, weight, length):
        self._weight = weight
        self._length = length

    def rectangle_info(self):
        return self._weight * self._length


class Round(Table):
    def __init__(self, radius):
        self._radius = radius

    def round_info(self):
        return round(math.pi * (self._radius ** 2), 2)

p = Rectangle(20, 10)
print(p.__dict__)
print(p.rectangle_info())
d = Rectangle(20, 20)
print(d.__dict__)
print(p.rectangle_info())
h = Round(20)
print(h.__dict__)
print(h.round_info())
