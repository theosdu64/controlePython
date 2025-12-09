from src.business.goncourt import Goncourt

def main() -> None:
    print("""
    --------------------------
    Bienvenue aux prix goncourt
    --------------------------""")

    print(Goncourt.get_auteur_by_id(11))

if __name__ == "__main__":
    main()
