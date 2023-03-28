# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Sqiare:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Sqiare(10)
# s2 = Sqiare(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     # if isinstance(g,Rectangle):
#     print(g.get_perimetr())
#     # else:
    #     print(g.get_per_sq())
    # els
# class Number:
#     def __init__(self,value):
#         self.value = value
#     def total(self,a):
#         return self.value + int(a)
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return str(self.value) + str(a)
# t1 = Number(10)
# t2 = Text("Убер")
# print(t1.total(35))
# print(t2.total(35))
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"I`m a Cat, my name is {self.name}, my age is {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} meows"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"I`m a Dog, my name is {self.name}, my age is {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} barks"
#
#
# c1 = Cat("Fluff", 2.5)
# d1 = Dog("Muhtar", 4)
#
# li = [c1, d1]
#
# for pet in li:
#     print(pet.info())
#     print(pet.make_sound())
# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'{self.surname} {self.name} {self.age}'
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, v1, group, ball):
#         self.v1 = v1
#         self.group = group
#         self.ball = ball
#         super().__init__(surname, name, age)
#
#     def info(self):
#         return f'{super().info()} {self.v1} {self.group} {self.ball}'
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub, rating):
#         self.sub = sub
#         self.rating = rating
#         super().__init__(surname, name, age)
#
#     def info(self):
#         return f'{super().info()} {self.sub} {self.rating}'
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, v1, group, ball, top):
#         self.top = top
#         super().__init__(surname, name, age, v1, group, ball)
#
#     def info(self):
#
#         return f'{super().info()} {self.top}'
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     print(i.info())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f"{self.__class__}:{self.name}"
#     def __str__(self):
#         return f"{self.name}"
#
# cat = Cat('Пушок')
#
# print(cat)

# class Point:
#     def __init__(self, *args):
#         print(args)
#         self.__coord = args
#     def __len__(self):
#         return len(self.__coord)
# p = Point(5,7,8)
#
# print(len(p))
# import math
# class Point:
#     __slots__ = ('x','y','__length')
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x*x+y*y)
#     @property
#     def lenght(self):
#         return self.__length
#     @lenght.setter
#     def length(self,value):
#         self.__length = value
#
# pt = Point(1,2)
# print(pt.length)
# pt.z = 3
#
# print(pt.__dict__)

# class Point:
#     __slots__ = ('x','y')
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# class Point2d:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1,2)
# pt2 =Point2d(1,2)
# print(pt2.__dict__)
# print("pt = ",pt.__sizeof__())
# print("pt2 = ",pt2.__sizeof__()+pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ('x','y')
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# class Point3D(Point):
#     __slots__ = 'z',
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z = z
#
# pt =Point(1,2)
# pt3= Point3D(10,20,30)
#
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)
# a =( '3',)
# print(type(a))

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()

class StripChars:
    def __init__(self, chars):
        self.__chars = chars
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)


s1= StripChars("?:!.;#")
print(s1("######Hello World!"))

def strip_chars(chars):
    def wrap(*args,**kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")
        return args[0].strip(chars)
    return  wrap
s1= strip_chars("?:!.;#")
print(s1("######Hello World!"))