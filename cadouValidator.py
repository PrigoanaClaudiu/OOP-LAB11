from Domain.cadou import Cadou


class CadouValidator():
    def valideaza(self, cadou: Cadou):
        erori = []
        if cadou.idUtilE == '':
            erori.append("Cele 2 id-uri trebuie sa existe.")
        if cadou.idUtilD == '':
            erori.append("Cele 2 id-uri trebuie sa existe.")
        if cadou.idUtilE == cadou.idUtilD:
            erori.append("Cele 2 id-uri trebuei sa fie diferite!")
        m = ['Secret Santa', 'Zi nastere', 'Altele']
        if cadou.tip not in m:
            erori.append("Tipul poate fii doar (“Secret Santa” / ”Zi nastere” / ”Altele”).")
        if erori:
            raise ValueError(erori)
