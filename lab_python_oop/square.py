from .rectangle import Rectangle

class Square(Rectangle):
    shape_name = "Квадрат"

    def __init__(self, side, color):
        Rectangle.__init__(self, side, side, color)

    def __repr__(self):
        return f"{self.shape_name}: сторона {self.width}, {self.color}, площадь: {self.area()}"
