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
    print("-" * 60)
    data = Goncourt.get_livre_by_id(1)
    if data:
        livre = data["livre"]
        print(livre)
        print(f"\nAuteur   : {data['auteur_prenom']} {data['auteur_nom']}")
        print(f"Éditeur  : {data['editeur_nom']}")
    else:
        print("Livre non trouvé")
    print("-" * 60)
    print(Goncourt.get_editeur_by_id(1))
    print("-" * 60)
    print(Goncourt.get_personnage_by_id(2))
    print("-" * 60)

if __name__ == "__main__":
    main()
