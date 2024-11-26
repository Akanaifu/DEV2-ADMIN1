import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
        - num et den sont des entiers
        - den !=0, il est non null

        POST : retourne la fraction à son état simple et sous forme irreductible :
        - Le numérateur et le dénominateur sont divisés par leur plus grand commun diviseur (GCD).
        - Le dénominateur est toujours positif.
        """

        if den == 0:
            raise ValueError("The denomnator can't be zero")
        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :
        - num et den doivent être des nombres entiers
        - den != 0

        POST : retourne la fraction sous cette forme : "num/den" où "num" est le numérateur et "den" est le dénominateur
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
        - num et den doivent être des entiers.
        - den != 0.

        POST : Retourne la fraction sous forme de nombre mixte :
        - Si la fraction est un entier, retourne l'entier comme un nombre entier.
        - Si la fraction n'est pas un entier, retourne une représentation sous forme de
        nombre mixte, c'est-à-dire un entier suivi du reste sous forme de fraction.
        """

        fraction_entier = (
            self.num // self.den
        )  # pour voir un chiffre en entier sans forcément décimale
        le_reste = self.num % self.den
        if le_reste == 0:  # donc si c'est un entier
            return fraction_entier
        else:
            return f"{le_reste} {fraction_entier}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE :
        - num et den doivent être des entiers
        - den ! = 0
        POST : Retourne une fraction qui est le resultat d'une addition entre fraction
        """
        try:
            if not isinstance(other, Fraction):
                raise TypeError(
                    "ça doit être une fraction "
                )  # on vérifie si other est un descendant / une instance de Fraction
            add_numerator = self.num * other.den + self.den * other.num
            add_denominator = self.den * other.den
            return Fraction(add_numerator, add_denominator)
        except TypeError as e:
            print(f"Erreur : {e}")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE :
        - num et den doivent être des entiers
        - den ! = 0
        POST : Retourne une fraction qui est le résultat d'une soustraction entre fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Ce n'est pas une instnace de la classe Fraction ")
        sub_numerator = self.num * other.den - self.den * other.num
        sub_denominator = self.den * other.den
        resultat = Fraction(sub_numerator, sub_denominator)
        return resultat

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
        - num et den doivent être des entiers
        - den != 0
        POST : Retourne une fraction qui est le resultat d'une multiplication entre fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        mul_numerator = self.num * other.num
        mul_denominator = self.den * other.den
        resultat = Fraction(mul_numerator, mul_denominator)
        return resultat

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
        - num et den doivent être des entiers
        - den != 0
        POST : Retourne une fraction qui est le resultat d'une division entre fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        truediv_numerator = self.num * other.den
        truediv_denominator = self.den * other.num
        resultat = Fraction(truediv_numerator, truediv_denominator)
        return resultat

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : "other" doit être un entier (exposant)
        POST : Retourne une fraction qui est le resultat de la puissance entre fraction de l'exposant "other".
        """
        try:
            if not isinstance(other, int):
                raise TypeError("L'exposant doit être un entier")
            new_num = self.num**other
            new_den = self.den**other
            return Fraction(new_num, new_den)
        except TypeError as e:
            print(f"Erreur : {e}")

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : "other" doit être une une instance de la clzsse Fraction
        POST : Retourne True si les fractions son égale, si ce n'est pas le cas ça retourne False

        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "Les objets doivent être des instances de la classe Fraction"
            )
        return self.num == other.num and self.den == other.den

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
        - num et den doivent être des entiers
        - den != 0
        POST :
        Retourne la valeur decimale de la fractions sous forme de nombre flottant
        """
        return self.num / self.den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """
        PRE : - num et den sont des entiers
               - den != 0
        POST : - Retourne True si la fraction est égale à zéro, sinon retourne False.
        """
        return self.num == 0  # si le num est égale à 0 alors la fraction vaut 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE :
        - num et den sont des entiers
        - den != 0
        POST : Retourne True si la fraction est un entier, sinon ça retourne False.
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :
        - num et den sont des entiers
        - den != 0
        POST : Retourne True si la valeur absolue de la fraction est inférieur à 1, sinon ça retourne False
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :
        - num et den sont des entiers
        - den != 0
        POST : - Retourne True si le numérateur est 1 dans la forme réduite de la fraction, sinon retourne False.
        """
        return self.num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE :
        - others doit etre une instance de la classe Fraction
        - den != 0

        POST : Retourne True si la fraction est adjacente, sinon ça renvoie False
        """
        diff_num = abs(self.num * other.den - other.num * self.den)
        return diff_num == 1
