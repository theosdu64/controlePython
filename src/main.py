from src.business.goncourt import Goncourt


def main() -> None:
    print("""
    --------------------------
    Bienvenue aux prix goncourt
    --------------------------""")

    print("-" * 60)
    print(Goncourt.get_auteur_by_id(11))

    print("-" * 60)
    print(Goncourt.get_jury_by_id(1))

    print("*" * 60)
    jurys = Goncourt.get_all_jury_by_id(1)
    Goncourt.afficher_jury(jurys)

    print("-" * 60)
    livres = Goncourt.get_all_livre_by_selection(1)
    Goncourt.afficher_livres(livres)

    print("-" * 60)
    data = Goncourt.get_livre_by_id(1)
    Goncourt.afficher_livre_details(data)

    print("-" * 60)
    print(Goncourt.get_personnage_by_id(2))

    print("-" * 60)
    print(Goncourt.get_selection_by_numero_tour(1))

    print("-" * 60)
    print(Goncourt.get_all_selection_data_by_numero_tour(2))

if __name__ == "__main__":
    main()