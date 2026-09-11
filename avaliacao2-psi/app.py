# app.py — Oficina de Conserto (versão inicial)
from flask import Flask, render_template, request, redirect, url_for, session
import models
from blueprints.servicos import servicos_bp
from blueprints.auth import auth_bp
from blueprints.main import main_bp
from models import Servico


app = Flask(__name__)
app.secret_key = "oficina-secreta"
app.register_blueprint(servicos_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

@app.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for s in models.servicos:
        if s["categoria"].lower() == nome.lower():
            lista.append(s)
    return render_template("main/index.html", servicos=lista, q="",
                           categorias=models.todas_categorias())

if __name__ == "__main__":
    app.run(debug=True)