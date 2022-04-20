class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ToyTerrier(Dog):
    voice = "Woof"


class Spaniel(Dog):
    voice = "Aoooo"


class GermanShepherd(Dog):
    voice = "*bark-bark*"


dog1 = Spaniel("Wolter", 5)
dog2 = GermanShepherd("Alex", 7)
dog3 = ToyTerrier("Larry", 1)
dog4 = Spaniel("Lucy", 10)
dog5 = GermanShepherd("Max", 14)
