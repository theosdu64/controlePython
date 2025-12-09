from dataclasses import dataclass
from typing import Optional, Any, Dict
from src.daos.auteur_dao import AuteurDao
from src.daos.jury_dao import JuryDao
from src.daos.livre_dao import LivreDao
from src.daos.personnage_dao import PersonnageDao
from src.model.personnage import Personnage
from src.model.auteur import Auteur
from src.model.jury import Jury
from src.model.livre import Livre
from src.daos.editeur_dao import EditeurDao
from src.model.editeur import Editeur



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

    @staticmethod
    def get_livre_by_id(id_livre: int) -> Optional[Dict[str, Any]]:
        """
        Récupérer un livre a l'aide de son id

        :param id_livre: int
        :return: dict avec livre, auteur_nom, auteur_prenom, editeur_nom
        """
        livre_dao : Livre = LivreDao()
        return livre_dao.read(id_livre)

    @staticmethod
    def get_editeur_by_id(id_editeur : int) -> Optional[Editeur]:
        """
        Recupere le nom de l'editeur a l'aide de son id

        :param id_editeur:
        :return: no mde l'editeur
        """
        editeur_dao : Editeur = EditeurDao()
        return editeur_dao.read(id_editeur)

    @staticmethod
    def get_personnage_by_id(id_personnage : int) -> Optional[Personnage]:
        """
        Recupere le nom du personnage a l'aide de son id

        :param id_personnage:
        :return: un personnage
        """
        personnage_dao : Personnage = PersonnageDao()
        return personnage_dao.read(id_personnage)
