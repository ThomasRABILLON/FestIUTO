from ..app import db

class Type_billet(db.Model):
    __tablename__ = 'TYPE_BILLET'

    id_type_billet = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.Text)
    duree = db.Column(db.Integer)
    prix = db.Column(db.Float)

    def __init__(self, libelle: str, duree: int, prix: float):
        self.libelle = libelle
        self.duree = duree
        self.prix = prix
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_type_billet

    def get_libelle(self) -> str:
        return self.libelle

    def get_duree(self) -> int:
        return self.duree

    def get_prix(self) -> float:
        return self.prix

    @staticmethod
    def get_all_type_billets() -> list:
        return Type_billet.query.all()

    @staticmethod
    def get_type_billet_by_id(id_type_billet: int):
        return Type_billet.query.filter_by(id_type_billet=id_type_billet).first()