from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from src.daos.dao import Dao
from src.model.editeur import Editeur

@dataclass
class EditeurDao(Dao[Editeur]):

    def read(self, id_entity: int) -> Optional[Editeur]:
        with Dao.connection.cursor() as cursor:
            sql = "SELECT nom FROM editeur WHERE id_editeur = %s"
            cursor.execute(sql, (id_entity,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Editeur(
                nom=row["nom"]
            )

    def read_all(self) -> List[Editeur]:
        raise NotImplemented

    def create(self, editeur: Editeur) -> None:
        raise NotImplemented

    def update(self, editeur: Editeur) -> None:
        raise NotImplemented

    def delete(self, id_entity: int) -> None:
        raise NotImplemented