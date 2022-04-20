class Soda:
    def __init__(self, flavour=None):
        self.flavour = flavour

    def show_my_drink(self):
        if self.flavour:
            print(f"Газировка и {self.flavour}")
        else:
            print("Обычная газировка")
