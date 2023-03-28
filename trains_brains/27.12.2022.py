# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Родитель")
#
#
# class Queen(Chess):
#     def move(self):
#         super.move()
#         print("Переместил шахматную фигуру")
#
# q = Queen()
# q.draw()
# q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
#
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")
# c = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 50)
# for elem in c:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")
# print('*' * 50)

# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
#
# class Child(Father):
#     def display1(self):
#         print("Дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
# qc = GrandChild()
# qc.display2()
# qc.display1()
#
# class MyOuter:
#     age = 18
#
#
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def outer_class_method():
#         print("Я метод этого класса")
#     def outer_obj_method(self):
#         print("Связующий метод")
#
#     class MyInner:
#         def __init__(self, inner_name,obj):
#             self.inner_name = inner_name
#             self.obj = obj
#         def inner_method(self):
#             print("Метод вложенного классса", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
# out=MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# print(inner.inner_name)
# inner.inner_method()

class Color:
    def __init__(self):
        self.name = "Green"
        self.lg = self.LightGreen()
    def show(self):
        print("Name:",self.name)
    class LightGreen:
        def __init__(self):
            self.name = "Light Green"
            self.code = "0204asd"

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)

outer = Color()
outer.show()

g=outer.lg
g.display()
