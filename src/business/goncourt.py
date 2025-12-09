from dataclasses import dataclass

from src.daos.auteur_dao import AuteurDao
from src.daos.jury_dao import JuryDao
from src.model.auteur import Auteur
from src.model.jury import Jury


@dataclass
class Goncourt:
    """Couche métier de l'application de gestion du prix goncourt"""

    @staticmethod
    def get_auteur_by_id(id_auteur : int) -> Auteur | None:
        """Récupérer un auteur a l'aide de son id

        :param : id_auteur : int
        : return un Auteur(nom , prenom)
        """
        auteur_dao : Auteur = AuteurDao()
        return auteur_dao.read(id_auteur)

    @staticmethod
    def get_jury_by_id(id_jury : int) -> Jury | None:
        """Récupérer un jury a l'aide de son id

        :param : id_jury : int
        : return un Jury(nom , prenom, est_president ?)
        """
        jury_dao : Jury = JuryDao()
        return jury_dao.read(id_jury)