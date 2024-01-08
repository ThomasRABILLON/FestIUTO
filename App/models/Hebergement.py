from ..app import db

class Hebergement(db.Model):
    __tablename__ = 'HEBERGEMENT'

    id_hebergement = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nb_place_jour = db.Column(db.Integer)

    def __init__(self, nb_place_jour: int):
        self.nb_place_jour = nb_place_jour
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_hebergement

    def get_nb_place_jour(self) -> int:
        return self.nb_place_jour