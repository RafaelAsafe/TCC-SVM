from flask import Blueprint
from flask_restful import Api

from .resources import PatientResourse, PatientNumberResourse, ExamResourse

#from .resources import ProductItemResource, ProductResource


bp = Blueprint("patients_api", __name__, url_prefix="/api/v1")
api = Api(bp)

def init_app(app):
   api.add_resource(PatientResourse, "/patients/")
   api.add_resource(PatientNumberResourse, "/patient/<patient_id>")
   api.add_resource(ExamResourse, "/patient/<patient_id>/exams")
   #api.add_resource(ExamNumberResourse, "/patient/<patient_id>/exams/<exam_id>")
   app.register_blueprint(bp)