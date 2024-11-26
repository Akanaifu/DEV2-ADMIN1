import math


class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0 (Denominator cannot be zero)
        POST : The fraction is initialized as num/den, and the fraction is reduced to its simplest form if possible.
        """
        pass

    @property
    def numerator(self):
        """Return the numerator of the fraction.

        PRE : None
        POST : The numerator of the fraction is returned.
        """
        pass

    @property
    def denominator(self):
        """Return the denominator of the fraction.

        PRE : None
        POST : The denominator of the fraction is returned.
        """
        pass

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE : None
        POST : A string representation of the fraction, in the form 'numerator/denominator'.
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE : None
        POST : A string representation of the mixed number in the form 'integer part (numerator/denominator)'.
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object that is the sum of the two fractions.
        """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object that is the difference of the two fractions.
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object that is the product of the two fractions.
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE : other is an instance of Fraction and other != 0.
        POST : Returns a new Fraction object that is the quotient of the two fractions.
        """
        pass

    def __pow__(self, exponent):
        """Overloading of the ** operator for fractions
        PRE : exponent is an instance of Fraction
        POST : Returns a new Fraction object that is the result of the exponentiation of the fraction.
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions.

        PRE : other is an instance of Fraction.
        POST : Returns True if the two fractions are equal, False otherwise.
        """
        pass

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRE : None
        POST : Returns a float value representing the fraction.
        """
        pass

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.

        PRE : None
        POST : Returns True if the fraction is equal to 0, False otherwise.
        """
        pass

    def is_integer(self):
        """Check if a fraction is an integer.

        PRE : None
        POST : Returns True if the fraction is an integer, False otherwise.
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE : None
        POST : Returns True if the absolute value of the fraction is less than 1, False otherwise.
        """
        pass

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE : None
        POST : Returns True if the fraction is a unit fraction (numerator = 1), False otherwise.
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        PRE : other is an instance of Fraction.
        POST : Returns True if the difference between the fractions is a unit fraction, False otherwise.
        """
        pass
