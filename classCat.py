class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age
    def __repr__(self):
        return f'Кота зовут {self.name}, пол: {self.sex}, ему {self.age} лет(года)'