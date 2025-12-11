from src.business.goncourt import Goncourt


def main() -> None:
    print("""
    --------------------------
    Bienvenue aux prix goncourt
    --------------------------""")

    goncourt_programme = True
    while goncourt_programme:
        print("\n" + "-" * 50)
        print('Menu principal du prix Goncourt - choisir par son numéro')
        print("\n" + "-" * 50)
        print('1 - Afficher les membres du jury')
        print('2 - Afficher les livres des auteur')
        print('3 - Afficher les livres du selection')
        print('4 - Processus de selection')
        print('5 - Réinitialisation des selections')
        print("0 - Quitter")

        choix_user = input("\n Votre choix : ")
        if choix_user == '1':
            print('Affichage des membres du jury')
            print("\n" + "-" * 50)

            try:
                id_jury = int(input("entrez l'id du jury : "))
                jury = Goncourt.get_all_jury_by_id(id_jury)

                if jury:
                    Goncourt.afficher_jury(jury)
                else:
                    print(f"aucun jury trouvé")

            except ValueError:
                print("erreur : entrer un id valide")
                continue

        elif choix_user == '2':
            print('Affichage dun auteur par id')
            try:
                id_auteur = int(input("entrez l'id de l'auteur : "))
                auteur = Goncourt.get_auteur_by_id(id_auteur)

                if auteur:
                    print(auteur)
                else:
                    print("erreur : entrez un id valide")

            except ValueError:
                print("erreur : entrez un id valide")
                continue

        elif choix_user == '3':
            print('Affichage des livres')
            try:
                id_selection = int(input("entrez l'id de selection : "))
                livres = Goncourt.get_all_livre_by_selection(id_selection)

                if livres:
                    Goncourt.afficher_livres(livres)
                else:
                    print("erreur : entrez un id valide")
            except ValueError:
                print("erreur : entrez un id valide")
                continue

        elif choix_user == '4':
            print('Processus de selection')
            try:
                Goncourt.processus_de_selection()
            except ValueError:
                print("erreur lors du processus de selection")

        elif choix_user == '5':
            print('Réinitialisation des selections')
            try:
                Goncourt.reinitialiser_selections()
            except ValueError:
                print("Réinitialisation des selections")

        elif choix_user == '0':
            print('Quitter')
            goncourt_programme = False
        else:
            print("choix invalide , recommencez")


if __name__ == "__main__":
    main()