from Domain import utilizator


class UtilizatorValidator:
    def valideaza(self, util: utilizator):
        erori = []
        if util.username == '':
            erori.append("Username-ul trebuie sa existe.")
        if util.nume == '':
            erori.append("Numele trebuie sa existe.")
        if util.adresa == '':
            erori.append("Adresa trebuie sa existe.")
        if erori:
            raise ValueError(erori)
