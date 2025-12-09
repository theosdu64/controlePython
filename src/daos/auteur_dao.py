# -*- coding: utf-8 -*-

"""
Classe Auteur d'un livre
"""

import dataclasses
from typing import Optional
from dataclasses import dataclass
from src.daos.dao import Dao
from src.model.auteur import Auteur


@dataclass
class AuteurDao(Dao[Auteur]):

    def read(self, id_auteur: int) -> Optional[Auteur]:
        try:
            """
            Recupere nom et prenom de l'auteur
            Jointure entre personne et auteur 
            """
            with Dao.connection.cursor() as cursor:
                sql_personne = """
                    SELECT p.nom, p.prenom
                    FROM auteur AS a
                    INNER JOIN personne AS p
                        ON p.id_personne = a.id_personne
                    WHERE a.id_auteur = %s
                """
                cursor.execute(sql_personne, (id_auteur,))
                row = cursor.fetchone()

                if row is None:
                    return None

                return Auteur(
                    nom=row["nom"],
                    prenom=row["prenom"]
                )

        except Exception as e:
            print("Erreur de la lecture d'un auteur :", e)
            return None

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

    def read_all(self) -> list[Auteur]:
        raise NotImplemented

    def update(self, id_auteur, obj : Auteur) -> bool:
        raise NotImplemented

    def delete(self, id: int) -> bool:
        raise NotImplemented