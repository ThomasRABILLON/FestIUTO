from ..app import db
from flask_login import UserMixin

import datetime

class Spectateur(db.Model, UserMixin):
    __tablename__ = 'SPECTATEUR'

    mail = db.Column(db.Text, primary_key=True)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    mot_de_passe = db.Column(db.Text)
    date_naissance = db.Column(db.Date)

    def __init__(self, mail: str, nom: str, prenom: str, mot_de_passe: str, date_naissance: datetime):
        self.mail = mail
        self.nom = nom
        self.prenom = prenom
        self.mot_de_passe = mot_de_passe
        self.date_naissance = date_naissance
    
    # les getteurs
    def get_id(self) -> str:
        return self.mail

    def get_nom(self) -> str:
        return self.nom

    def get_prenom(self) -> str:
        return self.prenom

    def get_mot_de_passe(self) -> str:
        return self.mot_de_passe

    def get_date_naissance(self) -> datetime:
        return self.date_naissance

    @staticmethod
    def get_all_spectateurs() -> list:
        return Spectateur.query.all()

    @staticmethod
    def get_spectateur_by_id(id: int) -> 'Spectateur':
        return Spectateur.query.get(id)

    @staticmethod
    def get_spectateur_by_mail(mail: str) -> 'Spectateur':
        return Spectateur.query.get(mail)

    @staticmethod
    def insert_new_spectateur(mail: str, nom: str, prenom: str, mot_de_passe: str, date_naissance: datetime) -> None:
        db.session.add(Spectateur(mail, nom, prenom, mot_de_passe, date_naissance))
        db.session.commit()