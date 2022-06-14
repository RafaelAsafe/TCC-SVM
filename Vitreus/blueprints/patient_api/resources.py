from flask import jsonify, abort
from flask_restful import Resource
from vitreus.ext.database import create_patient, create_exam

from vitreus.models import Patient, Exam

class PatientResourse(Resource):
    def get(self):
        patients = Patient.query.all() or abort(204)
        return jsonify(
            {"patient":[patient.to_dict() for patient in patients]}
        )

    def post (self):
       create_patient()

class PatientNumberResourse(Resource):
    def get(self, patient_id):
        patient = Patient.query.filter_by(id=patient_id).first() or abort(
            404 
        )
        return jsonify(patient.to_dict())

class ExamResourse(Resource):
    def get (self,patient_id):
        exams = Exam.query.filter_by(patient_id=patient_id).all()
        return jsonify(
            {"exams":[exam.to_dict() for exam in exams]
            }
        )
    def post (self):
      create_exam()