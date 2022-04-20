class Country:
    pass


class Russia(Country):
    capital = "Moscow"
    population = 0

    def setPopulation(cls, population):
        cls.population = population

    def getPopulation(cls):
        return cls.population


class Canada(Country):
    capital = "Ottawa"
    population = 0

    def setPopulation(cls, population):
        cls.population = population

    def getPopulation(cls):
        return cls.population


class Germany(Country):
    capital = "Berlin"
    population = 0

    def setPopulation(cls, population):
        cls.population = population

    def getPopulation(cls):
        return cls.population


russia = Russia()
russia.setPopulation(144_100_000)

canada = Canada()
canada.setPopulation(38_010_000)

germany = Germany()
germany.setPopulation(83_240_000)
