import re
from pprint import pprint

# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И',
#         # 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 120:  # old < 14 or old > 120
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         p = ps.split()
#         if len(p) != 2 or len(p[0]) != 4 or len(p[1]) != 6:
#             raise TypeError("Неверный формат серии-номера паспорта")
#         for o in p:
#             if not o.isdigit():
#                 raise TypeError("Серия и номер паспорта должны состоять из чисел!")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# # p1.fio="Сидорова Марина Владимировна"
# # print(p1.fio)
# # print(p1.__dict__)
# pprint(p1.__dict__)
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x},{self.__y})"


# print(issubclass(Point,object))
# print(dir(Point))
class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        print("Инициализатор базового класса")
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width
    def get_width(self):
        return self.__width

class Line(Prop):
    def __init__(self, *args):
        print("Переопределённый инициализатор Line")
        super().__init__(*args)
        # Prop.__init__(self,*args)

    def draw_line(self):
        print(f"Рисование линии: {self._sp},{self._ep},{self._color},{self.get_width()}")


class Rect(Prop):
    def __init__(self, *args, bg="yellow"):
        super().__init__(*args)
        self._background = bg

    def draw_rect(self):
        print(f"Рисование Прямоугольника: {self._sp},{self._ep},{self._color},{self.get_width()},{self._background}")


line = Line(Point(1, 2), Point(10, 20))

line.draw_line()
rect = Rect(Point(10, 20), Point(10, 20))
rect.draw_rect()
