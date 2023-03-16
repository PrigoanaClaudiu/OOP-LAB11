from Domain.cadouValidator import CadouValidator
from Domain.utilizatorValidator import UtilizatorValidator
from Repository.json_repository import JsonRepository
from Service.cadouService import CadouService
from Service.utilizatorService import UtilizatorService
from UserInterface.console import Console


def main():
    utilizatorRepository = JsonRepository("utilizator.json")
    utilizatorValidator = UtilizatorValidator()

    cadouRepository = JsonRepository("cadou.json")
    cadouValidator = CadouValidator()

    utilizatorService = UtilizatorService(utilizatorRepository, utilizatorValidator)
    cadouService = CadouService(cadouRepository, cadouValidator)

    console = Console(utilizatorService, cadouService)
    console.runMenu()


if __name__ == '__main__':
    main()
