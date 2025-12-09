# -*- coding: utf-8 -*-

"""
Classe abstraite Personne, mère de Jury et Student
"""

from dataclasses import dataclass, field
from abc import ABC
from typing import Optional


@dataclass
class Personne(ABC):
    """Personne liée aux prix goncourt : Jury et Auteur."""
    id_personne: Optional[int] = field(default=None, init=False)
    nom: str
    prenom: str

    def __str__(self) -> str:
        return f"{self.nom} , {self.prenom}"
