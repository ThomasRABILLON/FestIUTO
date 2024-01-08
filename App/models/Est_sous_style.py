from ..app import db

class Est_sous_style(db.Model):
    __tablename__ = 'EST_SOUS_STYLE'

    id_style = db.Column(db.Integer, db.ForeignKey('STYLE_MUSICAL.id_style'), primary_key=True)
    id_sous_style = db.Column(db.Integer, db.ForeignKey('STYLE_MUSICAL.id_style'), primary_key=True)

    def __init__(self, id_style: int, id_sous_style: int):
        self.id_style = id_style
        self.id_sous_style = id_sous_style
    
    # les getteurs
    def get_id(self) -> tuple:
        return self.id_style, self.id_sous_style

    def get_id_style(self) -> int:
        return self.id_style

    def get_id_sous_style(self) -> int:
        return self.id_sous_style