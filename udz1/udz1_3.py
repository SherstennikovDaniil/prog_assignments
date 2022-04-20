class Math1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def substraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)


class Math2:
    def __init__(self) -> None:
        pass

    @staticmethod
    def addition(a, b):
        print(a + b)

    @staticmethod
    def substraction(a, b):
        print(a - b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        print(a / b)
