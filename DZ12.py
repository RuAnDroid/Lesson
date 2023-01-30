import json
from random import randint, choice


def get_person():
    name = ''
    tel = ''
    n = ''
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(nums)

    n = 10

    person = {''.join(["{}".format(randint(0, 9)) for _ in range(0, n)]): {
        'name': name,
        'tel': tel
    }}
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person())
