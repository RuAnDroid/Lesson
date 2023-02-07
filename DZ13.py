import json


class CitiInfo:

    def __init__(self):
        self.country = "country"
        self.capital = "capital"
        self.data = {"country": "capital"}

    @staticmethod
    def add_data():
        country = str(input("Введите название страны (с заглавной буквы)"))
        capital = str(input("Введите название столицы страны (с заглавной буквы)"))
        data = {country:capital}
        with open("data_base.json", 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print("Файл сохранён")
        CitiInfo.show_info()

    @staticmethod
    def del_data():
        data = []
        with open("data_base.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)
            print("Удаление прошло успешно")
        CitiInfo.show_info()

    @staticmethod
    def find_data():
        with open("data_base.json") as f:
            text = json.load(f)
            country = str(input("Введите название страны:"))
        for txt in text['data_base.json']:
            print(txt[country])
        CitiInfo.show_info()

    @staticmethod
    def edit_data():
        pass

        CitiInfo.show_info()
    @staticmethod
    def view_data():
        try:
            with open("data_base.json", "r") as f:
                data = json.load(f)
                print(data)
        except FileNotFoundError:
            data = {}
            with open('data_base.json', 'w') as f:
                json.load(data, f)

        CitiInfo.show_info()

    @staticmethod
    def show_info():
        print('*' * 30)
        print(
            f"Выбор действия:\n1 - добавление данных \n2 - удаление данных \n3 - поиск данных \n4 - редактирование данных \n5 - просмотр данных \n6 - завершение работы")
        p = int(input("ВВод :"))
        while True:
            if p == 1:
                return CitiInfo.add_data()
            if p == 2:
                return CitiInfo.del_data()
            if p == 3:
                return CitiInfo.find_data()
            if p == 4:
                return CitiInfo.edit_data()
            if p == 5:
                return CitiInfo.view_data()
            if p == 6:
                break
            else:
                raise TypeError("Введите значение от 1 до 6")


CitiInfo.show_info()
