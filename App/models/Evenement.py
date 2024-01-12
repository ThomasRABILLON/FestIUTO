from ..app import db


class Evenement(db.Model):
    __tablename__ = 'EVENEMENT'

    ref_evenement = db.Column(db.Text, primary_key=True)
    jour_arrive = db.Column(db.Integer)
    heure_arrive = db.Column(db.Integer)
    jour_depart = db.Column(db.Integer)
    heure_depart = db.Column(db.Integer)
    duree = db.Column(db.Integer)
    temps_montage = db.Column(db.Integer)
    temps_demontage = db.Column(db.Integer)
    est_public = db.Column(db.Boolean)
    a_preinscription = db.Column(db.Boolean)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))
    id_type_evenement = db.Column(db.Integer, db.ForeignKey('TYPE_EVENEMENT.id_type_evenement'))
    id_lieu = db.Column(db.Integer, db.ForeignKey('LIEU.id_lieu'))

    def __init__(self, ref_evenement: str, jour_arrive: int, heure_arrive: int, jour_depart: int, heure_depart: int, duree: int, temps_montage: int, temps_demontage: int, est_public: bool, a_preinscription: bool, id_g: int, id_type_evenement: int, id_lieu: int):
        self.ref_evenement = ref_evenement
        self.jour_arrive = jour_arrive
        self.heure_arrive = heure_arrive
        self.jour_depart = jour_depart
        self.heure_depart = heure_depart
        self.duree = duree
        self.temps_montage = temps_montage
        self.temps_demontage = temps_demontage
        self.est_public = est_public
        self.a_preinscription = a_preinscription
        self.id_g = id_g
        self.id_type_evenement = id_type_evenement
        self.id_lieu = id_lieu
    
    # les getteurs
    def get_id(self) -> str:
        return self.ref_evenement

    def get_ref_evenement(self) -> str:
        return self.ref_evenement

    def get_jour_arrive(self) -> int:
        return self.jour_arrive

    def get_heure_arrive(self) -> int:
        return self.heure_arrive

    def get_jour_depart(self) -> int:
        return self.jour_depart

    def get_heure_depart(self) -> int:
        return self.heure_depart

    def get_duree(self) -> int:
        return self.duree

    def get_temps_montage(self) -> int:
        return self.temps_montage

    def get_temps_demontage(self) -> int:
        return self.temps_demontage

    def get_est_public(self) -> bool:
        return self.est_public

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
    def get_evenements_by_type_evenement(type_evenement):
        return Evenement.query.filter_by(id_type_evenement=type_evenement.get_id_type_evenement()).all()

    @staticmethod
    def get_evenements_by_jour(jour: int):
        return Evenement.query.filter_by(jour_arrive=jour).all()

    @staticmethod
    def get_evenements_by_reservable():
        return Evenement.query.filter_by(a_preinscription=True).all()
