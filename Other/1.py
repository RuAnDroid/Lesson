# class MyClass:
#     pass
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)
# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)
# class Star:
#    def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#    def __str__(self):
#        return self.name + ' in ' + self.galaxy
#
# sun = Star("Sun", "Milky Way")
# print(sun)
# class SampleClass:
#     def __init__(self, val):
#         self.val = val
# ob1 = SampleClass(0)
# ob2 = SampleClass(2)
# ob3 = ob1
# ob3.val += 1
# print(ob1 is ob2)
# print(ob2 is ob3)
# print(ob3 is ob1)
# print(ob1.val, ob2.val, ob3.val)
# str1 = "Mary had a little "
# str2 = "Mary had a little lamb"
# str1 += "lamb"
# print(str1 == str2, str1 is str2)
# class Level1:
#     varia1 = 100
#
#     def __init__(self):
#         self.var1 = 101
#
#     def fun1(self):
#         return 102
#
#
# class Level2(Level1):
#     varia2 = 200
#
#     def __init__(self):
#         super().__init__()
#
#         self.var2 = 201
#
#     def fun2(self):
#         return 202
# class Level3(Level2):
#     varia3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var3 = 301
#     def fun3(self):
#         return 302
# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())
# class Left:
#     var = "L"
#     varLeft = "LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var = "R"
#     varRight = "RR"
#     def fun(self):
#         return "Right"
# class Sub(Left, Right):
#     pass
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())
# class One:
#     def doit(self):
#         print("doit from One")
#     def doanything(self):
#         self.doit()
# class Two(One):
#     def doit(self):
#         print("doit from Two")
# one = One()
# two = Two()
# one.doanything()
# two.doanything()
# import time
# class Tracks:
#     def changedirection(self, left, on):
#          print("tracks: ", left, on)
# class Wheels:
#     def changedirection(self, left, on):
#         print("wheels: ", left, on)
# class Vehicle:
#     def __init__(self, controller):
#         self.controller = controller
#     def turn(self, left):
#         self.controller.changedirection(left, True)
#         time.sleep(0.25)
#         self.controller.changedirection(left, False)
# wheeled = Vehicle(Wheels())
# tracked = Vehicle(Tracks())
# wheeled.turn(True)
# tracked.turn(False)
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#     return n
# print(reciprocal(2))
# print(reciprocal(0))
# def printExcTree(thisclass, nest = 0):
#     if nest > 1:
#         print(" |" * (nest - 1), end="")
#     if nest > 0:
#         print(" +---", end="")
#     print(thisclass.__name__)
#     for subclass in thisclass.__subclasses__():
#         printExcTree(subclass, nest + 1)
# printExcTree(BaseException)
# def printargs(args):
#     lng = len(args)
#     if lng == 0:
#         print("")
#     elif lng == 1:
#         print(args[0])
#     else:
#         print(str(args))
#     try:
#         raise Exception
#     except Exception as e:
#         print(e, e.__str__(), sep=' : ' ,end=' : ')
#         printargs(e.args)
#     try:
#         raise Exception("my exception")
#     except Exception as e:
#         print(e, e.__str__(), sep=' : ', end=' : ')
#         printargs(e.args)
#     try:
#         raise Exception("my", "exception")
#     except Exception as e:
#         print(e, e.__str__(), sep=' : ', end=' : ')
#         printargs(e.args)
# class MyZeroDivisionError(ZeroDivisionError):
#     pass
# def doTheDivision(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:
#             raise ZeroDivisionError("some bad news")
# for mode in [False, True]:
#     try:
#         doTheDivision(mode)
#     except ZeroDivisionError:
#         print('Division by zero')
# for mode in [False, True]:
#     try:
#         doTheDivision(mode)
#     except MyZeroDivisionError:
#         print('My division by zero')
#     except ZeroDivisionError:
#         print('Original division by zero')
class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):

        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100',
                 message=''):

        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def makePizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa',
                     'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110),
                 ('mafia', 20)]:
    try:
        makePizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
