from ..app import db

class A_Favori(db.Model):
    __tablename__ = 'A_FAVORI'

    mail = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.mail'), primary_key=True)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'), primary_key=True)

    def __init__(self, mail: str, id_g: int):
        self.mail = mail
        self.id_g = id_g
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.mail, self.id_g

    def get_id_spec(self) -> str:
        return self.mail

    def get_id_g(self) -> int:
        return self.id_g

    @staticmethod
    def get_all_favoris() -> list:
        return A_Favori.query.all()

    @staticmethod
    def get_favori_by_id(mail: str, id_g: int):
        return A_Favori.query.filter_by(mail=mail, id_g=id_g).first()

    @staticmethod
    def get_favori_by_spec(mail: str):
        return A_Favori.query.filter_by(mail=mail).all()

    @staticmethod
    def insert_new_favori(mail: str, id_g: int):
        db.session.add(A_Favori(mail, id_g))
        db.session.commit()

    @staticmethod
    def delete_favori(mail: str, id_g: int):
        A_Favori.query.filter_by(mail=mail, id_g=id_g).delete()
        db.session.commit()