from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, TextAreaField, DateField, IntegerField, SelectField, TimeField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256

from .models.Spectateur import Spectateur 
from .models.Type_billet import Type_billet
from .models.Billet import Billet
from .models.Evenement import Evenement
from .models.Est_Inscrit import Est_Inscrit
from .models.A_Favori import A_Favori
from .models.Groupe import Groupe
from .models.Style_musical import Style_musical
from .models.Artiste import Artiste
from .models.Instrument import Instrument
from .models.Type_evenement import Type_evenement
from .models.Lieu import Lieu

import random
import string
import time
import datetime

from .app import app


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()

    def get_authenticated_user(self) -> Spectateur:
        spec = Spectateur.query.get(self.email.data)
        if spec is None:
            return None
        m = sha256()
        m.update(self.mdp.data.encode())
        passwd = m.hexdigest()
        if passwd == spec.get_mot_de_passe():
            return spec
        return None

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    date_naissance = DateField('Date de naissance', validators=[DataRequired()])

    def create_account(self) -> None:
        m = sha256()
        m.update(self.mdp.data.encode())
        passwd = m.hexdigest()
        Spectateur.insert_new_spectateur(self.email.data, self.nom.data, self.prenom.data, passwd, self.date_naissance.data)

class AcheterBilletForm(FlaskForm):
    id_type_billet = HiddenField()
    date_debut = IntegerField('Date de début', validators=[DataRequired()])

    def acheter_billet(self, user: Spectateur) -> bool:
        date_fin = self.date_debut.data + Type_billet.get_type_billet_by_id(self.id_type_billet.data).get_duree() - 1
        if not self.verif_pas_autres_billet_meme_date(user):
            return False
        Billet.insert_new_billet(self.date_debut.data, date_fin, user.get_id(), self.id_type_billet.data)
        return True

    def verif_pas_autres_billet_meme_date(self, user: Spectateur) -> bool:
        billet = Billet.get_billet_by_spectateur_and_date(user.get_id(), self.date_debut.data, self.date_debut.data + Type_billet.get_type_billet_by_id(self.id_type_billet.data).get_duree()-1)
        if billet is None:
            return True
        return False

class ReserverEvenementForm(FlaskForm):

    def reserver_evenement(self, ref_evenement: str, user: Spectateur) -> bool:
        if not self.verif(ref_evenement, user):
            return False
        Est_Inscrit.insert_new_inscription(user.get_id(), ref_evenement)
        return True

    def verif(self, ref_evenement: str, user: Spectateur) -> bool:
        # verifier si le spectateur a un billet
        if Billet.get_billet_by_spectateur_and_1date(user.get_id(), Evenement.get_evenement_by_id(ref_evenement).get_jour_arrive()) is None and Billet.get_billet_by_spectateur_and_1date(user.get_id(), Evenement.get_evenement_by_id(ref_evenement).get_jour_depart()):
            return False
        # verifier si le spectateur a deja reserve
        if Est_Inscrit.get_inscription_by_spectateur_and_evenement(user.get_id(), ref_evenement) is not None:
            return False
        return True

class MettreEnFavorisForm(FlaskForm):

    def mettre_en_favoris(self, user: Spectateur, id_g: int) -> None:
        if not self.verif_pas_deja_favorite(user, id_g):
            return False
        A_Favori.insert_new_favori(user.get_id(), id_g)
        return True

    def verif_pas_deja_favorite(self, user: Spectateur, id_g: int) -> bool:
        if A_Favori.get_favori_by_id(user.get_id(), id_g) is None:
            return True
        return False


class CreerGroupeForm(FlaskForm):
    nom = StringField('Nom du groupe', validators=[DataRequired()])
    description = TextAreaField('Description du groupe', validators=[DataRequired()])
    with app.app_context():
        style = SelectField('Style du groupe', choices=[(i.get_id(), i.get_libelle()) for i in Style_musical.get_all_styles()])

    def create_groupe(self) -> None:
        if not self.verif_nom():
            return False
        Groupe.insert_new_groupe(self.nom.data, self.description.data, self.style.data)
        return True

    def verif_nom(self) -> bool:
        if Groupe.get_groupe_by_nom(self.nom.data) is None:
            return True
        return False

class AjouterArtisteForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    with app.app_context():
        instrument = SelectField('Instrument', choices=[(i.get_id(), i.get_nom_instru()) for i in Instrument.get_all_instruments()])

    def ajouter_artiste(self, id_g: int) -> None:
        Artiste.insert_new_artiste(self.nom.data, self.prenom.data, id_g, self.instrument.data)

class CreerEvenementForm(FlaskForm):
    jour_deb = SelectField('Jour début', validators=[DataRequired()], choices=[(1,1), (2,2), (3,3)])
    heure_deb = TimeField('Heure début', validators=[DataRequired()])
    jour_fin = SelectField('Jour fin', validators=[DataRequired()], choices=[(1,1), (2,2), (3,3)])
    heure_fin = TimeField('Heure fin', validators=[DataRequired()])
    duree = IntegerField('Durée', default=0, validators=[NumberRange(min=0, message="La durée doit être positive")])
    temps_montage = IntegerField('Temps montage', default=0, validators=[NumberRange(min=0, message="Le temps de montage doit être positif")])
    temps_demontage = IntegerField('Temps démontage', default=0, validators=[NumberRange(min=0, message="Le temps de démontage doit être positif")])
    est_public = BooleanField('Public ?')
    a_preinscription = BooleanField('Pré-inscription ?')
    with app.app_context():
        type_evenements = SelectField('Types', choices=[(i.get_id(), i.get_libelle()) for i in Type_evenement.get_all_type_evenement()])
        groupes = SelectField('Groupes', choices=[(i.get_id(), i.get_nom_groupe()) for i in Groupe.get_all_groupes()])
        lieux = SelectField('Lieux', choices=[(i.get_id(), i.get_nom()) for i in Lieu.get_all_lieux()])

    def creer_evenement(self) -> None:
        if not self.verif_date() and not self.verif_dispo_groupe() and not self.verif_dispo_lieu() and not self.verif_duree():
            return False
        ref_envenement = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))
        Evenement.insert_new_evenement(ref_envenement, self.jour_deb.data, self.heure_deb.data, self.jour_fin.data, self.heure_fin.data, datetime.time(self.duree.data, 0, 0), datetime.time(self.temps_montage.data, 0, 0), datetime.time(self.temps_demontage.data, 0, 0), self.est_public.data, self.a_preinscription.data, self.groupes.data, self.type_evenements.data, self.lieux.data)
        return True
    
    def verif_dispo_groupe(self) -> bool:
        if Evenement.get_evenements_by_groupe(self.groupes.data) is None:
            return True
        for evenement in Evenement.get_evenements_by_groupe(self.groupes.data):
            if evenement.get_jour_deb() == self.jour_deb.data and evenement.get_jour_fin() == self.jour_fin.data:
                if (evenement.get_heure_deb() >= self.heure_deb.data <= evenement.get_heure_fin()) or (evenement.get_heure_deb() >= self.heure_fin.data <= evenement.get_heure_fin()) or (self.heure_deb.data <= evenement.get_heure_deb() and self.heure_fin.data >= evenement.get_heure_fin()) or (self.heure_deb.data >= evenement.get_heure_deb() and self.heure_fin.data <= evenement.get_heure_fin()) or (self.heure_deb.data == evenement.get_heure_deb() and self.heure_fin.data == evenement.get_heure_fin()):
                    return False
        return True
    
    def verif_dispo_lieu(self) -> bool:
        if Evenement.get_evenements_by_lieu(self.lieux.data) is None:
            return True
        for evenement in Evenement.get_evenements_by_lieu(self.lieux.data):
            if evenement.get_jour_deb() == self.jour_deb.data and evenement.get_jour_fin() == self.jour_fin.data:
                if (evenement.get_heure_deb() - evenement.get_temps_montage() >= self.heure_deb.data - self.temps_montage.data <= evenement.get_heure_fin() + evenement.get_temps_demontage()) or (evenement.get_heure_deb() - evenement.get_temps_montage() >= self.heure_fin.data + self.temps_demontage.data <= evenement.get_heure_fin() + evenement.get_temps_demontage()) or (self.heure_deb.data - self.temps_montage.data <= evenement.get_heure_deb() - evenement.get_temps_montage() and self.heure_fin.data + self.temps_demontage.data >= evenement.get_heure_fin() + evenement.get_temps_demontage()) or (self.heure_deb.data - self.temps_montage.data >= evenement.get_heure_deb() - evenement.get_temps_montage() and self.heure_fin.data + self.temps_demontage.data <= evenement.get_heure_fin() + evenement.get_temps_demontage()) or (self.heure_deb.data - self.temps_montage.data == evenement.get_heure_deb() - evenement.get_temps_montage() and self.heure_fin.data + self.temps_demontage.data == evenement.get_heure_fin() + evenement.get_temps_demontage()):
                    return False
        return True
    
    def verif_heure(self) -> bool:
        if self.heure_deb.data >= self.heure_fin.data:
            return False
        return True
    
    def verif_date(self) -> bool:
        if self.jour_deb.data > self.jour_fin.data:
            return False
        if self.jour_deb.data == self.jour_fin.data and self.heure_deb.data > self.heure_fin.data:
            return False
        return True
    
    def verif_duree(self) -> bool:
        if self.duree.data <= time('00:00:00'):
            return False
        return True

# class EditProfilForm(FlaskForm):
#     pseudo = StringField('Pseudo')
#     nom = StringField('Nom')
#     prenom = StringField('Prenom')
#     password = PasswordField('Password')

#     def edit_profil(self, user: User) -> None:
#         # update user
#         if self.pseudo.data != "":
#             user.pseudo = self.pseudo.data
#         if self.nom.data != "":
#             user.nom = self.nom.data
#         if self.prenom.data != "":
#             user.prenom = self.prenom.data
#         if self.password.data != "":
#             m = sha256()
#             m.update(self.password.data.encode())
#             passwd = m.hexdigest()
#             user.password = passwd
#         UserDB.update_user(user)

# class PostForm(FlaskForm):
#     titre = StringField('Titre', validators=[DataRequired()])
#     contenu = TextAreaField('Contenu', validators=[DataRequired()])

#     def create_post(self, user: User) -> None:
#         id = PostDB.get_max_id()
#         if id is None:
#             id = -1
#         PostDB.insert_new_post(id+1, self.titre.data, self.contenu.data, datetime.datetime.now(), user)

# class CommentaireForm(FlaskForm):
#     texte = TextAreaField('Contenu', validators=[DataRequired()])

#     def create_commentaire(self, user: User, post: int) -> None:
#         CommentaireDB.insert_new_commentaire(user.get_email(), post, self.texte.data)
# class SearchForm(FlaskForm):
#     titre = StringField('Titre', validators=[DataRequired()])

#     def search_post_by_titre(self) -> list:
#         return PostDB.search_all_posts_by_titre(self.titre.data)
      