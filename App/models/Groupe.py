from ..app import db

from .Artiste import Artiste
from .Evenement import Evenement
from .Lien_rs import Lien_rs
from .Lien_video import Lien_video
from .Photo import Photo

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
    def delete_groupe(nom_groupe: str, Est_Heberger) -> None:
        for artiste in Artiste.get_artiste_by_groupe(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Artiste.delete_artiste(artiste.get_id())

        for event in Evenement.get_evenements_by_groupe(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Evenement.delete_evenement(event.get_id())

        for est_heberger in Est_Heberger.get_est_heberger_by_groupe(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Est_Heberger.delete_est_heberger_by_id(est_heberger.get_id())

        for lien_rs in Lien_rs.get_lien_rs_by_id_g(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Lien_rs.delete_lien_rs(lien_rs.get_id_lien_rs())

        for lien_video in Lien_video.get_lien_video_by_id_g(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Lien_video.delete_lien_video(lien_video.get_id_lien_video())

        for photo in Photo.get_photo_by_id_g(Groupe.get_groupe_by_nom(nom_groupe).get_id()):
            Photo.delete_photo(photo.get_id_photo())

        db.session.delete(Groupe.get_groupe_by_nom(nom_groupe))
        db.session.commit()