from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Patient(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    diagnosis = db.Column(db.Integer)
    exams = db.relationship('exam', backref='Patient')


class exam(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    storage_ref = db.Column(db.String())
    patient_id = db.Column(db.Integer, db.ForeignKey(Patient.id))


def init_app(app):
    db.init_app(app)
