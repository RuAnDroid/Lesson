# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#     def show(self):
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "654"
#
#         def display(self):
#             print("Name :", self.name)
#             print("Id:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#             self.id = "007"
#
#         def display(self):
#             print("Name :", self.name)
#             print("Id:", self.id)
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# print(d1.id)
# print()
#
# d2 = outer.head
# d2.display()

# class Computer:
#     def __init__(self,name, os1,brand,model):
#         self.name = name
#         self.os = self.OS(os1)
#         self.cpu = self.CPU(brand, model)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self,brand, model):
#             self.brand = brand
#             self.model1 = model
#         def make(self):
#             return self.brand
#
#         def model(self):
#             return self.model1
# comp = Computer("PC001","windows7","Intel","Core-i7")
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())
#
# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("in Base Class")
#
#     class Inner:
#         def display(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
# a = SubClass()
# a.display()
# # b = a.db
# b =SubClass.Inner()
# b.display()
# b.display2()
#
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, "is sleeping")
# class Pet(Creature):
#     def play(self):
#         print(self.name, "is playing")
# class Dog(Animal,Pet):
#     def bark(self):
#         print(self.name, "is barking")
#
# beast = Dog("Buddy")
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     def __init__(self):
#         print("A")
# class AA:
#     pass
# class B(A):
#     def __init__(self):
#         print("B")
#     def hi(self):
#         print("B_hi")
# class C(AA):
#     def __init__(self):
#         print("C")
#     def hi(self):
#         print("C_hi")
# class D(B,C):
#     # def __init__(self):
#     #     B().__init__(self)
#     #     C().__init__(self)
#     #     print("D")
#     pass
#     def hi(self):
#         C.hi(self)
#         print("D_hi")
# d = D()
# d.hi()
# print(D.mro())
# class Point:
#     def __init__(self, x =0 ,y=0) :
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x},{self.y}"
# class Style:
#     def __init__(self, color="red",width=1):
#         self._color = color
#         self._width = width
#         print("Инициализатор Style")
#
# class Pos:
#     def __init__(self, sp:Point, ep:Point,*args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
# class Line(Pos, Style):
#     # def __init__(self,sp:Point, ep:Point,color="red",width=1):
#     #     Pos.__init__(self,sp, ep)
#     #     Style.__init__(self,color, width)
#     def draw(self):
#         print(f"Рисование линии: {self._sp},{self._ep},{self._color},{self._width}")
#
# l1 =Line(Point(10,10),Point(100,100),"green",5)
# l1.draw()

class Displayer:
    @staticmethod
    def display(message):
        print(message)

class LoggerMixin:
    def log(self,message, filename="logfile.txt"):
        with open(filename, "a") as fh:
            fh.write(message)

    def display(self, message):
        Displayer.display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message, filename =""):
        super().log(message, filename ="subclasslog.txt")

sub = MySubClass()
sub.display("Строка будет отображаться и регистрироваться в файле")
