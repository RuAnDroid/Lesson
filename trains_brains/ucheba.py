# class robot:
#     k = 0
#     def __init__(self, name):
#         self.name = name
#         print("инициализация робота:", self.name)
#         robot.k += 1
#     def __del__(self):
#         print(self.name, "выключается!")
#         robot.k -= 1
#         if robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("работающих роботов осталось:", robot.k)
#     def say_hi(self):
#         print("приветствую. меня зовут", self.name)
#
#
# droid1 = robot("r2-d2")
# droid1.say_hi()
# print("численность роботов:", robot.k)
#
# droid2 = robot("c-3po")
# droid2.say_hi()
# print("численность роботов:", robot.k)
# print("\nздесь роботы могут проделать какую-то работу\n")
# print("роботы закончили свою работу. давайте их выключим")
# del droid1
# del droid2
# print("численность роботов:", robot.k)
#
# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# # p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.get_coord())
# p1.set_coord(1, 2.3)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.set_coord_x(8)
# print(p1.get_coord_x())
# p1.set_coord_y(9)
# print(p1.get_coord_y())
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# print(p1.__dict__)
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#     @property
#     def x(self):  # получаем  __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # устанавливаем __set_x
#         print("Вызов __set_x")
#         self.__x = x
#     @x.deleter
#     def x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x

    # x = property(__get_x, __set_x, __del_x)


# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self,kg):
#         self.__kg = kg
#     @property
#     def kg(self):
#         return self.__kg
#     @kg.setter
#     def kg(self,new_kg):
#         if isinstance(new_kg,(int,float)):
#             self.__kg=new_kg
#         else:
#             print('Киллограмы передаются только числами')
#     def to_pounds(self):
#         return self.__kg*2.205
# weight =KgToPounds(12)
# print(weight.kg,"кг=>",end="")
# print(weight.to_pounds(),'фунтов')
# weight.kg = 41
# print(weight.kg,"кг=>",end="")
# print(weight.to_pounds(),'фунтов')
# weight.kg = 'Десять'
# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         del self.__age
# p1=Person("Vladimir",40)
# print(p1.name,p1.age)
# p1.name="Anna"
# p1.age =25
# print(p1.name,p1.age)
# del p1.name
# print(p1)
# class Point:
#     __count = 0
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(3, 15)
# p3 = Point(6, 23)
# print(Point.get_count)
# print(p1.get_count())
# class Change:
#     @staticmethod
#     def inc(x):
#         return x+1
#     @staticmethod
#     def dec(x):
#         return x-1
# print(Change.inc(10),Change.dec(10))
# class Args:
#     @staticmethod
#     def max(a,b,c,d):
#         return max(a,b,c,d)
#     @staticmethod
#     def min(a,b,c,d):
#         return min(a, b, c, d)
#     @staticmethod
#     def arf(a, b, c, d):
#         return (sum((a, b, c, d)))//4
#     @staticmethod
#     def factorial(x):
#         count = 1
#         for i in range(1, x + 1):
#             count *= i
#         return count
#
# print(Args.max(3,5,7,9))
# print(Args.min(3,5,7,9))
# print(Args.arf(3,5,7,9))
# print(Args.factorial(7))
# class Numbers:
#     @staticmethod
#     def max(*args):
#         _max = 0
#         for i in args:
#             _max = (_max if i < _max else i)
#         return _max
#
#
# print(Numbers.max(3,5,7,9,4,16,1))
# class Date:
#     def __init__(self,day=0,month=0,year=0):
#         self.day= day
#         self.month= month
#         self.year=year
#     @classmethod
#     def from_string(cls,date_as_string):
#         day,month,year=map(int,date_as_string.split('.'))
#         return cls(day,month,year)
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
# d = Date()
# string_date =d.from_string('23.10.2022')
# print(Date.string_to_db(string_date))
# string_date1=Date.from_string('21.12.2021')
# print(string_date1.string_to_db()
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет # {self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)
    def __del__(self):
        print('*'*50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")
    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate
    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self,val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
            self.print_balance()
        else:
                self.value -= val
                print(f'{val} {Account.suffix} было успешно снято')
                self.print_balance()
    def add_money(self,val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавленно')
        self.print_balance()

    def covert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета :{usd_val} {Account.suffix_usd}')

    def covert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета :{eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f"Текущий баланс: {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.covert_to_usd()
acc.covert_to_eur()
print()
Account.set_usd_rate(2)
acc.covert_to_usd()
Account.set_eur_rate(3)
acc.covert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percents()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
acc.withdraw_money(3000)
print()