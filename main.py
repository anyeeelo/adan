from mente import AdanMente

adan = AdanMente()
adan.ejecutar_ciclo()

# Interacción opcional:
while True:
    pregunta = input("\n🤖 Pregúntale algo a Adan ('salir' para terminar): ")
    if pregunta.lower() == 'salir':
        break
    respuesta = adan.responder(pregunta)
    print(f"Adan responde: {respuesta}")

