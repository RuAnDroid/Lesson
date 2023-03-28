# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'Значение {self.name}должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     qty = NonNegative()
#
#     def __init__(self, name, price, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty
#
#     def total(self):
#         return self.price * self.qty
#
#
# a= Order('apple', 5, 10)
# print(a.total())
# a.price = 15
# print(a.total())

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'координата {coord}должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(isinstance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#     def __delete__(self, instance):
#         delattr(instance, self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# del p1.z
# print(p1.__dict__)
# print(p1.y)

# class Point:
#
#    def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1= Point(5,10)
# print(p1.__dict__)
# print(getattr(p1, "x"))
# print(p1.x)
# print(hasattr(p1,"z"))

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'координата {coord}должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(isinstance, self.name)
#
#
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.y)

# import geometry.rect
# import geometry.sq
# import geometry.trian

from geometry import sq, rect, trian

# from geometry import *

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = trian.Triangle(1, 2, 3)
t2 = trian.Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.get_perimetr())


