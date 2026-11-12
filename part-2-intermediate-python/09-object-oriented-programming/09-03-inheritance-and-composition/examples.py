# 09-03 Inheritance and composition
import math


# Example 1: a base class and two subclasses that override a method
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Example 2: describe() is inherited; area() is each subclass's own
shapes = [Rectangle(3, 4), Circle(1)]
for shape in shapes:
    print(shape.describe())

# Example 3: isinstance and issubclass understand inheritance
print(isinstance(shapes[0], Rectangle), isinstance(shapes[0], Shape))
print(isinstance(shapes[0], Circle), issubclass(Circle, Shape))


# Example 4: a subclass of a subclass, extending a method with super()
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "square"

    def describe(self):
        return super().describe() + f" (side {self.width})"


print(Square(2).describe())
print([cls.__name__ for cls in Square.__mro__])


# Example 5: composition - a class that HAS other objects
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True


class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)   # a Car has an Engine

    def start(self):
        self.engine.start()
        return f"{self.model} started ({self.engine.horsepower} hp)"


car = Car("Roadster", 300)
print(car.start(), car.engine.running)


# Example 6: composition with a collection of parts
class Drawing:
    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum([shape.area() for shape in self.shapes])


drawing = Drawing()
drawing.add(Rectangle(2, 3))
drawing.add(Square(2))
print(drawing.total_area())
