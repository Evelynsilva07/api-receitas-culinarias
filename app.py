from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mesagem": "API de Receitas de Culinária"})

if __name__ == "__main__":
    app.run(debug=True)