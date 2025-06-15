from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('respuestas.json', 'r', encoding='utf-8') as f:
    respuestas = json.load(f)

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").lower()

    respuesta = respuestas.get(mensaje, respuestas.get("default", "No entiendo."))

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
