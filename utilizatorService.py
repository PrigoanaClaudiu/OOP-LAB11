from Domain.utilizator import Utilizator
from Domain.utilizatorValidator import UtilizatorValidator
from Repository.json_repository import JsonRepository


class UtilizatorService:
    def __init__(self, utilizatorRepository: JsonRepository,
                 utilizatorValidator: UtilizatorValidator):
        self.utilizatorRepository = utilizatorRepository
        self.utilizatorValidator = utilizatorValidator

    def getAll(self):
        """ia toate informatiile legate de toti utilizatorii"""
        return self.utilizatorRepository.read()

    def adauga(self, idUtilizator, username, nume, adresa):
        """
        Adauga un nou utilizator in multimea de utilizatori
        :param idUtilizator: id-ul utilizatorului -> str
        :param username: username-ul sau -> str
        :param nume: numele sau -> str
        :param adresa: adresa -> str
        """
        utilizator = Utilizator(idUtilizator, username, nume, adresa)
        self.utilizatorValidator.valideaza(utilizator)
        self.utilizatorRepository.create(utilizator)

    def ordo(self):
        utilizatori = self.utilizatorRepository.read()
        rez = {}
        for utilizator in utilizatori:
            for i in utilizator.adresa:
                if '0' <= i <= '9':
                    rez[utilizator.id_entity] += 1

        rez0 = sorted(rez.keys(), key=lambda nm: rez[nm])
        rez1 = []
        for idu in rez0:
            rez1.append({
                "numele":self.utilizatorRepository.read(idu),
                "nr de cifre": rez[idu]
            })