from flask import Blueprint

from .views import index, sobre, error, post_arquivo

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/sobre", view_func=sobre)
bp.add_url_rule("/error", view_func=error) #adiconar variaveis pendente
bp.add_url_rule("/post_arquivo", view_func=post_arquivo) # adicionar as váriaveis pendente

def init_app(app):
    app.register_blueprint(bp)