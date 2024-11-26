import math


class Fraction:
    """Class representing a fraction and operations on it.

    This class allows the creation and manipulation of fractions. It supports basic arithmetic
    operations, comparison, and properties such as checking if the fraction is proper or a unit fraction.

    Author: V. Van den Schrieck
    Date: October 2021
    """

    def __init__(self, num=0, den=1):
        """Initialize a fraction with a numerator and denominator.

        PRE : den != 0
        POST : The fraction is reduced to its simplest form, and the denominator is always positive.
        RAISE : ValueError if den == 0
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd
        if self.den < 0:  # Ensure the denominator is always positive
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self):
        """Return the numerator of the fraction.

        PRE : None
        POST : Returns the numerator as an integer.
        """
        return self.num

    @property
    def denominator(self):
        """Return the denominator of the fraction.

        PRE : None
        POST : Returns the denominator as a positive integer.
        """
        return self.den

    def __str__(self):
        """Return a textual representation of the fraction.

        PRE : None
        POST : Returns a string in the format 'numerator/denominator'.
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """Return a mixed number representation of the fraction.

        PRE : None
        POST : Returns a string in the format 'integer part numerator/denominator', or just 'integer part' if applicable.
        """
        whole_part = self.num // self.den
        remainder = abs(self.num % self.den)
        if remainder == 0:
            return f"{whole_part}"
        else:
            return f"{whole_part} {remainder}/{self.den}"

    def __add__(self, other):
        """Add two fractions.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object representing the sum.
        RAISE : TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Subtract one fraction from another.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object representing the difference.
        RAISE : TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Multiply two fractions.

        PRE : other is an instance of Fraction.
        POST : Returns a new Fraction object representing the product.
        RAISE : TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Divide one fraction by another.

        PRE : other is an instance of Fraction and other != 0.
        POST : Returns a new Fraction object representing the quotient.
        RAISE : TypeError if other is not a Fraction.
                ZeroDivisionError if other.num == 0.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __pow__(self, exponent):
        """Raise a fraction to an integer power.

        PRE : exponent is an integer.
        POST : Returns a new Fraction object representing the result of exponentiation.
        RAISE : ZeroDivisionError if raising to a negative power and the numerator is zero.
        """
        if exponent == 0:
            return Fraction(1, 1)  # Any value raised to the power 0 is 1
        elif exponent > 0:
            new_num = self.num**exponent
            new_den = self.den**exponent
        else:  # Negative exponent
            if self.num == 0:
                raise ZeroDivisionError("Cannot raise zero to a negative power.")
            new_num = self.den ** abs(exponent)
            new_den = self.num ** abs(exponent)
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        """Check equality of two fractions.

        PRE : other is an instance of Fraction.
        POST : Returns True if the fractions are equal, False otherwise.
        RAISE : TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        return self.num == other.num and self.den == other.den

    def __abs__(self):
        """Return the absolute value of the fraction.

        PRE : None
        POST : Returns a new Fraction object with positive numerator and denominator.
        """
        return Fraction(abs(self.num), abs(self.den))

    def __float__(self):
        """Convert the fraction to a floating-point number.

        PRE : None
        POST : Returns a float representing the decimal value of the fraction.
        """
        return self.num / self.den

    def is_zero(self):
        """Check if the fraction is zero.

        PRE : None
        POST : Returns True if the fraction is 0, False otherwise.
        """
        return self.num == 0

    def is_integer(self):
        """Check if the fraction is an integer.

        PRE : None
        POST : Returns True if the fraction has no remainder, False otherwise.
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the fraction is proper (absolute value less than 1).

        PRE : None
        POST : Returns True if the absolute value of the fraction is less than 1, False otherwise.
        """
        return abs(self.num) < self.den

    def is_unit(self):
        """Check if the fraction is a unit fraction (numerator = 1).

        PRE : None
        POST : Returns True if the numerator is 1, False otherwise.
        """
        return self.num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        PRE : other is an instance of Fraction.
        POST : Returns True if the difference is a unit fraction, False otherwise.
        RAISE : TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        return abs(self - other) == Fraction(1, self.den * other.den)
