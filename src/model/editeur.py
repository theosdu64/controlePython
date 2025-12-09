# -*- coding: utf-8 -*-

"""
Classe Editeur
"""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Editeur():
    id_editeur: Optional[int] = field(default=None, init=False)
    nom : str

    def __str__(self) -> str:
        return f"{self.nom}"