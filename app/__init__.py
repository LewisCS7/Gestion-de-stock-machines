# app/__init__.py

# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialise l'application Flask
app = Flask(__name__)

# Définir l'URI de la base de données (remplacez 'your_database_uri_here' par votre URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stoks1.db'

# Initialise la base de données SQLAlchemy
db = SQLAlchemy(app)

# Initialise la migration de la base de données
migrate = Migrate(app, db)

from app import routes, models

