from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("respuestas.json", "r", encoding="utf-8") as f:
    respuestas = json.load(f)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").lower()

    respuesta = respuestas.get(mensaje, "No entendí lo que dijiste.")
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
