from ..app import db

class Est_Inscrit(db.Model):
    __tablename__ = 'EST_INSCRIT'

    mail = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.mail'), primary_key=True)
    ref_evenement = db.Column(db.Text, db.ForeignKey('EVENEMENT.ref_evenement'), primary_key=True)

    def __init__(self, mail: str, ref_evenement: str):
        self.mail = mail
        self.ref_evenement = ref_evenement
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.mail, self.ref_evenement

    def get_mail(self) -> str:
        return self.mail

    def get_ref_evenement(self) -> str:
        return self.ref_evenement

    @staticmethod
    def insert_new_inscription(mail: str, ref_evenement: str) -> None:
        db.session.add(Est_Inscrit(mail, ref_evenement))
        db.session.commit()

    @staticmethod
    def get_inscription_by_mail(mail: str) -> list:
        return Est_Inscrit.query.filter_by(mail=mail).all()

    @staticmethod
    def get_inscription_by_ref_evenement(ref_evenement: str) -> list:
        return Est_Inscrit.query.filter_by(ref_evenement=ref_evenement).all()

    @staticmethod
    def get_inscription_by_spectateur_and_evenement(mail: str, ref_evenement: str):
        return Est_Inscrit.query.filter_by(mail=mail, ref_evenement=ref_evenement).first()