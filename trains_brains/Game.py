import random
while True:
    random_number = random.randint(1,5)
    user_number = int(input("Угадайте число от 1 до 5:" ))
    if user_number != random_number:
        print(f"Попробуйте ещё раз" )
        print(f"Было загадано {random_number}")
        continue
    else:
        print(f"Ура вы угадали число {user_number}")

        break