import random
from enum import IntEnum

class Action(IntEnum):
    ROCK = 0 # камень
    PAPER = 1 # бумага
    SCISSORS = 2 # ножницы

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Сделайте выбор — ({choices_str}): "))
    action = Action(selection)
    return action
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
    elif user_action == Action.ROCK:
        if computer_action == Action.SCISSORS:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == Action.PAPER:
        if computer_action == Action.ROCK:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == Action.SCISSORS:
        if computer_action == Action.PAPER:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]" # проверка на правильность ввода
        print(f"Некорректный ввод. Введите значение из промежутка {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Сыграем еще? (д/н)(y/n): ")
    if play_again.lower() != "д" and play_again.lower() != "y": # Перевод нижний регистр если нужно перевести в верхний регистр и вернуть значение /n будем использовать upper так же есть универсальное зеначение swapcase()/n
        break