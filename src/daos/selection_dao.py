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

    def read_all_by_year(self, year: int) -> list[Selection]:
        try:
            with Dao.connection.cursor() as cursor:
                sql_selection = """
                SELECT * FROM selection WHERE YEAR(date_selection) = %s;
                """
                cursor.execute(sql_selection, (year,))
                rows = cursor.fetchall()

                selections = []
                for row in rows:
                    selection = Selection(
                        id_selection=row['id_selection'],
                        numero_tour=row['numero_tour'],
                        date_selection=row['date_selection'],
                        nb_livre=row['nb_livre'],
                        id_jury=row.get('id_jury')
                    )
                    selections.append(selection)
                return selections

        except Exception as e:
            print(f"Erreur read_all_by_year: {e}")
            return []

    def read_all(self) -> Selection:
        raise NotImplemented

    def create(self, selection: Selection) -> Optional[Selection]:
        try:
            with Dao.connection.cursor() as cursor:
                sql_selection = """
                    INSERT INTO selection (id_selection,numero_tour, date_selection, nb_livre, id_jury)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql_selection, (
                    selection.id_selection,
                    selection.numero_tour,
                    selection.date_selection,
                    selection.nb_livre,
                    selection.id_jury
                ))
                id_selection = cursor.lastrowid
                Dao.connection.commit()

                selection.id_selection = id_selection
                return selection

        except Exception as e:
            print(f"Erreur lors de la création de la sélection : {e}")
            Dao.connection.rollback()
            return None

    def delete(self) -> Selection:
        raise NotImplemented

    def update(self) -> Selection:
        raise NotImplemented

    def updates_of_qualifiers(self, id_livre, id_selection):
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO fait_partie_de (id_livre, id_selection)
                    VALUES (%s, %s)
                """
                cursor.execute(sql, (id_livre, id_selection))
                Dao.connection.commit()

                return (id_livre, id_selection)

        except Exception as e:
            print(f"Erreur lors de l'insertion dans fait_partie_de (selection_dao) : {e}")
            Dao.connection.rollback()
            return None
