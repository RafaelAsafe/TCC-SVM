from vitreus.ext.database import db, Patient

def create_db():
    db.create_all()

def drop_db():
    """Cleans database"""
    db.drop_all()

def populate_db():
    """Populate db with sample data"""
    data = [
            #id = db.Column(db.Integer,primary_key=True)
            #name = db.Column(db.String(140))
            #description = db.Column(db.Text)
            #diagnosis = db.Column(db.Integer)
        Patient(id=1, name="joana", description="woman", diagnosis="PNES"),
        Patient(id=2, name="kaue", description="men", diagnosis="Epilepsy"),
        Patient(id=3, name="franklin", description="men", diagnosis="PNES")
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Patient.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
