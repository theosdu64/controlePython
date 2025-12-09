# -*- coding: utf-8 -*-

"""
Classe Personnage d'un livre
"""

from typing import Optional
from dataclasses import dataclass
from src.daos.dao import Dao
from src.model.personnage import Personnage

@dataclass
class PersonnageDao(Dao[Personnage]):

    def read(self, id_personnage: int) -> Optional[Personnage]:
        """recupere le personnage par l'id puis le nom du livre avec l'isbn"""
        try:
            with Dao.connection.cursor() as cursor:
                sql_personnage = """
                    SELECT p.nom, p.isbn_livre 
                    FROM personnage as p 
                    WHERE p.id_personnage = %s
                """
                cursor.execute(sql_personnage, (id_personnage,))
                row = cursor.fetchone()

                if row is None:
                    return None

                return Personnage(
                    nom=row["nom"],
                    isbn_livre=row["isbn_livre"]
                )

        except Exception as e:
            print(f"Erreur de la lecture du personnage : {e}")
            return None

    def read_all(self) -> list[Personnage]:
        raise NotImplemented

    def create(self, personnage: Personnage):
        raise NotImplemented

    def update(self, personnage: Personnage):
        raise NotImplemented

    def delete(self, personnage: Personnage):
        raise NotImplemented

