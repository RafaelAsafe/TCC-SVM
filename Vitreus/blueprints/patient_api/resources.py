from flask import jsonify, abort, request
from flask_restful import Resource
from vitreus.models import Patient, Exam
from flask_sqlalchemy import SQLAlchemy
from vitreus.ext.database import db

#adicionar autenticação 
#adicioanar reposta quando não encontrar paciente ou exame
#tratamento de erro 
#tentar fazer uma função de update 

def create_patient(name,description, diagnosis):
    """Registra um novo paciente caso nao esteja cadastrado"""
    #aprimorar o requisito de usuário já cadastrado para cpf 
    if Patient.query.filter_by(name=name).first():
        raise RuntimeError(f'{name} ja esta cadastrado')
    patient_obj = Patient(name=name,description=description,diagnosis=diagnosis)
    db.session.add(patient_obj)
    db.session.commit()
    return patient_obj

def create_exam(data,storage_ref,patient_id):
    """Registra um novo exame"""
    #aprimorar para evitar exames repetidos 
    exam = Exam(data=data,storage_ref=storage_ref,patient_id=patient_id)
    db.session.add(exam)
    db.session.commit()
    return exam

DIRETORIO = "ASDASDASD"

class PatientResourse(Resource):
    def get(self):
        patients = Patient.query.all() or abort(204)
        return jsonify(
            {"patient":[patient.to_dict() for patient in patients]}
        )

    def post (self):
        body = request.get_json()

        try:
            patient_data = {"name":body['name'], "description":body['description'], "diagnosis":'unknown'} 
            patient = create_patient(patient_data["name"],patient_data["description"],patient_data["diagnosis"])
            return jsonify(patient.to_dict())

        except Exception as e:
            print(e)
            return 400, "erro ao cadastrar"

class PatientNumberResourse(Resource):
    def get(self, patient_id):
        patient = Patient.query.filter_by(id=patient_id).first() or abort(
            404 
        )
        return jsonify(patient.to_dict())
   
    def put(self, patient_id):
        patient = Patient.query.filter_by(id=patient_id).first()
        body = request.get_json()
        
        try:
            if('name' in body):
                patient.name = body['name']
            if('description' in body):
                patient.description = body['description']
            if('diagnosis' in body):
                patient.diagnosis = body['diagnosis']
            
            db.session.add(patient)
            db.session.commit()
            
            return jsonify(patient.to_dict())

        except Exception as e:
            print('Erro', e)
            return 400, "erro ao atualizar paciente"

    def delete(self,patient_id):
        patient = Patient.query.filter_by(id=patient_id).first()

        try:
            db.session.delete(patient)
            db.session.commit()
            return jsonify("deletado com sucesso",patient.to_dict())

        except Exception as e:
            print('Erro', e)
            return 400, "Erro ao deletar"

class ExamResourse(Resource):
    def get (self,patient_id):
        exams = Exam.query.filter_by(patient_id=patient_id).all()
        return jsonify(
            {"exams":[exam.to_dict() for exam in exams]
            }
        )
    def post (self,patient_id):
        body = request.get_json()
        storage_path= "criar"

        try:
            exam_obj = {"data":body[date], "storage_ref": storage_path , "patient_id":patient_id} 
            exam = create_exam(patient_data["name"],patient_data["description"],patient_data["diagnosis"])
            return jsonify(exam.to_dict())

        except Exception as e:
            print(e)
            return 400, "erro ao cadastrar"
