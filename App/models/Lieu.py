from ..app import db

class Lieu(db.Model):
    __tablename__ = 'LIEU'

    id_lieu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text)
    emplacement = db.Column(db.Text)

    def __init__(self, nom: str, emplacement: str):
        self.nom = nom
        self.emplacement = emplacement
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_lieu

    def get_nom(self) -> str:
        return self.nom

    def get_emplacement(self) -> str:
        return self.emplacement

    @staticmethod
    def get_all_lieux() -> list:
        return Lieu.query.all()

    @staticmethod
    def get_lieu_by_id(id_lieu: int):
        return Lieu.query.filter_by(id_lieu=id_lieu).first()

    @staticmethod
    def insert_new_lieu(nom: str, emplacement: str):
        new_lieu = Lieu(nom, emplacement)
        db.session.add(new_lieu)
        db.session.commit()

    @staticmethod
    def delete_lieu(id_lieu: int):
        lieu = Lieu.query.filter_by(id_lieu=id_lieu).first()
        db.session.delete(lieu)
        db.session.commit()