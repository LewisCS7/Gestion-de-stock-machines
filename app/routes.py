# app/routes.py

from flask import send_file, make_response, redirect, url_for, render_template, request
import io
from io import BytesIO
import pandas as pd
from app import app, db
from app.models import Machine

@app.route('/')
def machines():
    # Récupérer les paramètres de recherche depuis l'URL
    id = request.args.get('id')
    manufacturer = request.args.get('manufacturer')
    machine_type = request.args.get('machine_type')
    model = request.args.get('model')
    serial_number = request.args.get('serial_number')
    year = request.args.get('year')
    programme = request.args.get('programme')
    mise = request.args.get('mise')
    state = request.args.get('state')
    commune = request.args.get('commune')

    # Effectuer la recherche dans la base de données en fonction des paramètres fournis
    machines = Machine.query
    if id:
        machines = machines.filter(Machine.id.ilike(f'%{id}%'))
    if manufacturer:
        machines = machines.filter(Machine.manufacturer.ilike(f'%{manufacturer}%'))
    if machine_type:
        machines = machines.filter(Machine.machine_type.ilike(f'%{machine_type}%'))
    if model:
        machines = machines.filter(Machine.model.ilike(f'%{model}%'))
    if serial_number:
        machines = machines.filter(Machine.serial_number.ilike(f'%{serial_number}%'))
    if year:
        machines = machines.filter(Machine.year == year)
    if programme:
        machines = machines.filter(Machine.programme.ilike(f'%{programme}%'))
    if mise:
        machines = machines.filter(Machine.mise.ilike(f'%{mise}%'))
    if state:
        machines = machines.filter(Machine.state.ilike(f'%{state}%'))
    if commune:
        machines = machines.filter(Machine.commune.ilike(f'%{commune}%'))

    machines = machines.all()

    return render_template('machines.html', machines=machines)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            try:
                # Utiliser pandas pour lire le fichier Excel
                df = pd.read_excel(file)

                # Supprimer toutes les données existantes dans la base de données
                db.session.query(Machine).delete()

                # Insérer les nouvelles données dans la base de données
                for index, row in df.iterrows():
                    machine = Machine(
                        id=row['N° MAS'],
                        manufacturer=row['Fabricant'],
                        machine_type=row['Type de MAS'],
                        model=row['Modèle'],
                        serial_number=row['N° Série'],
                        year=row['Année Fab.'],
                        programme=row['Programme'],
                        mise=row['Mise'],
                        state=row['Etat'],
                        commune=row['Commune']
                    )
                    db.session.add(machine)
                db.session.commit()

                return redirect(url_for('machines'))  # Rediriger vers la page affichant les données importées
            except Exception as e:
                return render_template('upload_form.html', error=str(e))  # Afficher un message d'erreur en cas d'échec de l'importation

    return render_template('upload_form.html')

@app.route('/download')
def download():
    # Récupérer les données depuis la base de données
    machines = Machine.query.all()

    # Convertir les données en un DataFrame Pandas
    data = {
        'N° MAS': [machine.id for machine in machines],
        'Fabricant': [machine.manufacturer for machine in machines],
        'Type de MAS': [machine.machine_type for machine in machines],
        'Modèle': [machine.model for machine in machines],
        'N° Série': [machine.serial_number for machine in machines],
        'Année Fab.': [machine.year for machine in machines],
        'Programme': [machine.programme for machine in machines],
        'Mise': [machine.mise for machine in machines],
        'Etat': [machine.state for machine in machines],
        'Commune': [machine.commune for machine in machines]
    }
    df = pd.DataFrame(data)

    # Créer un buffer de mémoire pour stocker le fichier Excel
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    # Créer une réponse avec le fichier Excel
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=machines.xlsx'
    return response