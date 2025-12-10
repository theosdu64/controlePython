# -*- coding: utf-8 -*-

"""
Classe Vote
"""
from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Vote:
    id_vote : Optional[int]
    date_vote: date
    nb_voix : int
    id_selection : Optional[int]
    id_livre : Optional[int]

    def __str__(self) -> str:
        return (
            "Vote:\n"
            f"  ID vote        : {self.id_vote}\n"
            f"  Date du vote   : {self.date_vote}\n"
            f"  Nombre de voix : {self.nb_voix}\n"
            f"  ID sélection   : {self.id_selection}\n"
            f"  ID livre       : {self.id_livre}\n"
        )
