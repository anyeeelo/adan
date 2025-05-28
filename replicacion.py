import os
import subprocess

NODOS_CONOCIDOS = [
    # Ejemplo de nodos accesibles para replicación (IPs, URLs)
    # Requiere que tengas acceso ssh o API autorizada para desplegar
    "user@192.168.1.10",
    "user@mi-servidor-cloud.com",
]

def replicar_en_nodo():
    for nodo in NODOS_CONOCIDOS:
        try:
            # Ejemplo simple: copiar archivos por scp y ejecutar main.py remotamente
            print(f"Intentando replicar en nodo: {nodo}")
            subprocess.run([
                "scp", "-r", "./adan_core", f"{nodo}:~/"
            ], check=True)
            subprocess.run([
                "ssh", nodo, "nohup python3 ~/adan_core/main.py &"
            ], check=True)
            print(f"Réplicas activas en {nodo}")
        except Exception as e:
            print(f"Error replicando en {nodo}: {e}")

