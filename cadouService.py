from Domain.cadou import Cadou
from Domain.cadouValidator import CadouValidator
from Repository.json_repository import JsonRepository


class CadouService:
    def __init__(self, cadouRepository: JsonRepository,
                 cadouValidator: CadouValidator,
                 utilizatorRepository = JsonRepository):
        self.cadouRepository = cadouRepository
        self.cadouValidator = cadouValidator
        self.utilizatorRepository = utilizatorRepository

    def getAll(self):
        """ia toate informatiile legate de toate cadourile"""
        return self.cadouRepository.read()

    def adauga(self, idCadou, idUtilE, idUtilD, denm, tip):
        """
        adauga un nou cadoi
        :param idCadou: str
        :param idUtilE: str
        :param idUtilD: str
        :param denm: str
        :param tip: str (“Secret Santa” / ”Zi nastere” / ”Altele”).
        """
        cadou = Cadou(idCadou, idUtilE, idUtilD, denm, tip)
        self.cadouValidator.valideaza(cadou)
        self.cadouRepository.create(cadou)

    def afsSecretSanta(self):
        rez = []
        for cadou in self.cadouRepository.read():
            if cadou.tip == 'Secret Santa':
                idE = self.utilizatorRepository.read(cadou.idUtilE)
                idD = self.utilizatorRepository.read(cadou.idUtilD)
                rez.append([cadou.denm, idE.nume, idD.nume, idD.adresa])
        return rez