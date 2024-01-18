from ..app import db

from .Artiste import Artiste
from .Evenement import Evenement

class Groupe(db.Model):
    __tablename__ = 'GROUPE'

    id_g = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_groupe = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    id_style = db.Column(db.Integer, db.ForeignKey('STYLE_MUSICAL.id_style'))

    def __init__(self, nom_groupe: str, description: str, id_style: int):
        self.nom_groupe = nom_groupe
        self.description = description
        self.id_style = id_style
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_g

    def get_nom_groupe(self) -> str:
        return self.nom_groupe

    def get_description(self) -> str:
        return self.description

    def get_id_style(self) -> int:
        return self.id_style

    @staticmethod
    def get_all_groupes() -> list:
        return Groupe.query.all()

    @staticmethod
    def get_groupe_by_id(id_g: int):
        return Groupe.query.filter_by(id_g=id_g).first()

    @staticmethod
    def get_groupe_by_nom(nom_groupe: str):
        return Groupe.query.filter_by(nom_groupe=nom_groupe).first()

    @staticmethod
    def get_groupe_by_style(id_style: int):
        return Groupe.query.filter_by(id_style=id_style).all()

    @staticmethod
    def get_nombre_artiste(id_g: int) -> int:
        return len(Artiste.get_artiste_by_groupe(id_g))
    
    @staticmethod
    def groupe_est_dispo(id_g: int, jour_deb: int, heure_deb: int, jour_fin: int, heure_fin: int) -> bool:
        for i in Evenement.get_evenements_by_groupe(id_g):
            if i.get_jour_deb() == jour_deb and i.get_joue_fin() == jour_fin and ((i.get_heure_fin() == heure_deb and i.get_heure_fin() == heure_fin) or (i.get_heure_fin() < heure_deb and i.get_heure_fin() > heure_fin) or (i.get_heure_fin() > heure_deb and i.get_heure_fin() < heure_fin) or (i.get_heure_fin() < heure_deb and i.get_heure_fin() < heure_deb) or (i.get_heure_fin() > heure_fin and i.get_heure_fin() > heure_fin)):
                return False
        return True

    @staticmethod
    def insert_new_groupe(nom_groupe: str, description: str, id_style: int) -> None:
        db.session.add(Groupe(nom_groupe, description, id_style))
        db.session.commit()

    @staticmethod
    def delete_groupe(nom_groupe: str) -> None:
        db.session.delete(Groupe.get_groupe_by_nom(nom_groupe))
        db.session.commit()