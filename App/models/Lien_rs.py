from ..app import db

class Lien_rs(db.Model):
    __tablename__ = 'LIEN_RS'

    id_lien_rs = db.Column(db.Integer, primary_key=True)
    lien_rs = db.Column(db.Text)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'), primary_key=True)

    def __init__(self, lien_rs: str, id_g: int):
        self.lien_rs = lien_rs
        self.id_g = id_g
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.id_lien_rs, self.id_g

    def get_id_lien_rs(self) -> int:
        return self.id_lien_rs

    def get_lien_rs(self) -> str:
        return self.lien_rs

    def get_id_g(self) -> int:
        return self.id_g