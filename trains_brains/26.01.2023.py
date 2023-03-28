# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#         }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # a = ''
        # for i in self.marks:
        #     a += f'[i],'
        a = ', '.join(map(str, self.marks))
        return f' Студент: {self.name}: {a}'

    def add_marks(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def change_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)


class Group:
    def __init__(self, students, group):
        self.group = group
        self.students = students

    def __str__(self):
        # a = ''
        # for i in self.students:
        #     a += str(i) + "\n"
        a = '\n'.join(map(str, self.students))
        return f"Группа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])

st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])

sts = [st1, st2]

my_group = Group(sts, "ГК Python")
# print(my_group)
# print()
my_group.add_student(st3)
# print(my_group)
# print()
my_group.remove_student(1)
# print(my_group)
# st1.add_marks(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.change_mark(2, 4)
# print(st1)
# print(st1.average_mark())
group22 = [st2]
print()
my_group2 = Group(group22, "ГК Web")
# print(my_group2)
Group.change_group(my_group, my_group2, 0)
print(my_group)
print()
print(my_group2)
