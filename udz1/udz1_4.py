class Car:
    def __init__(self, color=None, _type=None, year=None) -> None:
        self.color = color
        self.type = _type
        self.year = year

    def start_engine():
        print("Автомобиль заведён")

    def stop_engine():
        print("Автомобиль заглушен")

    def change_color(self, color):
        self.color = color

    def change_type(self, _type):
        self.type = _type

    def change_year(self, year):
        self.year = year
