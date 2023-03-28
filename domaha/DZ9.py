

class Power:
    def __init__(self, fn):
        self.func = fn

    def __call__(self, a, b):
        return f'Результат : {(a * b) ** self.func(a, b)}'


@Power
def func(a, b):
    return a * b


c = func(2, 2)

print(c)
