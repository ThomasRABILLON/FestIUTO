import io
from .app import app
from flask import redirect, render_template, url_for, request, flash, send_file

from .models.Groupe import Groupe
from .models.Spectateur import Spectateur
from .models.Evenement import Evenement
from .models.Lieu import Lieu
from .models.Type_billet import Type_billet
from .models.Billet import Billet
from .models.Est_Inscrit import Est_Inscrit
from .models.Type_evenement import Type_evenement
from .models.Style_musical import Style_musical
from .models.Artiste import Artiste
from .models.Instrument import Instrument
from .models.A_Favori import A_Favori
from .models.Hebergement import Hebergement
from .models.Est_Heberger import Est_Heberger
from .models.Lien_rs import Lien_rs
from .models.Lien_video import Lien_video
from .models.Photo import Photo

from .models.LoginManager import load_user
from .Form import LoginForm, RegisterForm, AcheterBilletForm, ReserverEvenementForm, MettreEnFavorisForm, CreerGroupeForm, AjouterArtisteForm, CreerEvenementForm, CreerHebergementForm

from flask_login import login_user, current_user, logout_user, login_required

import time


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', events = Evenement.get_all_evenements(), Groupe = Groupe, Lieu = Lieu)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/billet')
def billet():
    return render_template('billet.html', billet1 = Type_billet.get_type_billet_by_id(1), billet2 = Type_billet.get_type_billet_by_id(2), billet3 = Type_billet.get_type_billet_by_id(3))

@app.route('/achat_billet/<int:id>', methods=['GET', 'POST'])
@login_required
def achat_billet(id):
    if current_user_is_admin():
        return redirect(url_for('login'))
    form = AcheterBilletForm()
    if form.validate_on_submit():
        retour = form.acheter_billet(current_user)
        if retour:
            return redirect(url_for('mes_billets'))
        return redirect(url_for('achat_billet', id = id))
    form.id_type_billet.data = id
    return render_template('billet_confirmation.html', billet = Type_billet.get_type_billet_by_id(id), form = form, id = id)

@app.route('/mes_billets')
@login_required
def mes_billets():
    if current_user_is_admin():
        return redirect(url_for('login'))
    return render_template('mes_billets.html', billets = Billet.get_billet_by_spectateur(current_user.get_id()), Type_billet = Type_billet)

@app.route('/programme', methods=['GET', 'POST'])
def programme():
    if request.method == 'GET':
        if request.args.get('style') is not None and request.args.get('style') != "" and int(request.args.get('style')) != 0:
            return render_template('programme.html', events = Evenement.get_evenements_by_style(int(request.args.get('style')), Groupe), styles = Style_musical.get_all_styles(), Groupe = Groupe, Lieu = Lieu, id_style = int(request.args.get('style')))
    return render_template('programme.html', events = Evenement.get_all_evenements(), styles = Style_musical.get_all_styles(), Groupe = Groupe, Lieu = Lieu, style = 0)

@app.route("/reservation/<string:id>", methods=['GET', 'POST'])
@app.route("/reservation", methods=['GET', 'POST'])
@login_required
def reservation(id=""):
    if current_user_is_admin():
        return redirect(url_for('login'))
    form = ReserverEvenementForm()
    if form.validate_on_submit():
        retour = form.reserver_evenement(id, current_user)
        if retour:
            return redirect(url_for('mes_reservations'))
        return redirect(url_for('reservation'))
    return render_template('reservation.html', events = Evenement.get_evenements_by_reservable(), Groupe = Groupe, Lieu = Lieu, id = id, form = form)

@app.route('/mes_reservations')
@login_required
def mes_reservations():
    if current_user_is_admin():
        return redirect(url_for('login'))
    return render_template('mes_reservations.html', reservations = Est_Inscrit.get_inscription_by_mail(current_user.get_id()), Groupe = Groupe, Evenement = Evenement, Est_Inscrit = Est_Inscrit, Type_evenement = Type_evenement)

@app.route('/groupes')
def groupes():
    return render_template('groupes.html', groupes = Groupe.get_all_groupes(), Style_musical = Style_musical)

@app.route('/groupe/<int:id>', methods=['GET', 'POST'])
@login_required
def groupe(id):
    if current_user_is_admin():
        return redirect(url_for('login'))
    form = MettreEnFavorisForm()
    if form.validate_on_submit():
        retour = form.mettre_en_favoris(current_user, id)
        if retour:
            return redirect(url_for('mes_favoris'))
        return redirect(url_for('groupe', id = id))
    return render_template('groupe.html', form = form, groupe = Groupe.get_groupe_by_id(id), artistes = Artiste.get_artiste_by_groupe(id), Style_musical = Style_musical, Instrument = Instrument, A_Favori = A_Favori)

@app.route('/sup_favoris/<int:id>', methods=['GET', 'POST'])
@login_required
def sup_favoris(id):
    if current_user_is_admin():
        return redirect(url_for('login'))
    A_Favori.delete_favori(current_user.get_id(), id)
    return redirect(url_for('groupe', id = id))

@app.route('/mes_favoris')
@login_required
def mes_favoris():
    if current_user_is_admin():
        return redirect(url_for('login'))
    return render_template('mes_favoris.html', favoris = A_Favori.get_favori_by_spec(current_user.get_id()), Style_musical = Style_musical, Groupe = Groupe)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        mdp = request.form['mdp']
        if mdp == 'admin':
            login_user(Spectateur.get_spectateur_by_mail('admin'))
            return redirect(url_for('panel'))
    return render_template('admin_login.html')

@app.route('/admin/panel')
@login_required
def panel():
    if current_user_is_admin():
        return render_template('panel_admin.html')
    return redirect(url_for('admin'))

@app.route('/admin/creer_groupe', methods=['GET', 'POST'])
@login_required
def creer_groupe():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    form = CreerGroupeForm()
    if form.validate_on_submit():
        retour = form.create_groupe()
        if retour:
            return redirect(url_for('gestion_groupes'))
        return redirect(url_for('creer_groupe'))
    return render_template('creer_groupe.html', form = form)

@app.route('/admin/gestion_groupes')
@login_required
def gestion_groupes():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    return render_template('gestion_groupes.html', groupes = Groupe.get_all_groupes(), Style_musical = Style_musical, Artiste = Artiste, Instrument = Instrument)

@app.route('/admin/image/<int:image_id>')
def show_image(image_id):
    image = Photo.get_photo_by_id(image_id)
    return send_file(io.BytesIO(image.get_photo()), mimetype='image/jpeg')

@app.route('/admin/upload_image/<string:nom>', methods=['GET', 'POST'])
@login_required
def upload_image(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    if request.method == 'POST':
        if request.files['image'] is not None:
            image = request.files['image'].read()
            id_g = Groupe.get_groupe_by_nom(nom).get_id()
            Photo.insert_new_photo(image, id_g)
    return redirect(url_for('gestion_groupes'))

@app.route('/admin/gestion_groupe/<string:nom>')
@login_required
def gestion_groupe(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    groupe = Groupe.get_groupe_by_nom(nom)
    return render_template('gestion_groupe.html', groupe = groupe, artistes = Artiste.get_artiste_by_groupe(groupe.get_id()), liens_rs = Lien_rs.get_lien_rs_by_id_g(groupe.get_id()), liens_video = Lien_video.get_lien_video_by_id_g(groupe.get_id()), photos = Photo.get_photo_by_id_g(groupe.get_id()), Style_musical = Style_musical, Instrument = Instrument)

@app.route('/admin/gestion_groupe/<string:nom>/supprimer_groupe')
@login_required
def supprimer_groupe(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Groupe.delete_groupe(nom)
    return redirect(url_for('gestion_groupes'))

@app.route('/admin/gestion_groupe/<string:nom>/ajouter_lien', methods=['GET', 'POST'])
@login_required
def ajouter_lien(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    if request.method == 'POST':
        if request.form['lien_rs'] is not None and request.form['lien_rs'] != "":
            Lien_rs.insert_new_lien_rs(request.form['lien_rs'], Groupe.get_groupe_by_nom(nom).get_id())
        elif request.form['lien_v'] is not None and request.form['lien_v'] != "":
            Lien_video.insert_new_lien_video(request.form['lien_v'], Groupe.get_groupe_by_nom(nom).get_id())
    return redirect(url_for('gestion_groupe', nom = nom))

@app.route('/admin/gestion_groupe/<string:nom>/supprimer_artiste/<int:id>')
@login_required
def supprimer_artiste(nom, id):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Artiste.delete_artiste(id)
    return redirect(url_for('gestion_groupe', nom = nom))

@app.route('/admin/gestion_groupe/<string:nom>/ajouter_artiste', methods=['GET', 'POST'])
@login_required
def ajouter_artiste(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    form = AjouterArtisteForm()
    if form.validate_on_submit():
        form.ajouter_artiste(Groupe.get_groupe_by_nom(nom).get_id())
        return redirect(url_for('gestion_groupe', nom = nom))
    return render_template('ajouter_artiste.html', nom = nom, form = form)

@app.route('/admin/gestion_groupe/<string:nom>/evenements_groupe')
@login_required
def evenements_groupe(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    groupe = Groupe.get_groupe_by_nom(nom)
    return render_template('evenements_groupe.html', groupe = groupe, events = Evenement.get_evenements_by_groupe(groupe.get_id()), Lieu = Lieu, Type_evenement = Type_evenement, Evenement = Evenement)
    
# @app.route('/admin/gestion_groupe/<string:nom>/evenements_groupe/creer_evenement', methods=['GET', 'POST'])
# @login_required
# def creer_evenement(nom):
#     # TODO

@app.route('/admin/gestion_groupe/<string:nom>/evenements_groupe/<string:ref>/supprimer_evenement_groupe')
@login_required
def supprimer_evenement_groupe(nom, ref):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Evenement.delete_evenement(ref)
    return redirect(url_for('evenements_groupe', nom = nom))

@app.route('/admin/gestion_groupe/<string:nom>/hebergements_groupe')
@login_required
def hebergements_groupe(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    groupe = Groupe.get_groupe_by_nom(nom)
    return render_template('hebergements_groupe.html', groupe = groupe, Hebergement = Hebergement, hebergements = Est_Heberger.get_est_heberger_by_groupe(groupe.get_id()))

@app.route('/admin/gestion_groupe/<string:nom>/hebergements_groupe/ajouter_hebergement', methods=['GET', 'POST'])
@login_required
def ajouter_hebergement_groupe(nom):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    groupe = Groupe.get_groupe_by_nom(nom)
    if request.method == 'GET':
        if request.args.get('date_debut') is not None and request.args.get('date_fin') is not None and request.args.get('date_debut') != "" and request.args.get('date_fin') != "" and request.args.get('date_debut') <= request.args.get('date_fin'):
            if request.args.get('id_hebergement') is not None and request.args.get('id_hebergement') != "" and int(request.args.get('id_hebergement')) != -1:
                Est_Heberger.insert_est_heberger(groupe.get_id(), int(request.args.get('id_hebergement')), int(request.args.get('date_debut')), int(request.args.get('date_fin')))
                return redirect(url_for('hebergements_groupe', nom = nom))
            return render_template('ajouter_hebergement_groupe.html', groupe = groupe, date_debut = int(request.args.get('date_debut')), date_fin = int(request.args.get('date_fin')), hebergements = Est_Heberger.get_all_hebergements_disponibles(groupe, int(request.args.get('date_debut')), int(request.args.get('date_fin')), Groupe.get_nombre_artiste(groupe.get_id())))
    return render_template('ajouter_hebergement_groupe.html', groupe = groupe, date_debut = None, date_fin = None, hebergements = None)

@app.route('/admin/gestion_groupe/<string:nom>/hebergements_groupe/<int:id>/supprimer_hebergement_groupe')
@login_required
def supprimer_hebergement_groupe(nom, id):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Est_Heberger.delete_est_heberger(Groupe.get_groupe_by_nom(nom).get_id(), id)
    return redirect(url_for('hebergements_groupe', nom = nom))

@app.route('/admin/gestion_evenements')
@login_required
def gestion_evenements():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    return render_template('gestion_evenements.html', events = Evenement.get_all_evenements(), Lieu = Lieu, Type_evenement = Type_evenement, Evenement = Evenement, Groupe = Groupe)

@app.route('/admin/gestion_evenements/creer_evenement', methods=['GET', 'POST'])
@login_required
def creer_evenement():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    form = CreerEvenementForm()
    if form.validate_on_submit():
        retour = form.creer_evenement()
        if retour:
            return redirect(url_for('gestion_evenements'))
    return render_template('creer_evenement.html', form = form)

@app.route('/admin/gestion_evenements/supprimer_evenement/<string:ref>')
@login_required
def supprimer_evenement(ref):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Evenement.delete_evenement(ref)
    return redirect(url_for('gestion_evenements'))


@app.route('/admin/gestion_hebergements')
@login_required
def gestion_hebergements():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    return render_template('gestion_hebergements.html', hebergements = Hebergement.get_all_hebergements())

@app.route('/admin/gestion_hebergements/creer_hebergement', methods=['GET', 'POST'])
@login_required
def creer_hebergement():
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    form = CreerHebergementForm()
    if form.validate_on_submit():
        form.creer_hebergement()
        return redirect(url_for('gestion_hebergements'))
    return render_template('creer_hebergement.html', form = form)

@app.route('/admin/gestion_hebergements/supprimer_hebergement/<int:id>')
@login_required
def supprimer_hebergement(id):
    if not current_user_is_admin():
        return redirect(url_for('admin'))
    Hebergement.delete_hebergement(id)
    return redirect(url_for('gestion_hebergements'))





@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not form.is_submitted():
        form.next.data = request.args.get('next')
    elif form.validate_on_submit():
        user = form.get_authenticated_user()
        if user is not None:
            login_user(user)
            next = form.next.data
            if next is None or next == "":
                next = url_for('home')
            return redirect(next)
        return render_template('login.html', title='Se connecter', form=form)
    return render_template('login.html', title='Se connecter', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if Spectateur.get_spectateur_by_mail(form.email.data) is not None:
            flash('Email déjà utilisé')
            return render_template('register.html', title='Créer un compte', form=form)
        form.create_account()
        flash('Votre compte a été créé !')
        return redirect(url_for('login'))
    return render_template('register.html', title='Créer un compte', form=form)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




def current_user_is_admin():
    return current_user.get_id() == 'admin'
