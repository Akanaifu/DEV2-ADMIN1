"""
Chaque animal possede exactement 1 tete et 1 corps (composition). Il peut avoir plusieurs membres. Les membres appartiennent à un seul animal.

Habitat: Chaque animal habite exactement dans 1 habitat (agrégation). Un habitat peut être partagé par au moins 1 animal.

Héritage: Les especes (comme Lapin, Mouton) sont des sous-classes de la classe mere Animal.
"""


class Tete:
    def __init__(self):
        self.description = "Tete d'animal"

    def affiche_info(self):
        print(f"Description de la tete : {self.description}")


class Corps:
    def __init__(self):
        self.description = "Corps d'animal"

    def affiche_info(self):
        print(f"Description du corps : {self.description}")


class Membre:
    def __init__(self, nom):
        self.nom = nom

    def affiche_info(self):
        print(f"Membre : {self.nom}")


class Habitat:
    def __init__(self, nom):
        self.nom = nom

    def affiche_infos(self):
        return {"habitat": self.nom}


class Animal:
    def __init__(self, regime, habitat: Habitat):
        self.regime = regime  # Herbivore ou Carnivore
        self.habitat = habitat  # L'habitat de l'animal
        self.tete = Tete()
        self.corp = Corps()
        self.membres: list[Membre] = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def affiche_info(self):
        print(f"Animal de regime {self.regime} dans l'habitat {self.habitat.nom}")
        self.tete.affiche_info()
        self.corp.affiche_info()
        print("Membres de l'animal :")
        for membre in self.membres:
            membre.affiche_info()


class Lapin(Animal):
    def __init__(self, habitat):
        super().__init__(regime="Herbivore", habitat=habitat)


class Mouton(Animal):
    def __init__(self, habitat):
        super().__init__(regime="Herbivore", habitat=habitat)


# Exemple d'utilisation
if __name__ == "__main__":
    prairie = Habitat("Prairie")

    # Création d'un Lapin
    lapin = Lapin(habitat=prairie)
    lapin.ajouter_membre(Membre("Patte avant gauche"))
    lapin.ajouter_membre(Membre("Patte avant droite"))
    lapin.ajouter_membre(Membre("Patte arriere gauche"))
    lapin.ajouter_membre(Membre("Patte arriere droite"))

    # Affichage des informations du lapin
    print("Informations sur le Lapin :")
    lapin.affiche_info()

    # Création d'un Mouton
    mouton = Mouton(habitat=prairie)
    mouton.ajouter_membre(Membre("Patte 1"))
    mouton.ajouter_membre(Membre("Patte 2"))
    mouton.ajouter_membre(Membre("Patte 3"))
    mouton.ajouter_membre(Membre("Patte 4"))

    print("\nInformations sur le Mouton :")
    mouton.affiche_info()
