import unittest
import math
from utils import geometry_utils

class TestGeometryUtils(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(geometry_utils.circle_area(3.0), math.pi * 9.0)
        self.assertEqual(geometry_utils.circle_area(0), 0)
        with self.assertRaises(ValueError):
            geometry_utils.circle_area(-3.0)

    def test_circle_circumference(self):
        self.assertAlmostEqual(geometry_utils.circle_circumference(3.0), 2.0 * math.pi * 3.0)
        self.assertEqual(geometry_utils.circle_circumference(0), 0)
        with self.assertRaises(ValueError):
            geometry_utils.circle_circumference(-3.0)

    def test_rect_area(self):
        self.assertEqual(geometry_utils.rect_area(5.0, 4.0), 20.0)
        self.assertEqual(geometry_utils.rect_area(0, 4.0), 0)
        with self.assertRaises(ValueError):
            geometry_utils.rect_area(-5.0, 4.0)

    def test_rect_perimeter(self):
        self.assertEqual(geometry_utils.rect_perimeter(5.0, 4.0), 18.0)
        with self.assertRaises(ValueError):
            geometry_utils.rect_perimeter(5.0, -4.0)

    def test_triangle_area(self):
        self.assertEqual(geometry_utils.triangle_area(6.0, 4.0), 12.0)
        with self.assertRaises(ValueError):
            geometry_utils.triangle_area(-6.0, 4.0)

    def test_triangle_perimeter(self):
        self.assertEqual(geometry_utils.triangle_perimeter(3.0, 4.0, 5.0), 12.0)
        with self.assertRaises(ValueError):
            geometry_utils.triangle_perimeter(3.0, 4.0, -5.0)

if __name__ == '__main__':
    unittest.main()
