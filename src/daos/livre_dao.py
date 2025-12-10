# -*- coding: utf-8 -*-

"""
Classe livre
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any
from src.daos.dao import Dao
from src.daos.personnage_dao import Personnage
from src.model.livre import Livre


@dataclass
class LivreDao(Dao[Livre]):

    def read(self, id_livre: int) -> Optional[Dict[str, Any]]:
        """
        Récupere un livre avec auteur, éditeur
        Retourne un dict avec: livre, auteur_nom, auteur_prenom, editeur_nom
        """
        try:
            with Dao.connection.cursor() as cursor:
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
                cursor.execute(sql_livre, (id_livre,))
                row = cursor.fetchone()

                if row is None:
                    return None

                livre = Livre(
                    titre=row["titre"],
                    resume=row["resume"],
                    date_parution=row["date_parution"],
                    nb_page=row["nb_page"],
                    isbn=row["isbn"],
                    prix=row["prix"]
                )
                livre.id_livre = id_livre

                return {
                    "livre": livre,
                    "auteur_nom": row["auteur_nom"],
                    "auteur_prenom": row["auteur_prenom"],
                    "editeur_nom": row["editeur_nom"]
                }

        except Exception as e:
            print("Erreur de la lecture du livre :", e)
            return None

    def read_all_by_selection(self, id_selection: int) -> list[Livre]:
        """Récupère tous les livres d'une sélection"""
        try:
            with Dao.connection.cursor() as cursor:
                sql_livre = """
                    SELECT l.titre, l.resume, l.date_parution, l.nb_page, l.isbn, l.prix
                    FROM livre as l 
                    INNER JOIN fait_partie_de as f
                        ON l.id_livre = f.id_livre
                    WHERE f.id_selection = %s
                """
                cursor.execute(sql_livre, (id_selection,))
                rows = cursor.fetchall()

                livres = []
                for row in rows:
                    livre = Livre(
                        titre=row["titre"],
                        resume=row["resume"],
                        date_parution=row["date_parution"],
                        nb_page=row["nb_page"],
                        isbn=row["isbn"],
                        prix=row["prix"]
                    )
                    livres.append(livre)

                return livres

        except Exception as e:
            print(f"Erreur lors de la lecture des livres : {e}")
            import traceback
            traceback.print_exc()
            return []


    def read_all(self) -> list[Livre]:
        raise NotImplementedError

    def delete(self, id: int) -> bool:
        raise NotImplementedError

    def create(self, livre: Livre) -> Livre:
        raise NotImplementedError

    def update(self, livre: Livre) -> Livre:
        raise NotImplementedError


    def get_personnage_by_livre_id(self, livre_id: int) -> Optional[Personnage]:
        """
        SELECT l.titre as titre_du_livre ,p.nom as nom_du_personnage
from personnage as p
INNER JOIN livre as l
ON l.isbn = p.isbn_livre
WHERE l.id_livre = 1
        :param livre_id:
        :return:
        """
        raise NotImplementedError