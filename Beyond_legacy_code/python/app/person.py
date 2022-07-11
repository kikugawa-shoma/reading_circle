class Person():
    MINIMUM_AGE = 1
    MAXIMUM_AGE = 200

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
