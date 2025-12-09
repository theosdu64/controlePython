from dataclasses import dataclass

from src.daos.auteur_dao import AuteurDao
from src.model.auteur import Auteur

@dataclass
class Goncourt:
    """Couche métier de l'application de gestion du prix goncourt"""

    @staticmethod
    def get_auteur_by_id(id_auteur : int) -> Auteur | None:
        print(id_auteur)
        """Récupérer un auteur a l'aide de son id

        :param : id_auteur : int
        : return un Auteur(nom , prenom)
        """
        auteur_dao : Auteur = AuteurDao()
        return auteur_dao.read(id_auteur)
