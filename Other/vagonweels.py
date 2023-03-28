from functools import reduce

lst = input('ВВедите число через пробел: ').split()
print(
    float(reduce(lambda x, y: (x + y), map(lambda x: ((x + 7) / 2), filter(lambda x: (x >= 5), list(map(int, lst)))))))
