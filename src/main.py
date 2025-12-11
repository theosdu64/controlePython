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




if __name__ == "__main__":
    main()