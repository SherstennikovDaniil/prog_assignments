# Lab1
 ### [`Task 1`](https://github.com/SherstennikovDaniil/prog_assignments/blob/main/udz1/udz1_1.py)
Напишите программу с классом `Rectangle`, который построенный по длине и
 ширине, и метод, который будет вычислять площадь прямоугольника
 
 ---
 ```
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
```
* Метод `__init__` - конструктор, который принимает аргумент `width` и `height`. Когда в коде вызывается 
```Rectangle(x, y)```, создаётся объект класса `Rectangle` с заданными переменными.

* Метод `area` возвращает площать объекта используя заданные при инициализации параметры.