from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Utilizator(Entity):
    """
    creeaza un utilizator
    id -> unic
    username -> str
    nume -> str
    adresa -> str
    """
    username: str
    nume: str
    adresa: str
