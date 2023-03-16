from Service.cadouService import CadouService
from Service.utilizatorService import UtilizatorService


class Console:
    def __init__(self, utilizatorService: UtilizatorService,
                 cadouService: CadouService):
        self.utilizatorService = utilizatorService
        self.cadouService = cadouService

    def runMenu(self):
        while True:
            print("1. Adauga un utilizator.")
            print("2. Adauga un cadou.")
            print("3. Afișarea numelor utilizatorilor "
                  "ordonate crescător după numărul de "
                  "cifre din adresă.")

            print("4. Afișarea tuturor cadourilor cu tipul “Secret Santa” ")

            print("a1. Afiseaza toti utilizatorii.")
            print("b1. Afiseaza toti utilizatorii.")

            print("x. Iesire.")

            optiune = input("Dati optiunea: ")

            if optiune == '1':
                self.uiAdaugaUtilizator()
                self.afiseaza(self.utilizatorService.getAll())
            elif optiune == '2':
                self.uiAdaugaCadou()
                self.afiseaza(self.cadouService.getAll())
            elif optiune == '3':
                self.uiOrdo()
            elif optiune == '4':
                self.uiafsSecretSanta()
            elif optiune == 'a1':
                self.afiseaza(self.utilizatorService.getAll())
            elif optiune == 'b1':
                self.afiseaza(self.cadouService.getAll())
            elif optiune == 'x':
                break
            else:
                print("Optiune invalida!")

    def uiAdaugaUtilizator(self):
        try:
            idUtilizator = input("Dati id-ul utilizatorului: ")
            username = input("Dati username-ul: ")
            nume = input("Dati numele: ")
            adresa = input("Dati adresa: ")

            self.utilizatorService.adauga(idUtilizator, username, nume,
                                          adresa)
        except Exception as e:
            print(e)

    def afiseaza(self, listaEntitati):
        for entitate in listaEntitati:
            print(entitate)

    def uiAdaugaCadou(self):
        try:
            k=1
            idCadou = input("Dati id-ul cadoului: ")
            idUtilE = input("Dati id-ul utilizatorului expedietor: ")
            idUtilD = input("Dati id-ul utilizatorului destinatar: ")
            denm = input("Dati denumirea cadoului: ")
            tip = input("Dati tipul (“Secret Santa” / "
                        "”Zi nastere” / ”Altele”): ")
            for cadou in self.cadouService.getAll():
                if idUtilD == cadou.idUtilD and cadou.tip == 'Secret Santa':
                    k = 0
            if k == 1:
                self.cadouService.adauga(idCadou, idUtilE, idUtilD, denm, tip)
            else:
                print("Un utilizator poate primi un singur Secret Santa.")
        except Exception as e:
            print(e)

    def uiOrdo(self):
        for util in self.utilizatorService.ordo():
            print(util)

    def uiafsSecretSanta(self):
        for cad in self.cadouService.afsSecretSanta():
            print(cad)
