from ..app import db

class Lien_rs(db.Model):
    __tablename__ = 'LIEN_RS'

    id_lien_rs = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lien_rs = db.Column(db.Text)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))

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
    

    @staticmethod
    def get_all_lien_rs() -> list:
        return Lien_rs.query.all()
    
    @staticmethod
    def get_lien_rs_by_id(id_lien_rs: int):
        return Lien_rs.query.get(id_lien_rs)
    
    @staticmethod
    def get_lien_rs_by_id_g(id_g: int):
        return Lien_rs.query.filter_by(id_g=id_g).all()
    
    @staticmethod
    def insert_new_lien_rs(lien_rs: str, id_g: int):
        new_lien_rs = Lien_rs(lien_rs, id_g)
        db.session.add(new_lien_rs)
        db.session.commit()