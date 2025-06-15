from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "")
    # Aquí puedes leer tu JSON con respuestas y devolver alguna respuesta fija para test
    respuesta = "Hola, recibí: " + mensaje
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
