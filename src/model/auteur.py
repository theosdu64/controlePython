# -*- coding: utf-8 -*-

"""
Classe Auteur, hérite de Personne
"""
from dataclasses import dataclass, field
from typing import Optional

from .personne import Personne

@dataclass
class Auteur(Personne):
    id_auteur : Optional[int] = field(default=None, init=False)

    """Auteur d'un livre."""
    def __str__(self) -> str:
        return f"Auteur: {super().__str__()} "