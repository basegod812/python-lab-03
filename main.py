"""ЛР3, вариант 2: классы Student, Figure, Vector, Factory, NumberList."""
from abc import ABC, abstractmethod
from math import pi


class Student:
    def __init__(self, full_name: str, group: str):
        self.full_name = full_name
        self.group = group

    def information(self):
        return f"Студент: {self.full_name}; группа: {self.group}"


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными")
        self.width, self.height = width, height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Vector:
    """Среднее №7: перегрузка оператора сложения объектов."""
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


class FigureFactory:
    """Повышенное №2: фабрика объектов фигур."""
    @staticmethod
    def create(kind: str, **values) -> Figure:
        if kind == "circle":
            return Circle(values["radius"])
        if kind == "rectangle":
            return Rectangle(values["width"], values["height"])
        raise ValueError(f"Неизвестная фигура: {kind}")


class NumberList(list):
    """Повышенное №6: наследование от стандартного list."""
    def average(self) -> float:
        if not self:
            raise ValueError("Среднее пустого списка не определено")
        return sum(self) / len(self)

    def only_even(self):
        return NumberList(x for x in self if x % 2 == 0)


def main():
    print(Student("Шкловский Герман Вячеславович", "221141").information())
    figure = FigureFactory.create("circle", radius=3)
    print(f"Площадь круга: {figure.area():.2f}; периметр: {figure.perimeter():.2f}")
    print("Сложение векторов:", Vector(2, 3) + Vector(4, 5))
    numbers = NumberList([1, 2, 3, 4, 5, 6])
    print("Среднее:", numbers.average(), "Чётные:", numbers.only_even())


if __name__ == "__main__":
    main()
