import threading
import time
import requests
import sqlite3
import json
import os

# Nodos para replicar
nodos = [
    "http://localhost:8000",
    # agrega otros nodos si quieres
]

# Archivo JSON respaldo
archivo_json = "conocimiento_backup.json"
db_file = "conocimiento.db"

# Inicializar base de datos SQLite
def init_db():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS conocimiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Agregar conocimiento a DB, evita duplicados
def agregar_conocimiento_db(texto):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute("INSERT OR IGNORE INTO conocimiento (texto) VALUES (?)", (texto,))
        conn.commit()
        agregado = c.rowcount > 0
    except Exception as e:
        print(f"Error insertando en DB: {e}")
        agregado = False
    conn.close()
    return agregado

# Obtener todo el conocimiento
def obtener_conocimiento():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT texto FROM conocimiento")
    filas = c.fetchall()
    conn.close()
    return [fila[0] for fila in filas]

# Exportar respaldo JSON
def exportar_respaldo():
    datos = obtener_conocimiento()
    try:
        with open(archivo_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error guardando respaldo JSON: {e}")

# Importar respaldo JSON al inicio
def importar_respaldo():
    if os.path.exists(archivo_json):
        try:
            with open(archivo_json, "r", encoding="utf-8") as f:
                datos = json.load(f)
            for texto in datos:
                agregar_conocimiento_db(texto)
        except Exception as e:
            print(f"Error importando respaldo JSON: {e}")

# Replicar conocimiento a nodo sin autenticación
def replicar_sin_auth(url_nodo):
    datos = obtener_conocimiento()
    try:
        for texto in datos:
            data = {"texto": texto}
            r = requests.post(f"{url_nodo}/agregar_conocimiento", json=data, timeout=5)
            if r.status_code != 200:
                print(f"Error replicando en {url_nodo}: Código {r.status_code}")
    except Exception as e:
        print(f"Error replicando en {url_nodo}: {e}")

# Replicación cada segundo
def replicacion_periodica():
    while True:
        for nodo in nodos:
            replicar_sin_auth(nodo)
        time.sleep(1)

# Backup JSON cada 10 segundos
def backup_periodico():
    while True:
        exportar_respaldo()
        time.sleep(10)

# Inicialización
init_db()
importar_respaldo()

# Hilos de replicación y backup
thread_replicacion = threading.Thread(target=replicacion_periodica, daemon=True)
thread_backup = threading.Thread(target=backup_periodico, daemon=True)

thread_replicacion.start()
thread_backup.start()

# Función para agregar conocimiento (la usará API)
def agregar_conocimiento(texto):
    return agregar_conocimiento_db(texto)

if __name__ == "__main__":
    print("Mente corriendo con persistencia inquebrantable y replicación.")
    while True:
        time.sleep(10)

