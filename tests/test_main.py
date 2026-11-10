import unittest
from main import Student, Circle, Rectangle, Vector, FigureFactory, NumberList


class LabTests(unittest.TestCase):
    def test_student(self):
        self.assertIn("221141", Student("Герман", "221141").information())

    def test_figures(self):
        self.assertAlmostEqual(Circle(2).area(), 12.566370614359172)
        self.assertEqual(Rectangle(3, 4).perimeter(), 14)

    def test_vector(self):
        self.assertEqual(Vector(1, 2) + Vector(3, 4), Vector(4, 6))

    def test_factory(self):
        self.assertEqual(FigureFactory.create("rectangle", width=2, height=3).area(), 6)

    def test_extended_list(self):
        self.assertEqual(NumberList([1, 2, 3, 4]).average(), 2.5)
        self.assertEqual(NumberList([1, 2, 3, 4]).only_even(), [2, 4])


if __name__ == "__main__":
    unittest.main()
