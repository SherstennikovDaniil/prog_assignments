class Game:
    Year = 0

    def __init__(self, year, name=None):
        self.Year = year
        self.name = name

    def getName(self):
        return self.name


class PCGames(Game):
    def __init__(self, year, os, name=None):
        super().__init__(year, name)
        self.os = os

    def getName(self):
        return super().getName()

    def getOs(self):
        return self.os


class PS4Games(Game):
    def __init__(self, year, genre, name=None):
        super().__init__(year, name)
        self.genre = genre

    def getName(self):
        return super().getName()

    def getGenre(self):
        return self.genre


class XboxGames(Game):
    def __init__(self, year, genre, name=None):
        super().__init__(year, name)
        self.genre = genre

    def getName(self):
        return super().getName()

    def getGenre(self):
        return self.genre


class MobileGames(Game):
    def __init__(self, year, platform, name=None):
        super().__init__(year, name)
        self.platform = platform

    def getName(self):
        return super().getName()

    def getPlatform(self):
        return self.platform
