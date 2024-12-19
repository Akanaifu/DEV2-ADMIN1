"""
Class classe:

Les classes Élève et Professeur héritent de la classe mère Personne, qui centralise les informations communes.

Chaque Classe possède un professeur et entre 1 et 30 élèves. Ces éléments sont gérés directement dans la classe Classe.

Les Coordonnees (adresse et téléphone) sont uniques à chaque personne et ne peuvent pas exister indépendamment d’elle. Cette relation est une composition entre Personne et Coordonnees.
"""


class Coordonnees:
    def __init__(self, adresse: str, telephone: str):
        self.adresse = adresse
        self.telephone = telephone

    def __str__(self):
        return f"Adresse: {self.adresse}, Téléphone: {self.telephone}"


class Personne:
    def __init__(self, etat_civil: str, coordonnees: Coordonnees):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

    def __str__(self):
        return f"{self.__class__}: Etat civil: {self.etat_civil}, Coordonnées: {self.coordonnees}"


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
            print("La classe est complète (30 élèves maximum).")

    def afficher_classe(self):
        print(f"Professeur: {self.professeur}")
        print("Élèves:")
        for eleve in self.eleves:
            print(eleve)


# Exemple d'utilisation
if __name__ == "__main__":
    # Création des coordonnées
    coord_prof = Coordonnees("Rue des Professeurs, 123", "0123456789")
    coord_eleve1 = Coordonnees("Avenue des Élèves, 456", "0987654321")
    coord_eleve2 = Coordonnees("Boulevard des Étudiants, 789", "0678943210")

    # Création des personnes
    professeur = Professeur("Ms. Alice", coord_prof)
    eleve1 = Eleve("Bob Martin", coord_eleve1)
    eleve2 = Eleve("Tata Durand", coord_eleve2)

    # Création d'une classe
    ma_classe = Classe(professeur)

    # Ajout d'élèves
    ma_classe.ajouter_eleve(eleve1)
    ma_classe.ajouter_eleve(eleve2)

    # Affichage des informations de la classe
    print("Informations de la Classe :")
    ma_classe.afficher_classe()
