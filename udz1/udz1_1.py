class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


x = 3
y = 4
rectangle = Rectangle(x, y)
rectangle.area()  # 12
