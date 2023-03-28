class FigureСount:
    __Count = 0

    @staticmethod
    def PloshadGerona(a,b,c):
        FigureСount.__Count += 1
        return float(a + b + c) // 2
    @staticmethod
    def PloshadHight(b,h):
        FigureСount.__Count += 1
        return  float(b*h//2)

    @staticmethod
    def PloshadCub(a):
        FigureСount.__Count += 1
        return  a**2

    @staticmethod
    def PloshadRectangle(a,b):
        FigureСount.__Count += 1
        return a*b
    @staticmethod
    def get_count():
        return FigureСount.__Count
p1 = FigureСount.PloshadGerona(3,4,5)
p2 = FigureСount.PloshadHight(6,7)
p3 = FigureСount.PloshadCub(7)
p4 = FigureСount.PloshadRectangle(2,6)
print(f"Площадь треугольника по формуле Герона (3,4,5): {p1}")
print(f"Площадь треугольника через основание и высоту (6,7): {p2}")
print(f"Площадь квадрата (7): {p3}")
print(f"Площадь прямоугольника (2,6): {p4}")
print(f"Количество подсчетов площади: {FigureСount.get_count()}")
