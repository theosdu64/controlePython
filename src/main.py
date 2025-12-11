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


if __name__ == "__main__":
    main()