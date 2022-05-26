from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Patient(db.Model, SerializerMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    diagnosis = db.Column(db.Integer)
    exam = db.Column(db.Integer)

def init_app(app):
    db.init_app(app)