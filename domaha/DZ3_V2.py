class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет # {self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print('*' * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        self.__num = num
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
    @property
    def percent(self):
        return self.__percent
    @percent.setter
    def percent(self, percent):
        self.__percent = percent
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
            self.print_balance()
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавленно')
        self.print_balance()

    def covert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета :{usd_val} {Account.suffix_usd}')

    def covert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета :{eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f"Текущий баланс: {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
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
