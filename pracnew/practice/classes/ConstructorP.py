class Person:

    def __init__(self, n, o):
        print("hey i am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("harry", "developer")
b = Person("Divya", "hr")

a.info()
b.info()