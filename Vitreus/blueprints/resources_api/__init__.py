from flask import Blueprint
from flask_restful import Api
from .resources import PatientResourse, PatientNumberResourse

#from .resources import ProductItemResource, ProductResource


bp = Blueprint("resources_api", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(PatientResourse, "/patients/")
api.add_resource(PatientNumberResourse, "/patient/<patient_id>")
def init_app(app):
   app.register_blueprint(bp)
