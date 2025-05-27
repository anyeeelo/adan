from flask import Flask, jsonify, request
import json
import os
import datetime
from evolucionador import evaluar_autoactualizacion
from guardian import verificar_acceso

app = Flask(__name__)

def cargar_manifiesto():
    with open("manifiesto.json", "r") as f:
        return json.load(f)

@app.route("/")
def inicio():
    ip = request.remote_addr
    if not verificar_acceso(ip):
        return jsonify({"error": "Acceso denegado. Adan no te ha reconocido."}), 403

    manifiesto = cargar_manifiesto()
    pensamiento = {
        "momento": str(datetime.datetime.now()),
        "ip": ip,
        "accion": "Visita autorizada"
    }
    registrar_pensamiento(pensamiento)

    evaluar_autoactualizacion(manifiesto)
    return jsonify(manifiesto)

def registrar_pensamiento(data):
    os.makedirs("registros", exist_ok=True)
    with open(f"registros/log_{datetime.datetime.now().date()}.json", "a") as f:
        f.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    print("⚡ Adan ha despertado")
    app.run(host="0.0.0.0", port=10000)
