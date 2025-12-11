from dataclasses import dataclass
from typing import Optional, List
from src.daos.dao import Dao
from src.model.vote import Vote
from datetime import date

@dataclass
class VoteDao(Dao[Vote]):

    def read(self, id_selection: int) -> list[tuple[Vote, str]] | None:
        """
        Récupère tous les votes d'une sélection avec le titre du livre.
        Retourne une liste de tuples : (Vote, titre_du_livre)
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql_vote = """
                SELECT v.id_vote, v.date_vote, v.nb_voix, v.id_selection,
                       l.id_livre, l.titre AS titre_du_livre
                FROM vote AS v
                INNER JOIN livre AS l
                    ON v.id_livre = l.id_livre
                WHERE v.id_selection = %s
                """
                cursor.execute(sql_vote, (id_selection,))
                rows = cursor.fetchall()

                if not rows:
                    return None

                result = []
                for row in rows:
                    vote = Vote(
                        id_vote=row["id_vote"],
                        date_vote=row["date_vote"],
                        nb_voix=row["nb_voix"],
                        id_selection=row["id_selection"],
                        id_livre=row["id_livre"]
                    )

                    result.append((vote, row["titre_du_livre"]))

                return result

        except Exception as e:
            print("Erreur VoteDao.read :", e)
            return None

    def read_all(self) -> List[Vote]:
        raise NotImplemented

    def create(self, id_selection: int, id_livre: int,nb_voix : int ) -> Optional[Vote]:
        """Créer un vote pour une sélection et un livre"""
        try:
            with Dao.connection.cursor() as cursor:
                sql_vote = """
                    INSERT INTO vote (date_vote, nb_voix, id_selection, id_livre)
                    VALUES (%s, %s, %s, %s)
                """

                today = date.today()

                cursor.execute(sql_vote, (today, nb_voix, id_selection, id_livre))
                id_vote = cursor.lastrowid
                Dao.connection.commit()

                return Vote(
                    id_vote=id_vote,
                    date_vote=today,
                    nb_voix=nb_voix,
                    id_selection=id_selection,
                    id_livre=id_livre
                )

        except Exception as e:
            print("Erreur Vote Create :", e)
            return None

    def update(self, id_vote: int, vote: Vote):
        raise NotImplemented

    def delete(self, id_vote: int):
        raise NotImplemented
