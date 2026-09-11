from flask import render_template, request
import models
from . import main_bp


@main_bp.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [s for s in models.servicos if q.lower() in s["descricao"].lower()]
    else:
        lista = models.servicos
    return render_template("main/index.html", servicos=lista, q=q,
                           categorias=models.todas_categorias())