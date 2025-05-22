class Person:
    name = "harry"
    occupation = "software engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()

a.info()
b.name = "shubham"

b.info()