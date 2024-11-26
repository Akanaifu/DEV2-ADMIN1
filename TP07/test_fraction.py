from fraction_Loyd import Fraction


fraction1 = Fraction(1, 4)
fraction2 = Fraction(3, 8)
fraction3 = Fraction(5, 2)

if __name__ == "__main__":
    # Addition
    try:
        addition = fraction1 + fraction2
        print(f"Addition: {addition}")
    except Exception as e:
        print(f"An error occurred during addition: {e}")

    # Subtraction
    try:
        soustraction = fraction1 - fraction2
        print(f"Soustraction: {soustraction}")
    except Exception as e:
        print(f"An error occurred during subtraction: {e}")

    # Multiplication
    try:
        multiplication = fraction1 * fraction2
        print(f"Multiplication: {multiplication}")
    except Exception as e:
        print(f"An error occurred during multiplication: {e}")

    # Division
    try:
        division = fraction1 / fraction2
        print(f"Division: {division}")
    except Exception as e:
        print(f"An error occurred during division: {e}")

    # Power
    try:
        puissance = fraction3**2
        print(f"Puissance: {puissance}")
    except Exception as e:
        print(f"An error occurred during power: {e}")

    # equal
    try:
        equality = fraction1 == fraction2
        print(f"Egalite: {equality}")
    except Exception as e:
        print(f"An error occurred during equality: {e}")
