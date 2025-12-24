from .figure import GeometricFigure
from .color import FigureColor

class Rectangle(GeometricFigure):
    shape_name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.shape_name}: {self.width}x{self.height}, {self.color}, площадь: {self.area()}"
