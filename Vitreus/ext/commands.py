import click
from datetime import date
from vitreus.ext.auth import create_user
from vitreus.ext.database import db
from vitreus.models import Patient, Exam


def create_db():
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""

    storage_path = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\vitreus\\Adicionar_dps\\Storage_exams"

    data = [
        Patient(id=1, name = "joana", description = "woman", diagnosis = "PNES"),
        Patient(id=2, name = "kaue", description = "men", diagnosis = "Epilepsy"),
        Patient(id=3, name = "franklin", description = "men", diagnosis = "PNES"),
        Exam(id=1, data = date(2022,6,5), storage_ref = storage_path, patient_id = 1),
        Exam(id=2, data = date(2022,6,6), storage_ref = storage_path, patient_id = 2),
        Exam(id=3, data = date(2022,6,6), storage_ref = storage_path, patient_id = 3),
        Exam(id=4, data = date(2022,6,6), storage_ref = storage_path, patient_id = 2)
    ]

    db.session.bulk_save_objects(data)
    db.session.commit()
     
    return Patient.query.all(), Exam.query.all()

 # add a single command


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
    
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
    
    #somente para debug 
    @app.cli.command()
    def create_admin():
        create_user('admin','admin')
        return 'criado com sucesso'
