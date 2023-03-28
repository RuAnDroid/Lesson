# class Goods:
#     def __init__(self,name,weigth,price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weigth = weigth
#         self.price = price
#     def print_info(self):
#         print(f"{self.name} ,{self.weigth}кг, {self.price}RUB")
# class MixinLog:
#     ID = 0
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())

# Перегрузка Операторов
#24*60*60=86400(число секунд в одном дне)

# class Clock:
#     DAY = 86400
#
#     def __init__(self,sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#     def get_format_time(self):
#         s = self.sec % 60
#         m =(self.sec//60) % 60
#         h =(self.sec//3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#     def __add__(self, other ):
#         if not isinstance(other, Clock):
#             raise  ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#     def __sub__(self, other):
#         if not isinstance(other , Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#     def __mul__(self, other):
#         if not isinstance(other , Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#     def __floordiv__(self, other):
#         if not isinstance(other , Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#     def __gt__(self, other):
#         return self.sec == other.sec
#     def __ge__(self, other):
#         return self.sec == other.sec
# c1 = Clock(2100)
# c2 = Clock(300)
# # c1 += c2
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c2 >= c1:
#     print("Первый больше")
# else:
#     print("Второй больше")
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# class Student:
#     def __init__(self,name ,marks):
#         self.name = name
#         self.marks = list(marks)
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#     def __setitem__(self, key, value):
#         if not isinstance(key , int) or key < 0:
#             raise TypeError("Индекс должен быть целым не отрицательным числом")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None]*off)
#
#         self.marks[key] = value
#     def __delitem__(self, key):
#         if not isinstance(key , int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
# s1 = Student("Сергей", [5,5,3,4,5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# # print(s1.marks[2])
# print(s1.marks)
class Clock:
    DAY = 86400

    def __init__(self,sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY
    def get_format_time(self):
        s = self.sec % 60
        m =(self.sec//60) % 60
        h =(self.sec//3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __getitem__(self, item):
        if not isinstance(item , str):
            raise  ValueError(" Ключ должен быть строкой")
        if item == "hour":
            return  (self.sec//3600)%24
        elif item == "min":
            return  (self.sec // 60)% 60
        elif item == "sec":
            return  self.sec % 60
        return  "Неверный ключ"
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError(" Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError(" Значение должно быть целым числом")
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec//3600) % 24
        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        if key == "min":
            self.sec = s + 60 * value +h * 3600
        if key == "sec":
            self.sec = value +60 * m +h * 3600


c1 = Clock(80000)
print(c1.get_format_time())
c1["hour"] = 10
c1["min"] = 21
c1["sec"] = 15
print(c1["hour"], c1["min"], c1["sec"])
print(c1.get_format_time())
