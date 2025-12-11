from dataclasses import dataclass, field
from typing import Optional

@dataclass
class JuryTable:
    id_jury: Optional[int] = None
    annee: Optional[int] = None

    def __str__(self):
        return f"JuryTable(id_jury={self.id_jury}, annee={self.annee})"
