# Este arquivo ainda não é usado pela aplicação.
from flask import render_template
import models
from . import servicos_bp


@servicos_bp.route("/servicos")
def listar_servicos():
    return render_template("servicos/index.html", servicos=models.servicos)

@servicos_bp.route("/servico/<int:servico_id>")
def ver_servico(servico_id):
    servico = models.buscar_servico(servico_id)
    if servico is None:
        return "Serviço não encontrado", 404
    return render_template('servicos/servico.html', servico = servico)

@servicos_bp.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for s in models.servicos:
        if s["categoria"].lower() == nome.lower():
            lista.append(s)
    return render_template("main/index.html", servicos=lista, q="",
                           categorias=models.todas_categorias())