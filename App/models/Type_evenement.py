from ..app import db

class Type_evenement(db.Model):
    __tablename__ = 'TYPE_EVENEMENT'

    id_type_evenement = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.Text)

    def __init__(self, id_type_evenement: int, libelle: str):
        self.id_type_evenement = id_type_evenement
        self.libelle = libelle
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_type_evenement

    def get_libelle(self) -> str:
        return self.libelle

    @staticmethod
    def get_all_type_evenement() -> list:
        return Type_evenement.query.all()

    @staticmethod
    def get_type_evenement_by_id(id_type_evenement: int):
        return Type_evenement.query.filter_by(id_type_evenement=id_type_evenement).first()