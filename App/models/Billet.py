from ..app import db


class Billet(db.Model):
    __tablename__ = 'BILLET'

    id_billet = db.Column(db.Integer, primary_key=True, autoincrement=True)
    debut_validite = db.Column(db.Integer)
    fin_validite = db.Column(db.Integer)
    mail = db.Column(db.Text, db.ForeignKey('SPECTATEUR.mail'))
    id_type_billet = db.Column(db.Integer, db.ForeignKey('TYPE_BILLET.id_type_billet'))

    def __init__(self, debut_validite: int, fin_validite: int, mail: str, id_type_billet: int):
        self.debut_validite = debut_validite
        self.fin_validite = fin_validite
        self.mail = mail
        self.id_type_billet = id_type_billet
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_billet

    def get_debut_validite(self) -> int:
        return self.debut_validite

    def get_fin_validite(self) -> int:
        return self.fin_validite

    def get_id_spec(self) -> int:
        return self.id_spec

    def get_id_type_billet(self) -> int:
        return self.id_type_billet

    @staticmethod
    def get_billet_by_spectateur(mail: str) -> list:
        return Billet.query.filter_by(mail=mail).all()

    @staticmethod
    def get_billet_by_spectateur_and_date(mail: str, date: int, date_fin: int):
        return Billet.query.filter_by(mail=mail).filter(Billet.debut_validite <= date).filter(Billet.fin_validite >= date_fin).first()

    @staticmethod
    def get_billet_by_spectateur_and_1date(mail: str, date: int):
        return Billet.query.filter_by(mail=mail).filter(Billet.debut_validite <= date).filter(Billet.fin_validite >= date).first()


    @staticmethod
    def insert_new_billet(debut_validite: int, fin_validite: int, mail: str, id_type_billet: int) -> None:
        db.session.add(Billet(debut_validite, fin_validite, mail, id_type_billet))
        db.session.commit()