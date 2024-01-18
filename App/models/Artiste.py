from ..app import db

class Artiste(db.Model):
    __tablename__ = 'ARTISTE'

    id_art = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    id_g = db.Column(db.Text, db.ForeignKey('GROUPE.id_g'))
    id_instru = db.Column(db.Text, db.ForeignKey('INSTRUMENT.id_instru'))

    def __init__(self, nom: str, prenom: str, id_g: int, id_instru: int):
        self.nom = nom
        self.prenom = prenom
        self.id_g = id_g
        self.id_instru = id_instru
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_art

    def get_nom(self) -> str:
        return self.nom

    def get_prenom(self) -> str:
        return self.prenom

    def get_id_g(self) -> str:
        return self.id_g

    def get_id_instru(self) -> str:
        return self.id_instru

    @staticmethod
    def get_all_artistes() -> list:
        return Artiste.query.all()

    @staticmethod
    def get_artiste_by_id(id_art: int):
        return Artiste.query.filter_by(id_art=id_art).first()

    @staticmethod
    def get_artiste_by_groupe(id_g: int):
        return Artiste.query.filter_by(id_g=id_g).all()

    @staticmethod
    def insert_new_artiste(nom: str, prenom: str, id_g: int, id_instru: int) -> None:
        db.session.add(Artiste(nom, prenom, id_g, id_instru))
        db.session.commit()

    @staticmethod
    def delete_artiste(id_art: int) -> None:
        Artiste.query.filter_by(id_art=id_art).delete()
        db.session.commit()
