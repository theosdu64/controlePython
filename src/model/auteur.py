# -*- coding: utf-8 -*-

"""
Classe Auteur, hérite de Personne
"""
from dataclasses import dataclass
from .personne import Personne

@dataclass
class AuteurPersonne(Personne):
    """Auteur d'un livre."""
    def __str__(self) -> str:
        return f"Auteur: {super().__str__()} "