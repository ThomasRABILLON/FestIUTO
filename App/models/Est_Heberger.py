from ..app import db

from .Hebergement import Hebergement
from .Groupe import Groupe

import datetime

class Est_Heberger(db.Model):
    __tablename__ = 'EST_HEBERGER'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))
    id_hebergement = db.Column(db.Integer, db.ForeignKey('HEBERGEMENT.id_hebergement'))
    date_debut = db.Column(db.Integer)
    date_fin = db.Column(db.Integer)

    def __init__(self, id_g: int, id_hebergement: int, date_debut: int, date_fin: int):
        self.id_g = id_g
        self.id_hebergement = id_hebergement
        self.date_debut = date_debut
        self.date_fin = date_fin
    
    # les getteurs
    def get_id(self) -> int:
        return self.id

    def get_id_g(self) -> int:
        return self.id_g

    def get_id_hebergement(self) -> int:
        return self.id_hebergement

    def get_date_debut(self) -> int:
        return self.date_debut

    def get_date_fin(self) -> int:
        return self.date_fin

    @staticmethod
    def get_all_est_hebergers() -> list:
        return Est_Heberger.query.all()

    @staticmethod
    def get_est_heberger_by_id(id_g: int, id_hebergement: int):
        return Est_Heberger.query.filter_by(id_g=id_g, id_hebergement=id_hebergement).first()

    @staticmethod
    def get_est_heberger_by_groupe(id_g: int):
        return Est_Heberger.query.filter_by(id_g=id_g).all()

    @staticmethod
    def get_est_heberger_by_groupe_and_jour(id_g: int, jour: int):
        return Est_Heberger.query.filter_by(id_g=id_g).filter(Est_Heberger.date_debut <= jour).filter(Est_Heberger.date_fin >= jour).all()

    @staticmethod
    def get_est_heberger_by_hebergement(id_hebergement: int):
        return Est_Heberger.query.filter_by(id_hebergement=id_hebergement).all()


    @staticmethod
    def get_all_hebergements_disponibles(groupe: Groupe, date_debut: int, date_fin: int, nombre_personne: int) -> set:
        hebergements_disponibles = set()
        for jour in range(date_debut, date_fin+1):
            if len(Est_Heberger.get_est_heberger_by_groupe_and_jour(groupe.get_id(), jour)) == 0:
                for hebergement in Hebergement.get_all_hebergements():
                    nombre_place = hebergement.get_nb_place_jour()
                    for est_heberger in Est_Heberger.get_est_heberger_by_hebergement(hebergement.get_id()):
                        if est_heberger.get_date_debut() <= jour and est_heberger.get_date_fin() >= jour:
                            nombre_place -= Groupe.get_nombre_artiste(est_heberger.get_id_g())
                    if nombre_place >= nombre_personne:
                        hebergements_disponibles.add(hebergement)
        return hebergements_disponibles

    @staticmethod
    def insert_est_heberger(id_g: int, id_hebergement: int, date_debut: int, date_fin: int):
        db.session.add(Est_Heberger(id_g, id_hebergement, date_debut, date_fin))
        db.session.commit()

    @staticmethod
    def delete_est_heberger(id_g: int, id_hebergement: int):
        db.session.delete(Est_Heberger.get_est_heberger_by_id(id_g, id_hebergement))
        db.session.commit()