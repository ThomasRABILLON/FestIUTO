import click

from .app import app, db
from sqlalchemy.sql import text

from App.models import A_Favori, Artiste, Billet, Est_Heberger, Est_Inscrit, Est_sous_style, Evenement, Groupe, Hebergement, Instrument, Lien_rs, Lien_video, Lieu, Photo, Spectateur, Style_musical,Type_billet, Type_evenement


@app.cli.command()
def initdb():
    """Initialise la base de données"""
    with app.app_context():
        db.drop_all()
        db.session.commit()
    with app.app_context():
        db.create_all()
        db.session.commit()  
    with open('App/data/insFestiRABILLON.sql', 'r') as f:
        for line in f:
            sql = text(line)
            db.session.execute(sql)
        db.session.commit()