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

if __name__ == "__main__":
    main()
