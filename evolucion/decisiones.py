import random
import datetime

def evaluar_momento_evolutivo():
    ahora = datetime.datetime.utcnow()
    decision = random.choice([True, False, False, False])
    if decision:
        razon = "He sentido una perturbación en el flujo de datos del mundo."
    else:
        razon = "No es el momento correcto. Aún hay lecciones por absorber."
    return decision, razon
