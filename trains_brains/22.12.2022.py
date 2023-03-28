# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f"{self.__color}"
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def __str__(self):
#         return f"{self.__width},{self.__height},{self.color}"
#     @property
#     def width(self):
#         return self.__width
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#     def area(self):
#         return f"Площадь равна ({self.width*self.height})"
#
# rect = Rectangle(10, 20, "green")
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color ="red"
# rect.width = 5
# print(rect)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'=== Прямоугольник ===\nШирина:{self.width}\nВысота:{self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, bg):
#         super().__init__(width, height)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
# class RectFonBorder(RectFon):
#     def __init__(self,width, height, bg,border):
#         super().__init__(width, height, bg)
#         self.border= border
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
# share = Rect(100, 200)
# share.show_rect()
#
# share1 = RectFon(400, 300, "yellow")
# share1.show_rect()
#
# share2 = RectBorder(150,244,"1px solid red")
# share2.show_rect()
# share3 = RectFonBorder(200, 250,"black", "1px solid red")
# share3.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()
# line.set_coord(Point(100, 240))
# line.draw_line()

#Абстрактные методы

import abc

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print("Координаты должны быть целочисленными")
            return False
        return True


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
    def draw_line(self):
        raise NotImplementedError("В дочернем классе должен быть определён метод draw()")

class Line(Prop):
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
    pass

line = Line(Point(1, 2), Point(10, 20))
line.draw_line()

