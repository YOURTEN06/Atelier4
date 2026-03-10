class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None
        Set - Content.\atelier4.py @ "

        class Employe:
            def __init__(self, numeroPermis, nom, prenom):
                self.numeroPermis = numeroPermis
                self.nom = nom
                self.prenom = prenom
                self.voitureService = None

            def afficherInformations(self):
                print("Permis:", self.numeroPermis)
                print("Nom:", self.nom)
                print("Prenom:", self.prenom)
                if self.voitureService:
                    print("Voiture:", self.voitureService.marque, self.voitureService.modele)
                else:
                    print("Aucune voiture")

            def affecterVoiture(self, voiture):
                if self.voitureService is None:
                    self.voitureService = voiture
                    voiture.employe = self

            def retirerVoiture(self):
                if self.voitureService:
                    self.voitureService.employe = None
                    self.voitureService = None

