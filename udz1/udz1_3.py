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


math1 = Math1(6, 3)
math1.addition()  # 9
math1.substraction()  # 3
math1.multiplication()  # 18
math1.division()  # 2.0


class Math2:
    def __init__(self):
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


Math2.addition(6, 3)  # 9
Math2.substraction(6, 3)  # 3
Math2.multiplication(6, 3)  # 18
Math2.division(6, 3)  # 2.0
