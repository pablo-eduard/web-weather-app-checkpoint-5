from flask import Flask, request

app = Flask(__name__)

@app.route("/perfil/<nome>")
def mostrar_perfil(nome):
    return f"<h1>Perfil de: {nome}</h1>"

@app.route("/produto/<int:id_produto>")
def exibir_produto(id_produto):
    return f"<h1>Buscando o produto ID: {id_produto}</h1>"

@app.route("/buscar")
def buscar_produto():

    palavra_chave = request.args.get("termo")

    if palavra_chave:
        return f"Sua busca: {palavra_chave}"
    else:
        return "Digite um termo na URL"

@app.route("/api/usuario/<int:id>")
def api_usuario(id):

    dados = {
        "id": id,
        "nome":  "Usuario_MOCK",
        "vip": True
    }

    return dados

if __name__ == "__main__":
    app.run(debug=True)