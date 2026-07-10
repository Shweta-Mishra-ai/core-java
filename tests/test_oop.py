import unittest
from utils import oop_demos

class TestOopDemos(unittest.TestCase):

    def test_child_multiple_inheritance(self):
        c = oop_demos.Child()
        self.assertEqual(c.expend(), 3000)

    def test_polymorphism(self):
        s = oop_demos.Shweta()
        r = oop_demos.Ram()
        
        self.assertEqual(s.myprint(), "Shweta implementation of myprint")
        self.assertEqual(s.calc(4), 16)
        
        self.assertEqual(r.myprint(), "Abstract class print method called")
        self.assertEqual(r.calc(4), 64)

    def test_simple_interest(self):
        si = oop_demos.SimpleInterestCalculator.get_simple_interest(1000.0, 5.0, 2.0)
        self.assertEqual(si, 100.0)
        
        with self.assertRaises(ValueError):
            oop_demos.SimpleInterestCalculator.get_simple_interest(-1000.0, 5.0, 2.0)

if __name__ == '__main__':
    unittest.main()
