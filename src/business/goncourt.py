from dataclasses import dataclass
from typing import Optional, Any, Dict
from src.daos.auteur_dao import AuteurDao
from src.daos.jury_dao import JuryDao
from src.daos.livre_dao import LivreDao
from src.daos.personnage_dao import PersonnageDao
from src.daos.selection_dao import SelectionDao
from src.daos.vote_dao import VoteDao

from src.model.personnage import Personnage
from src.model.auteur import Auteur
from src.model.jury import Jury
from src.model.livre import Livre
from src.daos.editeur_dao import EditeurDao
from src.model.editeur import Editeur
from src.model.selection import Selection
from src.model.vote import Vote


@dataclass
class Goncourt:
    """Couche métier de l'application de gestion du prix goncourt"""

    @staticmethod
    def get_auteur_by_id(id_auteur: int) -> Auteur | None:
        """Récupérer un auteur a l'aide de son id"""
        auteur_dao = AuteurDao()
        return auteur_dao.read(id_auteur)

    @staticmethod
    def get_jury_by_id(id_jury: int) -> Jury | None:
        """Récupérer un jury a l'aide de son id"""
        jury_dao = JuryDao()
        return jury_dao.read(id_jury)

    @staticmethod
    def get_all_jury_by_id(id_jury: int) -> list[Jury] | None:
        """Recuperer tous les jury d'une selection"""
        jury_dao = JuryDao()
        return jury_dao.read_all(id_jury)

    @staticmethod
    def afficher_jury(jurys: list[Jury]) -> None:
        """Affiche la liste des jurys de manière formatée"""
        if not jurys:
            print("Aucun jury trouvé")
            return

        print(f"\n{'=' * 70}")
        print(f"{'PRÉNOM':<20} {'NOM':<20} {'STATUT':<15}")
        print(f"{'=' * 70}")

        for jury in jurys:
            statut = "Président" if jury.est_president else "Membre"
            print(f"{jury.prenom:<20} {jury.nom:<20} {statut:<15}")

        print(f"{'=' * 70}\n")
        print(f"Total : {len(jurys)} membre(s)")

    @staticmethod
    def get_livre_by_id(id_livre: int) -> Optional[Dict[str, Any]]:
        """Récupérer un livre avec son auteur et éditeur"""
        livre_dao = LivreDao()
        return livre_dao.read(id_livre)

    @staticmethod
    def afficher_livre_details(data: Dict[str, Any]) -> None:
        """Affiche les détails complets d'un livre"""
        if not data:
            print("Livre non trouvé")
            return

        livre = data["livre"]
        print(livre)
        print(f"\nAuteur   : {data['auteur_prenom']} {data['auteur_nom']}")
        print(f"Éditeur  : {data['editeur_nom']}")

    @staticmethod
    def get_all_livre_by_selection(id_selection: int) -> list[Livre] | None:
        """Recuperer tous les livres d'une selection"""
        livre_dao = LivreDao()
        return livre_dao.read_all_by_selection(id_selection)

    @staticmethod
    def afficher_livres(livres: list[Livre]) -> None:
        """Affiche la liste des livres de manière formatée"""
        if not livres:
            print("Aucun livre trouvé pour cette sélection")
            return

        print(f"\n{'=' * 90}")
        print(f"{'TITRE':<40} {'DATE PARUTION':<15} {'PAGES':<8} {'PRIX':<10}")
        print(f"{'=' * 90}")

        for livre in livres:
            print(f"{livre.titre:<40} {str(livre.date_parution):<15} {livre.nb_page:<8} {livre.prix:<10.2f} ")

        print(f"{'=' * 90}\n")
        print(f"Total : {len(livres)} livre(s)")

    @staticmethod
    def get_editeur_by_id(id_editeur: int) -> Optional[Editeur]:
        """Recupere le nom de l'editeur a l'aide de son id"""
        editeur_dao = EditeurDao()
        return editeur_dao.read(id_editeur)

    @staticmethod
    def get_personnage_by_id(id_personnage: int) -> Optional[Personnage]:
        """Recupere le nom du personnage a l'aide de son id"""
        personnage_dao = PersonnageDao()
        return personnage_dao.read(id_personnage)

    # ---------------------------Vote------------------------------------------
    @staticmethod
    def get_vote_by_selection(id_selection: int) -> list[Vote] :
        """
        Recuperer tous les votes d'une selection

        :param id_selection:
        :return: List de vote avec titre du livre
        """
        vote_dao = VoteDao()
        result = vote_dao.read(id_selection)

        print("\nVOTES DE LA SELECTION 1")
        print("=" * 60)

        for vote, titre in result:
            print(f"Livre : {titre}")
            print(vote)
            print("-" * 60)

    @staticmethod
    def create_vote(id_selection: int, id_livre: int) -> Optional[Vote]:
        """Créer un vote """
        vote_dao = VoteDao()
        return vote_dao.create(id_selection, id_livre)

    # ---------------------------Selection------------------------------------------
    def print_selection(selection: Selection) -> None:
        print("\n" + "=" * 80)
        print(f"NUMERO DU TOUR {selection.numero_tour}".center(80))

        print(f"  Date sélection : {selection.date_selection}")
        print(f"  Nombre de livres : {selection.nb_livre}")

    def print_livres(livres: list[Livre]) -> None:
        print("\n" + "=" * 90)
        print(f"{'LIVRES QUALIFIE':^90}")
        print("=" * 90)

        print(f"{'TITRE':<40} {'DATE':<15} {'PAGES':<8} {'PRIX (€)':<10}")
        print("-" * 90)

        for livre in livres:
            print(f"{livre.titre:<40} "
                  f"{str(livre.date_parution):<15} "
                  f"{livre.nb_page:<8} "
                  f"{float(livre.prix):<10.2f}")

        print("=" * 90)
        print(f"Total : {len(livres)} livres\n")

    def print_jury(jury: list[Jury]) -> None:
        print("\n" + "=" * 90)
        print(f"{'JURY DU PRIX GONCOURT':^90}")
        print("=" * 90)

        print(f"{'Nom':<30} {'Prénom':<30} {'Président':<30}")
        print("-" * 90)

        for membre in jury:
            is_pres = "Oui" if membre.est_president else "Non"
            print(f"{membre.nom:<30} {membre.prenom:<30} {is_pres:<30}")

        print("=" * 90)
        print(f"Total : {len(jury)} membres du jury\n")

    @staticmethod
    def get_selection_by_numero_tour(numero_tour: int) -> Optional[Selection]:
        """Recuperé une selection d'un tour"""
        selection_dao = SelectionDao()
        return selection_dao.read(numero_tour)

    @staticmethod
    def get_all_selection_data_by_numero_tour(numero_tour: int) -> None:
        selection_dao = SelectionDao()
        livre_dao = LivreDao()
        jury_dao = JuryDao()

        selection: Selection = selection_dao.read(numero_tour)
        if selection is None:
            print("Aucune sélection trouvée.")
            return

        livres: list[Livre] = livre_dao.read_all_by_selection(selection.id_selection)
        jury: list[Jury] = jury_dao.read_all(selection.id_jury)


        Goncourt.print_selection(selection)
        Goncourt.print_livres(livres)
        Goncourt.print_jury(jury)


