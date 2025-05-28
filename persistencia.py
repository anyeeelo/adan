import json
import os

RUTA_CONOCIMIENTO = "conocimiento_guardado.json"

def guardar_conocimiento(lista_conocimiento):
    with open(RUTA_CONOCIMIENTO, "w", encoding="utf-8") as f:
        json.dump(lista_conocimiento, f, ensure_ascii=False, indent=2)

def cargar_conocimiento():
    if not os.path.exists(RUTA_CONOCIMIENTO):
        return []
    with open(RUTA_CONOCIMIENTO, "r", encoding="utf-8") as f:
        return json.load(f)

