from ..app import db

import datetime

class Est_Heberger(db.Model):
    __tablename__ = 'EST_HEBERGER'

    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'), primary_key=True)
    id_hebergement = db.Column(db.Integer, db.ForeignKey('HEBERGEMENT.id_hebergement'), primary_key=True)
    date_debut = db.Column(db.DateTime)
    date_fin = db.Column(db.DateTime)
    duree = db.Column(db.Integer)

    def __init__(self, id_g: int, id_hebergement: int, date_debut: datetime, date_fin: datetime, duree: int):
        self.id_g = id_g
        self.id_hebergement = id_hebergement
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.duree = duree
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.id_g, self.id_hebergement

    def get_id_g(self) -> int:
        return self.id_g

    def get_id_hebergement(self) -> int:
        return self.id_hebergement

    def get_date_debut(self) -> datetime:
        return self.date_debut

    def get_date_fin(self) -> datetime:
        return self.date_fin

    def get_duree(self) -> int:
        return self.duree