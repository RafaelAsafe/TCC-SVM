from vitreus.ext.database import db
from sqlalchemy_serializer import SerializerMixin

class Patient(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    diagnosis = db.Column(db.Integer)
    exams = db.relationship('Exam', backref='patient')


class Exam(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    storage_ref = db.Column(db.String())
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))


class User(db.Model,SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))