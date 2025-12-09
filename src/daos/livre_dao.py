# -*- coding: utf-8 -*-

"""
Classe livre
"""
from dataclasses import dataclass
from typing import List

from src.daos import dao
from src.daos.dao import Dao
from src.model.livre import Livre


@dataclass
class LivreDao(Dao[Livre]):

    def read(self, id_livre: int) -> Livre:
        try:
            """
            Recupere titre, resume , date de parution , nb de page, isbn , prix du livre  
            nom et prenom de l'auteur et le nom de l'éditeur
            Select dans livre avec Jointure de personne , auteur et editeur
            """
            with dao.connection.cursor() as cursor:
                sql_livre = """
                    SELECT l.titre, l.resume, l.date_parution, l.nb_page, l.isbn, l.prix,e.nom as editeur_nom ,p.nom as auteur_nom, p.prenom as auteur_prenom
                    FROM livre as l
                    INNER JOIN editeur as e
                    on l.id_editeur = e.id_editeur
                    INNER JOIN auteur as a 
                    on l.id_auteur = a.id_auteur
                    INNER JOIN personne as p 
                    on a.id_auteur = p.id_personne
                    WHERE l.id_livre = %s
                    """
                cursor.execute(sql_livre, id_livre)
                row = cursor.fetchone()

                if row is None:
                    return None

                livre =  Livre(
                    titre=row["titre"],
                    resume=row["resume"],
                    date_parution=row["date_parution"],
                    nb_page=row["nb_page"],
                    isbn=row["isbn"],
                    prix=row["prix"]
                )
                return livre, row["auteur_nom"], row["auteur_prenom"], row["editeur_nom"]

        except Exception as e:
            print("Erreur de la lecture du livre :", e)
            return None

    def read_all(self) -> List[Livre]:
        raise NotImplemented

    def delete(self, id: int) -> bool:
        raise NotImplemented

    def create(self, livre: Livre) -> Livre:
        raise NotImplemented

    def update(self, livre: Livre) -> Livre:
        raise NotImplemented