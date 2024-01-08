from ..app import db

class Lien_video(db.Model):
    __tablename__ = 'LIEN_VIDEO'

    id_lien_video = db.Column(db.Integer, primary_key=True)
    lien_video = db.Column(db.Text)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'), primary_key=True)

    def __init__(self, lien_video: str, id_g: int):
        self.lien_video = lien_video
        self.id_g = id_g
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.id_lien_video, self.id_g

    def get_id_lien_video(self) -> int:
        return self.id_lien_video

    def get_lien_video(self) -> str:
        return self.lien_video

    def get_id_g(self) -> int:
        return self.id_g