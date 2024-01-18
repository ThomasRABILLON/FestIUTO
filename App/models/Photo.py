from ..app import db

class Photo(db.Model):
    __tablename__ = 'PHOTO'

    id_ph = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo = db.Column(db.LargeBinary)
    id_g = db.Column(db.Integer, db.ForeignKey('GROUPE.id_g'))

    def __init__(self, photo: bytes, id_g: int):
        self.photo = photo
        self.id_g = id_g

    def get_id(self) -> int:
        return self.id_ph

    def get_photo(self) -> bytes:
        return self.photo

    def get_id_g(self) -> int:
        return self.id_g
    
    @staticmethod
    def get_all_photo() -> list:
        return Photo.query.all()
    
    @staticmethod
    def get_photo_by_id(id_ph: int):
        return Photo.query.get(id_ph)
    
    @staticmethod
    def get_photo_by_id_g(id_g: int):
        return Photo.query.filter_by(id_g=id_g).all()
    
    @staticmethod
    def insert_new_photo(photo: bytes, id_g: int):
        new_photo = Photo(photo, id_g)
        db.session.add(new_photo)
        db.session.commit()
        