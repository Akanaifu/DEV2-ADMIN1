"""
Class classe:

Les classes eleve et Professeur heritent de la classe mere Personne, qui centralise les informations communes.

Chaque Classe possede un professeur et entre 1 et 30 eleves. Ces elements sont geres directement dans la classe Classe.

Les Coordonnees (adresse et telephone) sont uniques à chaque personne et ne peuvent pas exister independamment d’elle. Cette relation est une composition entre Personne et Coordonnees.
"""


class Coordonnees:
    def __init__(self, adresse: str, telephone: str):
        self.adresse = adresse
        self.telephone = telephone

    def __str__(self):
        return f"Adresse: {self.adresse}, Telephone: {self.telephone}"


class Personne:
    def __init__(self, etat_civil: str, coordonnees: Coordonnees):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

    def __str__(self):
        return f"{self.__class__}: Etat civil: {self.etat_civil}, Coordonnees: {self.coordonnees}"


class Eleve(Personne):
    def __init__(self, etat_civil: str, coordonnees: Coordonnees):
        super().__init__(etat_civil, coordonnees)


class Professeur(Personne):
    def __init__(self, etat_civil: str, coordonnees: Coordonnees):
        super().__init__(etat_civil, coordonnees)


class Classe:
    def __init__(self, professeur: Professeur):
        self.professeur = professeur
        self.eleves = []

    def ajouter_eleve(self, eleve: Eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            print("La classe est complete (30 eleves maximum).")

    def afficher_classe(self):
        print(f"Professeur: {self.professeur}")
        print("eleves:")
        for eleve in self.eleves:
            print(eleve)


# Exemple d'utilisation
if __name__ == "__main__":
    # Creation des coordonnees
    coord_prof = Coordonnees("Rue des Professeurs, 123", "0123456789")
    coord_eleve1 = Coordonnees("Avenue des eleves, 456", "0987654321")
    coord_eleve2 = Coordonnees("Boulevard des etudiants, 789", "0678943210")

    # Creation des personnes
    professeur = Professeur("Ms. Alice", coord_prof)
    eleve1 = Eleve("Bob Martin", coord_eleve1)
    eleve2 = Eleve("Tata Durand", coord_eleve2)

    # Creation d'une classe
    ma_classe = Classe(professeur)

    # Ajout d'eleves
    ma_classe.ajouter_eleve(eleve1)
    ma_classe.ajouter_eleve(eleve2)

    # Affichage des informations de la classe
    print("Informations de la Classe :")
    ma_classe.afficher_classe()
