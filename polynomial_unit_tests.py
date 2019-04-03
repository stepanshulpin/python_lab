import unittest
from polynomial import Polynomial


class PolynomialUnitTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Polynomial([3, -2, 0, -2])
        self.p2 = Polynomial([-1, 1, 3, 0])
        self.p3 = Polynomial([0, -2, 0, 0])

    def test_init_value_error(self):
        self.assertRaises(ValueError, Polynomial, [0, 0, 0])

    def test_init_type_error(self):
        self.assertRaises(TypeError, Polynomial, "Hello")

    def test_init_p1(self):
        self.assertEqual([3, -2, 0, -2], self.p1.coefficients)

    def test_init_p3(self):
        self.assertEqual([-2, 0, 0], self.p3.coefficients)

    def test_str_p1(self):
        self.assertEqual("3x^3 - 2x^2 - 2", str(self.p1))

    def test_str_p2(self):
        self.assertEqual("-x^3 + x^2 + 3x", str(self.p2))

    def test_str_p3(self):
        self.assertEqual("-2x^2", str(self.p3))

    def test_repr_p1(self):
        self.assertEqual("Polynomial([3, -2, 0, -2])", repr(self.p1))

    def test_repr_p2(self):
        self.assertEqual("Polynomial([-1, 1, 3, 0])", repr(self.p2))

    def test_repr_p3(self):
        self.assertEqual("Polynomial([-2, 0, 0])", repr(self.p3))

    def test_add_p1_p2(self):
        self.assertEqual(Polynomial([2, -1, 3, -2]), self.p1 + self.p2)

    def test_add_p2_p3(self):
        self.assertEqual(Polynomial([-1, -1, 3, 0]), self.p2 + self.p3)

    def test_add_p1_p3(self):
        self.assertEqual(Polynomial([3, -4, 0, -2]), self.p1 + self.p3)

    def test_add_p1_const(self):
        self.assertEqual(Polynomial([3, -2, 0, 1]), self.p1 + 3)

    def test_add_const_p1(self):
        self.assertEqual(Polynomial([3, -2, 0, 1]), 3 + self.p1)

    def test_add_type_error(self):
        self.assertRaises(TypeError, self.p1.__add__, "Hello")

    def test_sub_p1_p2(self):
        self.assertEqual(Polynomial([4, -3, -3, -2]), self.p1 - self.p2)

    def test_sub_p2_p3(self):
        self.assertEqual(Polynomial([-1, 3, 3, 0]), self.p2 - self.p3)

    def test_sub_p1_p3(self):
        self.assertEqual(Polynomial([3, 0, 0, -2]), self.p1 - self.p3)

    def test_sub_p1_const(self):
        self.assertEqual(Polynomial([3, -2, 0, -5]), self.p1 - 3)

    def test_sub_const_p1(self):
        self.assertEqual(Polynomial([-3, 2, 0, 5]), 3 - self.p1)

    def test_sub_type_error(self):
        self.assertRaises(TypeError, self.p1.__sub__, "Hello")

    def test_mul_p1_p2(self):
        self.assertEqual(Polynomial([-3, 5, 7, -4, -2, -6, 0]), self.p1 * self.p2)

    def test_mul_p2_p3(self):
        self.assertEqual(Polynomial([2, -2, -6, 0, 0, 0]), self.p2 * self.p3)

    def test_mul_p1_p3(self):
        self.assertEqual(Polynomial([-6, 4, 0, 4, 0, 0]), self.p1 * self.p3)

    def test_mul_p1_const(self):
        self.assertEqual(Polynomial([9, -6, 0, -6]), self.p1 * 3)

    def test_mul_const_p1(self):
        self.assertEqual(Polynomial([9, -6, 0, -6]), 3 * self.p1)

    def test_mul_type_error(self):
        self.assertRaises(TypeError, self.p1.__mul__, "Hello")

    def test_eq_p1(self):
        self.assertTrue(self.p1 == Polynomial([3, -2, 0, -2]))

    def test_eq_type_error(self):
        self.assertRaises(TypeError, self.p1.__eq__, "Hello")

    def test_ne_p1(self):
        self.assertTrue(self.p1 != self.p2)

    def test_ne_type_error(self):
        self.assertRaises(TypeError, self.p1.__ne__, "Hello")

    def test_lt_p1_p2(self):
        self.assertFalse(self.p1 < self.p2)

    def test_lt_p2_p3(self):
        self.assertFalse(self.p2 < self.p3)

    def test_lt_type_error(self):
        self.assertRaises(TypeError, self.p1.__lt__, "Hello")

    def test_le_p3_p1(self):
        self.assertTrue(self.p3 <= self.p1)

    def test_le_p1(self):
        self.assertTrue(self.p1 <= Polynomial([3, -2, 0, -2]))

    def test_le_type_error(self):
        self.assertRaises(TypeError, self.p1.__le__, "Hello")

    def test_gt_p2_p3(self):
        self.assertTrue(self.p2 > self.p3)

    def test_gt_type_error(self):
        self.assertRaises(TypeError, self.p1.__gt__, "Hello")

    def test_ge_p3_p1(self):
        self.assertFalse(self.p3 >= self.p1)

    def test_ge_type_error(self):
        self.assertRaises(TypeError, self.p1.__ge__, "Hello")


if __name__ == '__main__':
    unittest.main()
