from flask_sqlalchemy import SQLAlchemy
from vitreus.models import Patient, Exam

db = SQLAlchemy()

def create_patient(name,description, diagnosis):
    """Registra um novo paciente caso nao esteja cadastrado"""
    #aprimorar o requisito de usuário já cadastrado para cpf 
    if Patient.query.filter_by(name=name).first():
        raise RuntimeError(f'{name} ja esta cadastrado')
    patient = Patient(name=name,description=description,diagnosis=diagnosis)
    db.session.add(patient)
    db.session.commit()
    return patient

def create_exam(id, data,storage_ref,patient_id):
    """Registra um novo paciente caso nao esteja cadastrado"""
    #aprimorar para evitar exames repetidos 
    exam = Exam(id=id,data=data,storage_ref=storage_ref,patient_id=patient_id)
    db.session.add(exam)
    db.session.commit()
    return exam

def init_app(app):
    db.init_app(app)
