from flask import Flask, jsonify, request
from db import receitas, gerar_id

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Receitas Culinárias"})

# CREATE
@app.route("/receitas", methods=["POST"])
def criar_receita():
    dados = request.get_json()

    nova_receita = {
        "id": gerar_id(),
        "nome": dados.get("nome"),
        "ingredientes": dados.get("ingredientes"),
        "modo_preparo": dados.get("modo_preparo")
    }

    receitas.append(nova_receita)
    return jsonify(nova_receita), 201

# READ - listar
@app.route("/receitas", methods=["GET"])
def listar_receitas():
    return jsonify(receitas)

# READ - buscar por id
@app.route("/receitas/<id>", methods=["GET"])
def buscar_receita(id):
    for receita in receitas:
        if receita["id"] == id:
            return jsonify(receita)
    return jsonify({"erro": "Receita não encontrada"}), 404

# UPDATE
@app.route("/receitas/<id>", methods=["PUT"])
def atualizar_receita(id):
    dados = request.get_json()
    for receita in receitas:
        if receita["id"] == id:
            receita.update(dados)
            return jsonify(receita)
    return jsonify({"erro": "Receita não encontrada"}), 404

# DELETE
@app.route("/receitas/<id>", methods=["DELETE"])
def deletar_receita(id):
    for receita in receitas:
        if receita["id"] == id:
            receitas.remove(receita)
            return jsonify({"mensagem": "Receita removida com sucesso"})
    return jsonify({"erro": "Receita não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
