import unittest
from polynomial import Polynomial

class PolynomialUnitTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Polynomial([3,-2,0,-2])
        self.p2 = Polynomial([-1,1,3,0])
        self.p3 = Polynomial([0,-2,0,0])


    #добавить проверку на выбрасывание исключений для невалидных данных

    def test_init_p1(self):
        self.assertEqual([3,-2,0,-2],self.p1.coefficients)

    def test_init_p3(self):
        self.assertEqual([-2,0,0],self.p3.coefficients)

    def test_str_p1(self):
        self.assertEqual("3x^3 - 2x^2 - 2", str(self.p1))

    def test_str_p2(self):
        self.assertEqual("-x^3 + x^2 + 3x", str(self.p2))

    def test_str_p3(self):
        self.assertEqual("-2x^2", str(self.p3))