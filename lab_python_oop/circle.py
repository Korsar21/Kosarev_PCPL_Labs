import math
from .figure import GeometricFigure
from .color import FigureColor

class Circle(GeometricFigure):
    shape_name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"{self.shape_name}: радиус {self.radius}, {self.color}, площадь: {self.area():.2f}"
