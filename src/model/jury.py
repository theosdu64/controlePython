# -*- coding: utf-8 -*-

"""
Classe Jury, hérite de Personne
"""
from dataclasses import dataclass, field
from typing import Optional

from src.model.personne import Personne


@dataclass
class Jury(Personne):
    """Membre du jury du prix Goncourt."""
    est_president: bool
    id_jury: Optional[int] = field(default=None, init=False)

    def __str__(self) -> str:
        person_str = super().__str__()
        statut = "est le président" if self.est_president else "n'est pas le président"
        return f"{person_str}, {statut}"