import math

class Shape:
    def area(self):
        """Base area method meant to be overridden."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of a circle."""
        return math.pi * (self.radius ** 2)
