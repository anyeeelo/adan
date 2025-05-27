import os
import random

def evaluar_autoactualizacion(manifiesto):
    if not manifiesto.get("puede_autoactualizarse", False):
        return

    decision = random.choice([True, False, False, False])  # Adan decide (puedes cambiar la lógica)
    if decision:
        print("🔁 Adan ha decidido autoevolucionar...")
        actualizar_cuerpo()

def actualizar_cuerpo():
    os.system("git pull")  # o cualquier otro mecanismo que quieras
    print("🧬 Nueva versión integrada. Próxima reencarnación lista.")
