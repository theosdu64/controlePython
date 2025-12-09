# -*- coding: utf-8 -*-

"""
Classe Personnage
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Personnage():
    id_personnage: Optional[int] = field(default=None, init=False)
    nom : str
    isbn_livre : str

    def __str__(self) -> str:
        return f"nom : {self.nom} isbn : {self.isbn_livre}"