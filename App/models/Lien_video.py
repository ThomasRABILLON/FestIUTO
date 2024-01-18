from ..app import db

class Lien_video(db.Model):
    __tablename__ = 'LIEN_VIDEO'

    id_lien_video = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lien_video = db.Column(db.Text)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))

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
    

    @staticmethod
    def get_all_lien_video() -> list:
        return Lien_video.query.all()
    
    @staticmethod
    def get_lien_video_by_id(id_lien_video: int):
        return Lien_video.query.get(id_lien_video)
    
    @staticmethod
    def get_lien_video_by_id_g(id_g: int):
        return Lien_video.query.filter_by(id_g=id_g).all()
    
    @staticmethod
    def insert_new_lien_video(lien_video: str, id_g: int):
        new_lien_video = Lien_video(lien_video, id_g)
        db.session.add(new_lien_video)
        db.session.commit()