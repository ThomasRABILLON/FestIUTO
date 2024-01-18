from ..app import db

import time

class Evenement(db.Model):
    __tablename__ = 'EVENEMENT'

    ref_evenement = db.Column(db.Text, primary_key=True)
    jour_deb = db.Column(db.Integer)
    heure_deb = db.Column(db.Time)
    jour_fin = db.Column(db.Integer)
    heure_fin = db.Column(db.Time)
    duree = db.Column(db.Time)
    temps_montage = db.Column(db.Time)
    temps_demontage = db.Column(db.Time)
    est_public = db.Column(db.Boolean)
    nb_place = db.Column(db.Integer)
    a_preinscription = db.Column(db.Boolean)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))
    id_type_evenement = db.Column(db.Integer, db.ForeignKey('TYPE_EVENEMENT.id_type_evenement'))
    id_lieu = db.Column(db.Integer, db.ForeignKey('LIEU.id_lieu'))

    def __init__(self, ref_evenement: str, jour_deb: int, heure_deb: time, jour_fin: int, heure_fin: time, duree: time, temps_montage: time, temps_demontage: time, est_public: bool, nb_place: int, a_preinscription: bool, id_g: int, id_type_evenement: int, id_lieu: int):
        self.ref_evenement = ref_evenement
        self.jour_deb = jour_deb
        self.heure_deb = heure_deb
        self.jour_fin = jour_fin
        self.heure_fin = heure_fin
        self.duree = duree
        self.temps_montage = temps_montage
        self.temps_demontage = temps_demontage
        self.est_public = est_public
        self.nb_place = nb_place
        self.a_preinscription = a_preinscription
        self.id_g = id_g
        self.id_type_evenement = id_type_evenement
        self.id_lieu = id_lieu
    
    # les getteurs
    def get_id(self) -> str:
        return self.ref_evenement

    def get_ref_evenement(self) -> str:
        return self.ref_evenement

    def get_jour_deb(self) -> int:
        return self.jour_deb

    def get_heure_deb(self) -> time:
        return self.heure_deb

    def get_jour_fin(self) -> int:
        return self.jour_fin

    def get_heure_fin(self) -> time:
        return self.heure_fin

    def get_duree(self) -> time:
        return self.duree

    def get_temps_montage(self) -> time:
        return self.temps_montage

    def get_temps_demontage(self) -> time:
        return self.temps_demontage

    def get_est_public(self) -> bool:
        return self.est_public
    
    def get_nb_place(self) -> int:
        return self.nb_place

    def get_a_preinscription(self) -> bool:
        return self.a_preinscription

    def get_id_g(self) -> int:
        return self.id_g

    def get_id_type_evenement(self) -> int:
        return self.id_type_evenement

    def get_id_lieu(self) -> int:
        return self.id_lieu

    @staticmethod
    def get_all_evenements() -> list:
        return Evenement.query.all()

    @staticmethod
    def get_evenement_by_id(id: str):
        return Evenement.query.filter_by(ref_evenement=id).first()

    @staticmethod
    def get_evenements_by_groupe(id_g: int):
        return Evenement.query.filter_by(id_g=id_g).all()
    
    @staticmethod
    def get_evenements_by_lieu(id_lieu: int):
        return Evenement.query.filter_by(id_lieu=id_lieu).all()

    @staticmethod
    def get_evenements_by_type_evenement(type_evenement):
        return Evenement.query.filter_by(id_type_evenement=type_evenement.get_id_type_evenement()).all()

    @staticmethod
    def get_evenements_by_jour(jour: int):
        return Evenement.query.filter_by(jour_deb=jour).all()

    @staticmethod
    def get_evenements_by_reservable():
        return Evenement.query.filter_by(a_preinscription=True).all()
    
    @staticmethod
    def insert_new_evenement(ref_evenement: str, jour_deb: int, heure_deb: time, jour_fin: int, heure_fin: time, duree: time, temps_montage: time, temps_demontage: time, est_public: bool, nb_place: int, a_preinscription: bool, id_g: int, id_type_evenement: int, id_lieu: int):
        db.session.add(Evenement(ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, nb_place, a_preinscription, id_g, id_type_evenement, id_lieu))
        db.session.commit()

    @staticmethod
    def delete_evenement(ref_evenement: str):
        Evenement.query.filter_by(ref_evenement=ref_evenement).delete()
        db.session.commit()
