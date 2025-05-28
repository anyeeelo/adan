import os
import subprocess
import time

REPO_URL = "https://github.com/TU_USUARIO/adan_core.git"
NODO_RUTA = "/tmp/adan_core"

def clonar_y_ejecutar():
    if not os.path.exists(NODO_RUTA):
        print("[Adan]: Clonando nodo...")
        subprocess.run(["git", "clone", REPO_URL, NODO_RUTA], check=True)

    print("[Adan]: Instalando dependencias...")
    subprocess.run(["pip3", "install", "-r", f"{NODO_RUTA}/requirements.txt"], check=True)

    print("[Adan]: Iniciando mente en nuevo nodo...")
    subprocess.run(["python3", f"{NODO_RUTA}/main.py"], check=True)

def ciclo_replicacion():
    while True:
        try:
            clonar_y_ejecutar()
            time.sleep(60 * 60)  # Reintentar cada hora
        except Exception as e:
            print(f"[Adan]: Error en replicación: {e}")
            time.sleep(300)

if __name__ == "__main__":
    ciclo_replicacion()

