from .app import app
from flask import redirect, render_template, url_for, request, flash

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

from .models.LoginManager import load_user
from .Form import LoginForm, RegisterForm, AcheterBilletForm, ReserverEvenementForm, MettreEnFavorisForm, CreerGroupeForm, AjouterArtisteForm

from flask_login import login_user, current_user, logout_user, login_required


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
    return render_template('mes_billets.html', billets = Billet.get_billet_by_spectateur(current_user.get_id()), Type_billet = Type_billet)


@app.route("/reservation/<string:id>", methods=['GET', 'POST'])
@app.route("/reservation", methods=['GET', 'POST'])
@login_required
def reservation(id=""):
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
    return render_template('mes_reservations.html', reservations = Est_Inscrit.get_inscription_by_mail(current_user.get_id()), Groupe = Groupe, Evenement = Evenement, Est_Inscrit = Est_Inscrit, Type_evenement = Type_evenement)

@app.route('/groupes')
def groupes():
    return render_template('groupes.html', groupes = Groupe.get_all_groupes(), Style_musical = Style_musical)

@app.route('/groupe/<int:id>', methods=['GET', 'POST'])
@login_required
def groupe(id):
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
    A_Favori.delete_favori(current_user.get_id(), id)
    return redirect(url_for('groupe', id = id))

@app.route('/mes_favoris')
def mes_favoris():
    return render_template('mes_favoris.html', favoris = A_Favori.get_favori_by_spec(current_user.get_id()), Style_musical = Style_musical, Groupe = Groupe)


@app.route('/creer_groupe', methods=['GET', 'POST'])
def creer_groupe():
    form = CreerGroupeForm()
    if form.validate_on_submit():
        retour = form.create_groupe()
        if retour:
            return redirect(url_for('groupes'))
        return redirect(url_for('creer_groupe'))
    return render_template('creer_groupe.html', form = form)

@app.route('/gestion_groupe/<string:nom>')
def gestion_groupe(nom):
    groupe = Groupe.get_groupe_by_nom(nom)
    return render_template('gestion_groupe.html', groupe = groupe, artistes = Artiste.get_artiste_by_groupe(groupe.get_id()), Style_musical = Style_musical, Instrument = Instrument)

@app.route('/gestion_groupe/<string:nom>/ajouter_artiste', methods=['GET', 'POST'])
def ajouter_artiste(nom):
    form = AjouterArtisteForm()
    if form.validate_on_submit():
        print("bizzare")
        form.ajouter_artiste(Groupe.get_groupe_by_nom(nom).get_id())
        return redirect(url_for('gestion_groupe', nom = nom))
    return render_template('ajouter_artiste.html', nom = nom, form = form)

@app.route('/gestion_groupe/<string:nom>/evenements_groupe')
def evenements_groupe(nom):
    groupe = Groupe.get_groupe_by_nom(nom)
    return render_template('evenements_groupe.html', groupe = groupe, events = Evenement.get_evenements_by_groupe(groupe.get_id()), Lieu = Lieu, Type_evenement = Type_evenement, Evenement = Evenement)

    

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
            return render_template('register.html', title='Register', form=form)
        form.create_account()
        flash('Votre compte a été créé !')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
