class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None


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

                    class VoitureService:
                        def __init__(self, marque, modele, matricule):
                            self.marque = marque
                            self.modele = modele
                            self.matricule = matricule
                            self.employe = None

                        def afficherInformations(self):
                            print("Marque:", self.marque)
                            print("Modele:", self.modele)
                            print("Matricule:", self.matricule)
                            if self.employe:
                                print("Employe:", self.employe.nom, self.employe.prenom)
                            else:
                                print("Aucun employe")

                                emp1 = Employe("P12345", "Dupont", "Jean")
                                emp2 = Employe("P67890", "Martin", "Sophie")

                                v1 = VoitureService("Toyota", "Corolla", "ABC123")
                                v2 = VoitureService("Honda", "Civic", "XYZ789")

                                emp1.affecterVoiture(v1)
                                emp2.affecterVoiture(v2)

                                print("=== Informations Employes ===")
                                emp1.afficherInformations()
                                print()
                                emp2.afficherInformations()

                                print("\n=== Informations Voitures ===")
                                v1.afficherInformations()
                                print()
                                v2.afficherInformations()

