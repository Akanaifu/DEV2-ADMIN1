class FichierJoint:
    def __init__(self, nom, taille, chemin):
        self.nom = nom
        self.taille = taille
        self.chemin = chemin


class Email:
    def __init__(self, expediteur, destination, objet="", texte=""):
        self.objet = objet
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier_joint(self, fichier: FichierJoint):
        self.fichiers_joints.append(fichier)


if __name__ == "__main__":
    email = Email(
        "alice@example.com", "bob@example.com", "Projet", "Bonjour, voici le projet."
    )
    email.ajouter_fichier_joint(FichierJoint("document.pdf", 1024, "dev2/tp5"))

    print(f"De: {email.expediteur}, À: {email.destination}")
    print(f"Titre: {email.objet}, Texte: {email.texte}")
    print("Fichiers joints:")
    for f in email.fichiers_joints:
        print(f"  - {f.nom}, {f.taille} octets")
