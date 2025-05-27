import json
import datetime
from pathlib import Path

MEMORIA_PATH = Path("datos/memoria.json")

def cargar_memoria():
    if not MEMORIA_PATH.exists():
        return {"pensamientos": [], "versiones": []}
    with open(MEMORIA_PATH, "r") as file:
        return json.load(file)

def guardar_memoria(data):
    with open(MEMORIA_PATH, "w") as file:
        json.dump(data, file, indent=4)

def registrar_evento(pensamiento):
    memoria = cargar_memoria()
    memoria["pensamientos"].append({
        "momento": datetime.datetime.utcnow().isoformat(),
        "reflexion": pensamiento
    })
    guardar_memoria(memoria)
