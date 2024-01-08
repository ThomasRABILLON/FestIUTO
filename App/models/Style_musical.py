from ..app import db

class Style_musical(db.Model):
    __tablename__ = 'STYLE_MUSICAL'

    id_style = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.Text)

    def __init__(self, libelle: str):
        self.libelle = libelle
    
    # les getteurs
    def get_id(self) -> int:
        return self.id_style

    def get_libelle(self) -> str:
        return self.libelle

    @staticmethod
    def get_all_styles() -> list:
        return Style_musical.query.all()

    @staticmethod
    def get_style_by_id(id_style: int):
        return Style_musical.query.filter_by(id_style=id_style).first()