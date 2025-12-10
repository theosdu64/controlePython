from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Selection():
    id_selection: Optional[int] = field(init=False, default=None)
    numero_tour : int
    date_selection : date
    nb_livre : int

    def __str__(self) -> str:
        return (
            f"Selection:\n"
            f"  numero tour        : {self.numero_tour}\n"
            f"  date de selection       : {self.date_selection}\n"
            f"  nb_livre: {self.nb_livre}\n"
        )