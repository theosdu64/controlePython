from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Livre():
    id_livre : Optional[int] = field(default=None, init=False)
    titre : str
    resume : str
    date_parution : date
    nb_page : int
    isbn : str
    prix : float

    def __str__(self) -> str:
        return (
            f"Livre:\n"
            f"  Titre        : {self.titre}\n"
            f"  Résumé       : {self.resume}\n"
            f"  Date parution: {self.date_parution}\n"
            f"  Nombre pages : {self.nb_page}\n"
            f"  ISBN         : {self.isbn}\n"
            f"  Prix         : {self.prix} €"
        )
