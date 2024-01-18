from ..app import db


class Hebergement(db.Model):
    __tablename__ = 'HEBERGEMENT'

    id_hebergement = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_hebergement = db.Column(db.Text)
    nb_place_jour = db.Column(db.Integer)

    def __init__(self, nom_hebergement: str, nb_place_jour: int):
        self.nom_hebergement = nom_hebergement
        self.nb_place_jour = nb_place_jour
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_hebergement
    
    def get_nom_hebergement(self) -> str:
        return self.nom_hebergement

    def get_nb_place_jour(self) -> int:
        return self.nb_place_jour

    @staticmethod
    def get_all_hebergements() -> list:
        return Hebergement.query.all()

    @staticmethod
    def get_hebergement_by_id(id_hebergement: int):
        return Hebergement.query.filter_by(id_hebergement=id_hebergement).first()

    @staticmethod
    def insert_hebergement(nom_hebergement: str, nb_place_jour: int):
        db.session.add(Hebergement(nom_hebergement, nb_place_jour))
        db.session.commit()

    @staticmethod
    def delete_hebergement(id_hebergement: int, Est_Heberger):
        for est_heberger in Est_Heberger.get_est_heberger_by_hebergement(id_hebergement):
            db.session.delete(est_heberger)
        db.session.delete(Hebergement.get_hebergement_by_id(id_hebergement))
        db.session.commit()