import math
from abc import abstractclassmethod

class Shape:
    def __init__(self, color):
        self.color = color
    @abstractclassmethod
    def show_info(self):
        pass

    @abstractclassmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        super().__init__(color)
        self.a = a

    def show_info(self):
        print(f"===Квадрат===\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {self.a ** 2}\nПериметр:{self.a * 4}")

    def print_info(self):
        for i in range(self.a):
            if i in (0, self.a - 1):
                print('*' * self.a)
            else:
                print('*', end='')
                for j in range(1, self.a - 1):
                    print('*' if j in (i, self.a - i - 1) else ' ', end='')
                print('*')


class Rectangle(Shape):
    def __init__(self, x, y, color):
        super().__init__(color)
        self.x = x
        self.y = y

    def show_info(self):
        print(
            f"===Прямоугольник===\nДлинна: {self.x}\nШирина: {self.y}\nЦвет: {self.color}\nПлощадь: {self.x * self.y}\nПериметр:{(self.x + self.y) * 2}")

    def print_info(self):
        for x in range(self.x):
            for y in range(self.y):
                print("*", end='')
            print()


class Triangle(Shape):

    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def show_info(self):
        print(
            f"===Треугольник===\nСторона1: {self.a}\nСторона2: {self.b}\nСторона3: {self.b}\nЦвет: {self.color}\nПлощадь: {round(math.sqrt((self.a + self.b + self.c) / 2 * ((self.a + self.b + self.c) / 2 - self.a) * ((self.a + self.b + self.c) / 2 - self.b) * ((self.a + self.b + self.c) / 2 - self.c)), 2)} \nПериметр: {(self.a + self.b + self.c) / 2}")

    def print_info(self):
        for j in range(1, self.b + 1):
            for i in range(self.b * 2 + 1):
                if i == self.b:
                    print('*' * (j * 2 - 1), end="")
                    self.b -= 1
                else:
                    print(' ', end="")
            print()


a = Square(3, 'red')
b = Rectangle(3, 7, 'green')
c = Triangle(11, 6, 6, 'yellow')
a.show_info()
a.print_info()
print()
b.show_info()
b.print_info()
print()
c.show_info()
c.print_info()
print()
