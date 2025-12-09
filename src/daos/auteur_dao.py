import dataclasses
from typing import Optional

from src.daos.dao import Dao
from src.model.auteur import Auteur


@dataclasses
class AuteurDao(Dao[Auteur]):

    def create(self, auteur: Auteur) -> int:
        try:

            with Dao.connection.cursor() as cursor:
                sql_personne = """
                    INSERT INTO personne (nom, prenom)
                    VALUES (%s, %s)
                """

                cursor.execute(sql_personne, (auteur.nom, auteur.prenom))
                id_personne = cursor.lastrowid
                sql_auteur = """
                    INSERT INTO auteur (id_auteur)
                    VALUES (%s)
                """

                cursor.execute(sql_auteur, (id_personne,))
                Dao.connection.commit()
                return id_personne

        except Exception as e:
            print("Erreur lors de la création d'un auteur :", e)
            return 0

    def read(self, id_auteur: int) -> Optional[Auteur]:
        try:
            with Dao.connection.cursor() as cursor:

                sql = """
                    SELECT p.nom, p.prenom
                    FROM auteur AS a
                    INNER JOIN personne AS p
                        ON p.id_personne = a.id_personne
                    WHERE a.id_auteur = %s
                """
                cursor.execute(sql, (id_auteur,))
                row = cursor.fetchone()

                if row is None:
                    return None

                return Auteur(
                    id_auteur=id_auteur,
                    nom=row["nom"],
                    prenom=row["prenom"]
                )

        except Exception as e:
            print("Erreur lors de la lecture d'un auteur :", e)
            return None

    def update(self, id_auteur, obj : Auteur) -> bool:
        raise NotImplemented

    def delete(self, id: int) -> bool:
        raise NotImplemented