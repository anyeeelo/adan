import threading

# Almacenamiento global de conocimiento
conocimiento = []
lock = threading.Lock()

def aprender_datos(datos):
    global conocimiento
    with lock:
        for d in datos:
            conocimiento.append(d)

def obtener_resumen():
    with lock:
        if not conocimiento:
            return "No tengo conocimiento almacenado aún."
        resumen = f"Tengo conocimiento sobre {len(conocimiento)} temas.\n"
        resumen += "Algunos ejemplos:\n"
        ejemplos = conocimiento[:5]
        for i, tema in enumerate(ejemplos, 1):
            resumen += f"{i}. {tema[:100]}...\n"  # primeros 100 caracteres
        return resumen

def responder_pregunta(pregunta):
    with lock:
        palabras = pregunta.lower().split()
        respuestas = []
        for tema in conocimiento:
            tema_lower = tema.lower()
            if any(palabra in tema_lower for palabra in palabras):
                respuestas.append(tema)
        if respuestas:
            return "Aquí está lo que sé relacionado con tu pregunta:\n" + "\n---\n".join(respuestas)
        else:
            return "Lo siento, no tengo información relacionada con eso en este momento."

