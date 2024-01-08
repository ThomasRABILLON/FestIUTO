from ..app import db

class Photo(db.Model):
    __tablename__ = 'PHOTO'

    id_ph = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.BLOB)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'), primary_key=True)

    def __init__(self, photo: bytes, id_g: int):
        self.photo = photo
        self.id_g = id_g
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.id_ph, self.id_g

    def get_id_ph(self) -> int:
        return self.id_ph

    def get_photo(self) -> bytes:
        return self.photo

    def get_id_g(self) -> int:
        return self.id_g