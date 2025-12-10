from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Selection():
    id_selection: Optional[int]
    numero_tour : int
    date_selection : date
    nb_livre : int
    id_jury : Optional[int]

    def __str__(self) -> str:
        return (
            f"Selection:\n"
            f"  numero tour        : {self.numero_tour}\n"
            f"  date de selection       : {self.date_selection}\n"
            f"  nb_livre: {self.nb_livre}\n"
        )