from dataclasses import dataclass
from typing import Optional, List
from src.daos.dao import Dao
from src.model.jury import Jury

@dataclass
class JuryDao(Dao[Jury]):

    def read(self, id_personne: int) -> Optional[Jury]:
        """Renvoie le membre du jury correspondant à l'id_personne"""
        try :
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT p.nom, p.prenom, em.est_president
                    FROM est_membre AS em
                    INNER JOIN personne AS p
                        ON p.id_personne = em.id_personne
                    WHERE em.id_personne = %s
                """
                cursor.execute(sql, (id_personne,))
                record = cursor.fetchone()

            if record is not None:
                jury = Jury(
                    record['nom'],
                    record['prenom'],
                    record['est_president']
                )
                jury.id_personne = id_personne
            else:
                jury = None
            return jury
        except Exception as e:
            print(e)

    def read_all(self) -> List[Jury]:
        raise NotImplemented

    def create(self, jury: Jury) -> int:
        raise NotImplemented

    def delete(self, id_jury: int) -> None:
        raise NotImplemented

    def update(self, id_jury, obj : Jury) -> bool:
        raise NotImplemented