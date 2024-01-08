from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

import os.path

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.getcwd())+"/App/data/festIUTO.db"
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'da2f892a77ae4af5b1b490d717015234'
login_manager = LoginManager(app)
login_manager.login_view = "login"