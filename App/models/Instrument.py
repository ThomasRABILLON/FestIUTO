from ..app import db

class Instrument(db.Model):
    __tablename__ = 'INSTRUMENT'

    id_instru = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_instru = db.Column(db.Text)

    def __init__(self, nom_instru: str):
        self.nom_instru = nom_instru
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_instru

    def get_nom_instru(self) -> str:
        return self.nom_instru

    @staticmethod
    def get_all_instruments() -> list:
        return Instrument.query.all()

    @staticmethod
    def get_instrument_by_id(id_instru: int):
        return Instrument.query.filter_by(id_instru=id_instru).first()