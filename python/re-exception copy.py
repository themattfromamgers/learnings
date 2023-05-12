class Person:

    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla")
        else:
            self.name = name


p = Person("burakyabguu", 1931)
    