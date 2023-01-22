class Integer:
    @staticmethod
    def verify_coord(coord):
        if not isinstance(coord, int):
            raise TypeError(f'Координата {coord} должна быть целым числом')
        elif coord < 1:
            raise TypeError(f'Координата {coord} должна быть не меньше 1')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value



class Triangle:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Треугольник со сторонами ({self.x},{self.y},{self.z})"


    def verify_tri(self):
        if self.x + self.y > self.z and self.y + self.z > self.x and self.x + self.z > self.y:
            return f'Треугольник со сторонами: ({self.x},{self.y},{self.z}) существует.'
        else:
            return f'Треугольник со сторонами: ({self.x},{self.y},{self.z}) не существует.'

t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)


print(t1.verify_tri())
print(t2.verify_tri())
print(t3.verify_tri())
# print(t1)
# print(t2)
# print(t3)
