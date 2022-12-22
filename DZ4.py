class Car:
    def __init__(self, model, year, mf, power, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = mf
        self.__power = power
        self.__color = color
        self.__price = price
    @staticmethod
    def car_info():
        print(("*" * 10), "Данные автомобиля", ("*" * 10))
    @property
    def model_info(self):
        return f"Название модели: {self.__model}"
    @model_info.setter
    def model_info(self, model):
        self.__model = model

    @property
    def year_info(self):
        return f"Год выпуска: {self.__year}"

    @year_info.setter
    def year_info(self, year):
        self.__year = year

    @property
    def mf_info(self):
        return f"Производитель: {self.__manufacturer}"

    @mf_info.setter
    def price_info(self, mf):
        self.__manufacturer = mf

    @property
    def power_info(self):
        return f"Мощность двигателя: {self.__power}"

    @power_info.setter
    def power_info(self, power):
        self.__power = power

    @property
    def color_info(self):
        return f"Цвет машины: {self.__color}"

    @color_info.setter
    def color_info(self, color):
        self.__color = color

    @property
    def price_info(self):
        return f"Цена: {self.__price} рублей"

    @price_info.setter
    def price_info(self, price):
        self.__price = price
    @staticmethod
    def close_info():
        print("=" * 39)

p1 = Car("X7 M50i",2021,"BMW","530 л.с.","white",10790000)

Car.car_info()
Car.model_info
print(p1.model_info)
Car.year_info
print(p1.year_info)
Car.mf_info
print(p1.mf_info)
Car.power_info
print(p1.power_info)
Car.color_info
print(p1.color_info)
Car.price_info
print(p1.price_info)
Car.close_info()

