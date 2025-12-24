import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestFigures(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(3, 4,  "синий")
        self.assertEqual(rect.area(), 12)

    def test_circle_area(self):
        circle = Circle(2, "зелёный")
        self.assertAlmostEqual(circle.area(), 3.141592653589793 * 4, places=5)

    def test_square_area(self):
        square = Square(5, "красный")
        self.assertEqual(square.area(), 25)

    def test_repr_contains_name(self):
        rect = Rectangle(3, 4, "синий")
        self.assertIn("Прямоугольник", repr(rect))
        circle = Circle(2, "зелёный")
        self.assertIn("Круг", repr(circle))
        square = Square(5, "красный")
        self.assertIn("Квадрат", repr(square))


if __name__ == "__main__":
    unittest.main()
