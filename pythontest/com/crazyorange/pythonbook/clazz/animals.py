class Animals():
    def __init__(self, name):
        self.name = name


class Dog(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.type = DogType()

    def getType(self):
        return self.type.getTypeName()


class DogType():
    def __init__(self):
        self.type = 'dog'
        print('dogtype : ' + self.type)

    def getTypeName(self):
        return self.type
