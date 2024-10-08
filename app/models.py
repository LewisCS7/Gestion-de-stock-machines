# app/models.py

from app import db

class Machine(db.Model):
    __tablename__ = 'machine'  # Nom de la table dans la base de données
    id = db.Column(db.String(100), primary_key=True)
    manufacturer = db.Column(db.String(100))
    machine_type = db.Column(db.String(100))
    model = db.Column(db.String(100))
    serial_number = db.Column(db.String(100)) 
    year = db.Column(db.Integer)
    programme = db.Column(db.String(100))
    mise = db.Column(db.Integer)  
    state = db.Column(db.String(100))
    commune = db.Column(db.String(100))
