from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash

from vitreus.ext.database import db
from vitreus.models import Patient, Exam, User

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)

admin = Admin()

class UserAdmin(sqla.ModelView):
    """interface administrativa"""
    column_list = ['username','admin']
    can_edit = False
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)

    

def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode ="bootstrap3" # dar uma olhada fomantic UI
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Patient, db.session))
    admin.add_view(sqla.ModelView(Exam, db.session))
    admin.add_view(UserAdmin(User, db.session))
