from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests  # пример вызова внешней библиотеки

if __name__ == "__main__":
    N = 5


    rect = Rectangle(N, N + 2, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rect)
    print(circle)
    print(square)

    response = requests.get("https://api.github.com")
    print(f"Код ответа от GitHub API: {response.status_code}")
