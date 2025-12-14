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



if __name__ == "__main__":
    app.run(debug=True)