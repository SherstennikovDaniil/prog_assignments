class Soda:
    def __init__(self, flavour=None):
        self.flavour = flavour

    def show_my_drink(self):
        if self.flavour:
            print(f"Газировка и {self.flavour}")
        else:
            print("Обычная газировка")


regular = Soda()  # flavour=None
regular.show_my_drink()  # Обычная газировка

fanta = Soda("апельсин")  # flavour="апельсин"
regular.show_my_drink()  # Газировка и апельсин
