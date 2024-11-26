import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_initialisation(self):
        fraction = Fraction(4, 6)
        self.assertEqual(fraction.numerator, 2)
        self.assertEqual(fraction.denominator, 3)

        fraction_negative = Fraction(-4, 6)
        self.assertEqual(fraction_negative.numerator, -2)
        self.assertEqual(fraction_negative.denominator, 3)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_addition(self):
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(1, 6)
        resultat = fraction1 + fraction2
        self.assertEqual(resultat, Fraction(1, 2))

    def test_soustraction(self):
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(1, 3)
        resultat = fraction1 - fraction2
        self.assertEqual(resultat, Fraction(1, 6))

    def test_multiplication(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(3, 4)
        resultat = fraction1 * fraction2
        self.assertEqual(resultat, Fraction(1, 2))

    def test_division(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(2, 5)
        resultat = fraction1 / fraction2
        self.assertEqual(resultat, Fraction(15, 8))

        with self.assertRaises(ZeroDivisionError):
            fraction1 / Fraction(0, 1)

    def test_str(self):
        fraction = Fraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

    def test_equality(self):
        self.assertEqual(Fraction(2, 4), Fraction(1, 2))
        self.assertNotEqual(Fraction(2, 3), Fraction(1, 3))


if __name__ == "__main__":
    unittest.main()
