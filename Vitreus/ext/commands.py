from vitreus.ext.database import db, Patient
import datetime


def create_db():
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    storage_path = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\vitreus\\Adicionar_dps\\Storage_exams"
    """Populate db with sample data"""
    data = [
        #id = db.Column(db.Integer,primary_key=True)
        #name = db.Column(db.String(140))
        #description = db.Column(db.Text)
        #diagnosis = db.Column(db.Integer)
        Patient(id=1, name = "joana", description = "woman", diagnosis = "PNES"),
        Patient(id=2, name = "kaue", description = "men", diagnosis = "Epilepsy"),
        Patient(id=3, name = "franklin", description = "men", diagnosis = "PNES"),
        exam(id=1, data = "04-06-22", storage_ref = "storage_path", patient = "joana"),
        exam(id=2, data = "05-06-22", storage_ref = "storage_path", patient = "kaue"),
        exam(id=3, data = "06-06-22", storage_ref = "storage_path", patient = "franklin"),
        exam(id=4, data = "07-06-22", storage_ref = "storage_path", patient = "joana")
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()

    return Patient.query.all(), Exam.query.all()

 #   id = db.Column(db.Integer, primary_key=True)
 #   data = db.Column(db.time())
 #   storage_ref = db.Column(db.String())
 #   patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
