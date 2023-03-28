# from car import electrocar
#
#
# def main():
#     e_car = electrocar.ElectroCar("Tesla", "T", 2020, 50000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()


import pickle

#
# filename = "basket1.txt"
#
#
# shop_list = {
#
#      "фрукты": ["яблоки", "манго"],
#         "овощи": ["морковь"],
#             "бюджет": 1000
#
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
#
# with open(filename, 'rb') as fh:
#     shop = pickle.load(fh)
#
# print(shop)

# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1,2,3]
#     d= {"first":"a", "second": 2}
#     tpl =(22,33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl} "
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
#
# print(f"Сериализация в строку: \n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
#
# print(f"Десериализация в строку: \n{l_obj}\n")
import json
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

import json

data = {
    'name': 'Игорьььь',
    'hobby': ('drink','drags'),
    'age': 20,
    'children' : [
        {
            'firsname' : 'Alice',
            'age': 5
        },
        {
            'firsname': 'Boobs',
            'age': 8
        }
    ]
}

# with open("data_file.json", 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", 'r') as fw:
#     data = json.load(fw)
#     print(data)


json_string = json.dumps(data, ensure_ascii=False)
print(json_string)
data = json.loads(json_string)

print(data)


