# psi-avaliacao2-lucival

# questão 1:
blueprint de servicos não importado para app.py; (deixa o app.py inflado e com muitas rotas de acordo com organização MVC)
rotas dos blueprints dentro do app.py; ## (deixa menos organizado, e quebra a separação entre os controladores)

retorno sem render_template em /servico
  if servico is None:
        return "Serviço não encontrado", 404
    return f"""
    <h2>{servico['descricao']}</h2>
    <p>Categoria: {servico['categoria']}</p>
    <p>Prazo: {servico['prazo']}</p>
    <p>Valor: R$ {servico['valor']}</p>
    <a href='/'>Voltar para a oficina</a>
    """ ## (quebra a regra de Viewers do modelo MVC e torna menos prática a resolução de futuros problemas)

redirect em login levando para rota inexistente
  for u in models.usuarios:
            if u["nome"] == request.form["nome"] and u["senha"] == request.form["senha"]:
                session["usuario"] = u["nome"]
                return redirect(url_for("painel")) ## (enviar para uma rota inexistente quebra o codigo e faz com que a aplicação pare de funcionar corretamente)

template inexistente em servicos/index.html, e para os outros blueprints. ## (dificulta o manuseio do código da aplicação e quebra o fundamento dos viewers em uma arquitetura MVC)
não existe link para a roda /categoria

# questão 2:
Dentro da camada M de Models

# questão 3:
Por causa que os templates foram movidos para subpastas dentro da pasta templates, e portanto tiveram de ser especificados após a refatoração, assim como seus respectivos prefixos, para que o app.py pudesse acessar a essas rotas dentro dos blueprints.
como exemplo return render_template("auth/login.html")
