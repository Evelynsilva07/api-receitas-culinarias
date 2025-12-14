from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mesagem": "API de Receitas de Culinária"})

receitas = [
    {
        "id": 1,
        "nome": "Bolo de Chocolate",
        "ingredientes": ["farinha", "açúcar", "chocolate", "ovos"],
        "modo_preparo": "Misture tudo e asse por 40 minutos."
    }
]

@app.route("/receitas", methods=["GET"])
def listar_receitas():
    return jsonify(receitas)

@app.route("/receitas/<int:id>", methods=["GET"])
def buscar_receita(id):
    for receita in receitas:
        if receita["id"] == id:
            return jsonify(receita)
    return jsonify({"erro": "Receita não encontrada"}), 404 
 
@app.route("/receitas", methods=["POST"])
def criar_receita():
    nova_receita = request.get_json()
    nova_receita["id"] = receitas[-1]["id"] + 1
    receitas.append(nova_receita)
    return jsonify(nova_receita), 201

{
  "nome": "Panqueca",
  "ingredientes": ["leite", "ovo", "farinha"],
  "modo_preparo": "Misture tudo e frite."
}


@pp.route("/receitas/<int:id>", methods=["PUT"])
def atualizar_receita(id):
    dados = request.get_json()
    for receita in receitas:
        if receita["id"] == id:
            receita.update(dados)
            return jsonify(receita)
    return jsonify({"erro": "Receita não encontrada"}), 404




if __name__ == "__main__":
    app.run(debug=True)