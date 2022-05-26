from flask import Blueprint

from .views import index, sobre, error, post_arquivo, patients, patient

bp = Blueprint("webui", __name__, template_folder="templates",static_folder="static",static_url_path='/webiu/static/')

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/sobre", view_func=sobre)
bp.add_url_rule("/<string:nome>", view_func=error) #adiconar variaveis pendente
bp.add_url_rule("/post_arquivo",view_func=post_arquivo) # adicionar as váriaveis pendente
bp.add_url_rule("/patients", view_func=patients)
bp.add_url_rule(
    "/patient/<patient_id>", view_func=patient, endpoint="patientview"
)

def init_app(app):
    app.register_blueprint(bp)


