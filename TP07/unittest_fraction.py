import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_initialisation(self):
        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-6, 8)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(6, -8)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-6, -8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_as_mixed_number(self):
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 1/3")

        f = Fraction(4, 2)
        self.assertEqual(f.as_mixed_number(), "2")

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6))

    def test_subtraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 - f2, Fraction(1, 6))

    def test_multiplication(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 * f2, Fraction(1, 3))

    def test_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 / f2, Fraction(3, 4))

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_power(self):
        f = Fraction(2, 3)
        self.assertEqual(f**2, Fraction(4, 9))
        self.assertEqual(f**-1, Fraction(3, 2))

    def test_equality(self):
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))

    def test_float_conversion(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(1, 5).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(5, 3).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(3, 4).is_proper())
        self.assertFalse(Fraction(4, 3).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 2)
        self.assertFalse(f1.is_adjacent_to(Fraction(5, 6)))
        self.assertTrue(f1.is_adjacent_to(f2))


if __name__ == "__main__":
    unittest.main()
