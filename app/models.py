# app/models.py

from app import db

class Machine(db.Model):
    __tablename__ = 'machine'  # Nom de la table dans la base de données
    id = db.Column(db.String(100), primary_key=True)
    manufacturer = db.Column(db.String(100))
    machine_type = db.Column(db.String(100))
    model = db.Column(db.String(100))
    serial_number = db.Column(db.String(100))  # Suppression de unique=True
    year = db.Column(db.Integer)
    #sas = db.Column(db.String(100))
    programme = db.Column(db.String(100))
    mise = db.Column(db.Integer)  
    #jackpot = db.Column(db.Integer)  
    #rhi = db.Column(db.Integer)  
    #denomination = db.Column(db.String(100))
    #bill_denomination = db.Column(db.String(100))
    #val_jet = db.Column(db.Integer)  
    #mode_calcul = db.Column(db.String(100))
    #category = db.Column(db.String(100))
    state = db.Column(db.String(100))
    #delegation = db.Column(db.String(100))
    commune = db.Column(db.String(100))
    #sector = db.Column(db.String(100))
    #emplacement = db.Column(db.String(100))
    #machine_type_2 = db.Column(db.String(100))
    #code_analytique = db.Column(db.String(100))
    #date_achat = db.Column(db.String(100))  
    #prix_achat = db.Column(db.Float)
    #devise = db.Column(db.String(100))
    #code_immobilisation = db.Column(db.String(100))
    #numero_sim = db.Column(db.String(100))

    #def __repr__(self):
    #    return f'<Machine {self.serial_number}>'
