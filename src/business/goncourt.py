from dataclasses import dataclass
from typing import Optional, Any, Dict
from src.daos.auteur_dao import AuteurDao
from src.daos.dao import Dao
from src.daos.jury_dao import JuryDao
from src.daos.livre_dao import LivreDao
from src.daos.personnage_dao import PersonnageDao
from src.daos.selection_dao import SelectionDao
from src.daos.vote_dao import VoteDao
from src.model import jury

from src.model.personnage import Personnage
from src.model.auteur import Auteur
from src.model.jury import Jury
from src.model.livre import Livre
from src.daos.editeur_dao import EditeurDao
from src.model.editeur import Editeur
from src.model.selection import Selection
from src.model.vote import Vote

from typing import Any
from datetime import datetime

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

    def getTour(numero_tour: int) -> str:
        if numero_tour == 1:
            return "Premier tour (8 livres à choisir)"
        elif numero_tour == 2:
            return "Deuxième tour (4 livres à choisir)"
        elif numero_tour == 3:
            return "Troisième tour (1 livre à choisir)"
        else:
            return "Tour inconnu"


    @staticmethod
    def processus_de_selection() -> Any:
        jury_dao = JuryDao()
        selection_dao = SelectionDao()
        livre_dao = LivreDao()
        vote_dao = VoteDao()

        year_today = datetime.today().year
        print(f"\n{'=' * 60}")
        print(f"Processus de seleection pour l'annee : {year_today}")
        print(f"{'=' * 60}\n")

        # Recuperation du jury et des selectiond de l'annee

        jury_actuel = jury_dao.read_by_year(year_today)
        if not jury_actuel:
            print(f"Aucun jury trouvé pour l'année {year_today}")
            return

        print(f"Année Jury sélectionné : {jury_actuel.annee}\n")

        selections = selection_dao.read_all_by_year(year_today)
        if not selections:
            print(f"Aucune sélection trouvée pour l'année {year_today}")
            return

        # Affichage des tours existant

        print(f"Tours de sélection pour l'année {year_today}:\n")
        print(f"{'ID Sélection':<15} {'Tour':<8} {'Date':<15} {'Nb livres':<12} {'ID Jury':<10}")
        print("-" * 70)

        for sel in selections:
            print(f"{sel.id_selection:<15} {sel.numero_tour:<8} "
                  f"{sel.date_selection.strftime('%Y-%m-%d'):<15} "
                  f"{sel.nb_livre:<12} {sel.id_jury:<10}")

        # Déterminer le tour actuel
        numero_tour_max = max(sel.numero_tour for sel in selections)
        id_selection_actuelle = max(sel.id_selection for sel in selections if sel.numero_tour == numero_tour_max)

        print(f"\n{'=' * 70}")
        print(f"Tour actuel : {Goncourt.getTour(numero_tour_max)}")
        print(f"{'=' * 70}\n")


        # Affichage des livres du tour actuel
        livres = livre_dao.read_all_by_selection(id_selection_actuelle)

        if not livres:
            print(f"Aucun livre trouvé pour la sélection avec l'id : {id_selection_actuelle}")
            return

        print(f"Livres en compétition (Tour {numero_tour_max}):\n")
        print(f"{'ID':<5} {'TITRE':<30} {'DATE PARUTION':<15} {'PAGES':<8} {'PRIX':<10}")
        print("=" * 75)

        for livre in livres:
            print(f"{livre.id_livre:<5} {livre.titre:<30} "
                  f"{livre.date_parution.strftime('%Y-%m-%d'):<15} "
                  f"{livre.nb_page:<8} {livre.prix:<10.2f}€")

        print("=" * 75)
        print(f"Total : {len(livres)} livres en compétition\n")

        # Saisie des votes

        print("PHASE DE VOTE")
        print("-" * 70)
        print("Format attendu : id_livre,nb_votes ...")
        print("Exemple : 1,5 3,8 7,12")
        print("-" * 70)

        vote_input = input("\nEntrez les votes : ").strip()

        if not vote_input:
            print("Aucun vote saisi , processus terminé.")
            return

        # Enregistrement des votes

        votes = []
        print("\nEnregistrement des votes")

        for vote_str in vote_input.split():
            try:
                id_livre, nb_vote = vote_str.split(",")
                id_livre = int(id_livre)
                nb_vote = int(nb_vote)

                # Créer le vote pour le tour actuel
                vote = vote_dao.create(
                    id_selection=id_selection_actuelle,
                    id_livre=id_livre,
                    nb_voix=nb_vote
                )

                if vote:
                    votes.append((id_livre, nb_vote))
                    print(f"vote enregistré : Livre {id_livre} → {nb_vote} voix")
                else:
                    print(f"erreur lors de l'enregistrement du vote pour le livre {id_livre}")

            except ValueError:
                print(f"format invalide : '{vote_str}' ignoré")
                continue

        if not votes:
            print("\n aucun vote valide enregistre.")
            return

        # Affichage des resultat du vote

        print(f"\n{'=' * 70}")
        print("Resultat du vote")
        print(f"{'=' * 70}\n")

        resultats_votes = vote_dao.read(id_selection_actuelle)

        if resultats_votes:
            print(f"{'Rang':<6} {'ID Livre':<10} {'Titre':<30} {'Voix':<10}")
            print("-" * 70)

            for i, (vote, titre) in enumerate(resultats_votes, 1):
                print(f"{i:<6} {vote.id_livre:<10} {titre:<30} {vote.nb_voix:<10}")

            print("=" * 70)

        # Trouver les qualifié

        # Définir le nombre de qualifiés selon le tour
        nb_qualifies_dict = {
            1: 8,
            2: 4,
            3: 1
        }

        nb_qualifies = nb_qualifies_dict.get(numero_tour_max, 1)

        print(f"\n nombre de qualifiés pour le prochain tour : {nb_qualifies}")

        livres_qualifies = resultats_votes[:nb_qualifies] if resultats_votes else []

        if not livres_qualifies:
            print("Pas de livre qualifié.")
            return

        print(f"\n Livres qualifié :")
        for i, (vote, titre) in enumerate(livres_qualifies, 1):
            print(f"  {i}. Id livre {vote.id_livre} - {titre} ({vote.nb_voix} voix)")

        # 8 Création de la nouvelle selection

        nouveau_tour = numero_tour_max + 1
        nouvel_id_selection = id_selection_actuelle + 1

        print(f"\n{'=' * 70}")
        print(f" creation du tour {nouveau_tour}")
        print(f"{'=' * 70}\n")

        nouvelle_selection = Selection(
            id_selection=nouvel_id_selection,
            numero_tour=nouveau_tour,
            date_selection=datetime.today(),
            nb_livre=nb_qualifies,
            id_jury=jury_actuel.id_jury
        )

        selection_cree = selection_dao.create(nouvelle_selection)

        if not selection_cree:
            print("erreur de creation de la sélection")
            return

        print(f" sélection créée avec l'ID {nouvel_id_selection}, tour numero : {nouveau_tour}, "
              f"{nb_qualifies} livre")

        # Ajout des livres qualifie dans la nouvelle selection

        print(f"\n Ajout des livres qualifiés dans la nouvelle sélection...")

        for vote, titre in livres_qualifies:
            resultat = selection_dao.updates_of_qualifiers(vote.id_livre, nouvel_id_selection)
            if resultat:
                print(f"livre {vote.id_livre} ajouté à la sélection {nouvel_id_selection}")
            else:
                print(f"erreur lors de l'ajout du livre {vote.id_livre}")

        # Affichage final

        print(f"\n{'=' * 70}")
        print(f"Processus Terminé {nouveau_tour} prêt")
        print(f"{'=' * 70}\n")

        # Afficher les livres du nouveau tour
        livres_nouveau_tour = livre_dao.read_all_by_selection(nouvel_id_selection)

        print(f"Livres qualifiés pour le {Goncourt.getTour(nouveau_tour)}:\n")
        print(f"{'ID':<5} {'TITRE':<30} {'DATE PARUTION':<15} {'PAGES':<8} {'PRIX':<10}")
        print("=" * 75)

        for livre in livres_nouveau_tour:
            print(f"{livre.id_livre:<5} {livre.titre:<30} "
                  f"{livre.date_parution.strftime('%Y-%m-%d'):<15} "
                  f"{livre.nb_page:<8} {livre.prix:<10.2f}€")

        print("=" * 75)
        print(f"\n{'Le livre a gagné le prix Goncourt : ' if len(livres_nouveau_tour) == 1 else 'Livres en compétition pour le prochain tour'}\n")

    @staticmethod
    def reinitialiser_selections() -> bool:
        try:
            with Dao.connection.cursor() as cursor:
                print("\n" + "=" * 70)
                print("Suppression de la selection")

                sql_delete_votes = "DELETE FROM vote"
                cursor.execute(sql_delete_votes)

                sql_delete_fait_partie = """
                    DELETE FROM fait_partie_de 
                    WHERE id_selection != 1
                """
                cursor.execute(sql_delete_fait_partie)

                sql_delete_selections = """
                    DELETE FROM selection 
                    WHERE id_selection != 1
                """
                cursor.execute(sql_delete_selections)
                Dao.connection.commit()
                print("\n" + "=" * 70)
                print("Reinitialisation de selection faite")

                return True

        except Exception as e:
            print(f"\n erreur de Reinitialisation : {e}")
            Dao.connection.rollback()
            import traceback
            traceback.print_exc()
            return False
