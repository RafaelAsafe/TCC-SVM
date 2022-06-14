from flask import Blueprint
from flask_restful import Api

#from .tratar_data import 


bp = Blueprint('Exam_api',__name__, url_prefix="/api_exam/v1")
api = Api(bp)
def init_app(app):
    api.add_resource(ExamResourse, "/exams/")
    api.add_resource(ExamNumberResourse, "/exam/<exam_id>")
    app.register_blueprint(bp)