from flask import jsonify, abort
from flask_restful import Resource
from vitreus.models import Patient

class PatientResourse(Resource):
    def get(self):
        patients = Patient.query.all()
        return jsonify(
            {"patient":[
                patient.to_dict()
                for patient in patients
            ]       
            }
        )
    def post (self):
        criar_novo_paciente()

class PatientNumberResourse(Resource):
    def get(self, patient_id):
        patient = Patient.query.filter_by(id=patient_id).first() or abort(
            404 
        )
        return jsonify(patient.to_dict())
