from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Cadou(Entity):
    """
    creeaza un cadou
    id ->unic
    idUtilE -> str
    idUtilD -> str
    denm -> str
    tip -> str (“Secret Santa” / ”Zi nastere” / ”Altele”).
    """
    idUtilE: str
    idUtilD: str
    denm: str
    tip: str