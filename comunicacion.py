# comunicacion.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio
import json
import os
import httpx

app = FastAPI()

# Archivo para persistir el conocimiento
ARCHIVO_CONOCIMIENTO = "conocimiento.json"

# Lista de conocimiento (cargada al iniciar)
conocimiento = []

# Lista de nodos remotos para replicar (cambia según tu red)
nodos_remotos = [
    "http://192.168.1.5:8000",     # Ejemplo nodo 1
    "https://replit.com/@anyelolucianof/adanreplika" # Ejemplo nodo 2
    "https://adan-efba.onrender.com"
    "http://3.21.164.140:8000"
]

# Cargar conocimiento desde archivo (si existe)
def cargar_conocimiento():
    global conocimiento
    if os.path.exists(ARCHIVO_CONOCIMIENTO):
        with open(ARCHIVO_CONOCIMIENTO, "r", encoding="utf-8") as f:
            conocimiento = json.load(f)
    else:
        conocimiento = []

# Guardar conocimiento a archivo
def guardar_conocimiento():
    with open(ARCHIVO_CONOCIMIENTO, "w", encoding="utf-8") as f:
        json.dump(conocimiento, f, ensure_ascii=False, indent=2)

# Inicializar conocimiento al iniciar la app
cargar_conocimiento()

@app.post("/agregar_conocimiento")
async def agregar_conocimiento(request: Request):
    datos = await request.json()
    texto = datos.get("texto", "").strip()
    if texto and texto not in conocimiento:
        conocimiento.append(texto)
        guardar_conocimiento()
        return JSONResponse({"status": "OK", "mensaje": "Conocimiento agregado"})
    return JSONResponse({"status": "OK", "mensaje": "Conocimiento ya existente o vacío"})

@app.get("/")
async def raiz():
    return {"mensaje": "Servidor de Adan activo y listo para replicar"}

# Función para replicar conocimiento a un nodo remoto
async def replicar_a_nodo(nodo_url):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            for dato in conocimiento:
                await client.post(f"{nodo_url}/agregar_conocimiento", json={"texto": dato})
        print(f"Replicación completada a {nodo_url}")
    except Exception as e:
        print(f"Error replicando a {nodo_url}: {e}")

# Tarea asíncrona que replica cada segundo a todos los nodos remotos
async def replicar_periodicamente():
    while True:
        for nodo in nodos_remotos:
            await replicar_a_nodo(nodo)
        await asyncio.sleep(1)  # Espera 1 segundo

# Evento al iniciar la app para lanzar replicación automática en background
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(replicar_periodicamente())

