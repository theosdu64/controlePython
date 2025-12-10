# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from typing import Optional
from dataclasses import dataclass
from src.daos.dao import Dao
from src.model.selection import Selection

@dataclass
class SelectionDao:

    def read(self, numero_tour: int) -> Optional[Selection]:
        try:
            with Dao.connection.cursor() as cursor:
                sql_selection = """
                SELECT s.numero_tour, s.date_selection, s.nb_livre, s.id_selection, s.id_jury
                FROM selection AS s
                WHERE s.numero_tour = %s
                """
                cursor.execute(sql_selection, (numero_tour,))
                row = cursor.fetchone()

                if row is None:
                    return None

                return Selection(
                    id_selection = row["id_selection"],
                    numero_tour=row["numero_tour"],
                    date_selection=row["date_selection"],
                    nb_livre=row["nb_livre"],
                    id_jury=row["id_jury"]
                )

        except Exception as e:
            print(e)
            return None

    def read_all(self) -> Selection:
        raise NotImplemented

    def create(self) -> Selection:
        raise NotImplemented

    def delete(self) -> Selection:
        raise NotImplemented

    def update(self) -> Selection:
        raise NotImplemented