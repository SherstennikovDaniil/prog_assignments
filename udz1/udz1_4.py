class Car:
    def __init__(self, color=None, type_=None, year=None):
        self.color = color
        self.type = type_
        self.year = year

    def start_engine(self):
        print("Автомобиль заведён")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def change_color(self, color):
        self.color = color

    def change_type(self, type_):
        self.type = type_

    def change_year(self, year):
        self.year = year


car = Car()
car.start_engine()  # Автомобиль заведён
car.stop_engine()  # Автомобиль заглушен

car.change_color("red")
print(car.color)  # red

car.change_type("sport")
print(car.type)  # sport

car.change_year(2014)
print(car.year)  # 2014
