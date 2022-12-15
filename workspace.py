import math
h = int(input("ВВедите Ширина прямоугольника:"))
w = int(input("ВВедите Длинна прямоугольника:"))

class Rectangle:
    def weith_heith():
        print(f"Длинна прямоугольника:{h}\nШирина прямоугольника:{w}")
    weith_heith()
    def ploshad():
        z = h * w
        print(f"Площадь прямоугольника:{z}")
    ploshad()
    def perimetr():
        p = h * w * 2
        print(f"Периметр прямоугольника:{p}")
    perimetr()
    def gepotinuza():
        g = round(math.sqrt(h ** 2 + w ** 2), 2)
        print(f"Гипотинуза прямоугольника:{g}")
    gepotinuza()
    def print_cub():
        for x in range(h):
            for y in range(w):
                print("*", end='')
            print()
    print_cub()