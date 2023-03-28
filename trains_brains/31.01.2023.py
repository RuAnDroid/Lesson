# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += f'[i],'
#         a = ', '.join(map(str, self.marks))
#         return f' Студент: {self.name}: {a}'
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def change_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_to_json(stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_to_file(filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.group = group
#         self.students = students
#
#     def __str__(self):
#         # a = ''
#         # for i in self.students:
#         #     a += str(i) + "\n"
#         a = '\n'.join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#
#     @staticmethod
#     def dump_group(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#     @staticmethod
#     def upload_journal(file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
#
# # Student.dump_to_json(st1, 'student.json')
# # Student.load_to_file('student.json')
# #
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# # # Student.dump_to_json(st2, 'student.json')
# # # Student.load_to_file('student.json')
# #
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# # Student.dump_to_json(st3, 'student.json')
# # Student.load_to_file('student.json')
#
# sts = [st1, st2]
#
# my_group = Group(sts, "ГК Python")
# # print(my_group)
# # print()
# # my_group.add_student(st3)
# # print(my_group)
# # print()
# # my_group.remove_student(1)
# # print(my_group)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.change_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())
# group22 = [st3]
# # print()
# my_group2 = Group(group22, "ГК Web")
# Group.dump_group('group.json', my_group)
# Group.dump_group('group.json', my_group2)
# Group.upload_journal('group.json')
# # # print(my_group2)
# # Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print()
# # print(my_group2)

import requests
import json
from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

# pprint(todos[:10])
# print(type(todos))

todos_by_user = {}

for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(dict(top_users))
max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

# print(users)
max_users = " and ".join(users)
s = 's' if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")


def keep(tod):
    is_complete = tod['completed']
    has_max_count = str(tod['userId']) in users
    return is_complete and has_max_count


with open('filtered_data_file.json', 'w') as f:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, f, indent=2)

with open('filtered_data_file.json', 'r') as f:
    data = json.load(f)
    print(data)

