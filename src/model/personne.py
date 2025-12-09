# -*- coding: utf-8 -*-

"""
Classe abstraite Personne, mère de Jury et Student
"""

from dataclasses import dataclass, field
from abc import ABC

@dataclass
class Personne(ABC):
    """Personne liée aux prix goncourt : Jury et Auteur."""
    id_personne: int
    nom: str
    prenom: str

    def __str__(self) -> str:
        return f"{self.nom} , {self.prenom}"
