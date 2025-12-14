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
 



if __name__ == "__main__":
    app.run(debug=True)