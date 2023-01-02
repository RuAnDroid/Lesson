class Student:
    def __init__(self, name):
        self.name = name
        self.info = self.Info()

    def show(self):
        print(f"{self.name} =>, {self.Info().pc},{self.Info().model},{self.Info().ram}")

    class Info:
        def __init__(self, pc="HP", model="I7", ram="16"):
            self.pc = pc
            self.model = model
            self.ram = ram

    #comp = Info("HP","I7",16)
user1 = Student("Roman")
user2 = Student("Владимир")
user1.show()
user2.show()
print()
# d1.display()
# print(d1.id)
# print()
