# import random
#
#
# class Cat:
#     def __init__(self, name,age, pol):
#         self.name = name
#         self.pol = pol
#         self.age = age
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return  f"Cat(name = '{self.name}', age = {self.age}, sex ='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, random.choice(['M', 'F'])) for _ in range(1,(random.randint(2,7)))]
#         else:
#             return "Types are not support"
#             # raise  TypeError("Types are not support")
# cat1 = Cat("Tom", 4,"M")
# # print(cat1)
# cat2 = Cat("Elsa", 5, "F")
# # print(cat2)
# # print(cat1 + cat2)
# cat3 = Cat("Ron", 3, "M")
# # print(cat3)
# # print(cat1+cat3)
# # print((cat2 + cat3))
# lst = (cat1, cat2, cat3)
# b, c = random.choices(lst, k = 2)
# print(b + c)
#
# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         return str(res) + '\nПосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# # test = MyDecorator(func)
# # print(test(2, 5))
#
# print(func(2, 5))
#
# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print(func(2, 3))
#
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('Перед вызовом функции')
#             print(self.name, end=": ")
#             fn(a, b)
#             print('После вызова функции')
#         return wrap
#
#
# # @MyDecorator
# # def func(a, b):
# #     return a * b
# #
# # @MyDecorator
# # def func1(a, b, c):
# #     return a * b * c
# #
# # @MyDecorator
# # def func2(a, b, c):
# #     return a * b * c
#
# # test = MyDecorator(func)
# # print(test(2, 5))
# #
# # print(func(2, 5))
# # print(func1(2, 5,2))
# # print(func2(2, 5,c =3))
#
# @MyDecorator('test2')
# def func(a, b):
#     print(a, b)
#
# func(2,5)

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# p.name.set("Олег")
# print(p.name.get(), p.surname.get())

class ValidateString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} Должно быть строкой")
        instance.__dict__[self.__name] = value


class Person:
    name = ValidateString()
    surname = ValidateString()


    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

p = Person("Иван", "Петров")
p.name = "Света"
print(p.name)
print(p.surname)

