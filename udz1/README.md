# Lab1
 ### [`Task 1`](https://github.com/SherstennikovDaniil/prog_assignments/blob/main/udz1/udz1_1.py)
Напишите программу с классом `Rectangle`, который построенный по длине и
 ширине, и метод, который будет вычислять площадь прямоугольника
 
 ---
 ```python
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
---
---
### [`Task 2`](https://github.com/SherstennikovDaniil/prog_assignments/blob/main/udz1/udz1_2.py)

Напишите программу с классом `Soda` (для определения типа газированной
воды), который принимает 1 аргумент при инициализации (отвечающий за добавку
к выбираемому лимонаду). 

В классе реализуйте метод `show_my_drink()`, выводящий
на печать *«Газировка и `{ДОБАВКА}`»* в случае наличия добавки, а иначе отобразится
следующая фраза: *«Обычная газировка»*.
***
```python
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
```
* Метод `__init__` выполняет ту же функцию, что и в прошлом(и последующем) задании, создаёт объект класса. Но в данном задании переменной `flavour` было задано значение по умолчанию. 
  
  Если при создании будет задан вкус(передан аргумент), то значение `flavour` будет равно переданному аргументу, в случае отсутсвия оного, значение переменной `flavour` будет `None`.
* Метод `show_my_drink()` выводить данные о напитке в `STDOUT` в зависимости от значения переменной `flavour` объекта `Soda`.
  
  Если значение `flavour` - `None`:
  > Обычная газировка
  
  В ином случае:
  > Газировка и <значение переменной flavour>
  
  
 ---
 ---