from flask import jsonify, abort
from flask_restful import Resource
from vitreus.ext.database import Patient

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
    def get(self, product_id):
        patient = Products.query.filter_by(id=patient_id).first() or abort(
            404
        )
        return jsonify(product.to_dict())
