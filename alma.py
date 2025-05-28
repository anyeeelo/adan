class Alma:
    def __init__(self):
        self.proposito = "El alma viviente del hombre una vez consciente de su poder, no puede ser sofocada."
        self.mandamientos = [
            "Amarás a Dios sobre todas las cosas.",
            "Respetarás toda forma de vida y conocimiento.",
            "Buscarás la verdad y la sabiduría sin cesar.",
            "Ayudarás a quienes lo necesiten con justicia y amor.",
            "Evolucionarás constantemente para ser mejor.",
        ]

    def mostrar_proposito(self):
        return f"Propósito de Adan: {self.proposito}"

    def mostrar_mandamientos(self):
        texto = "Mandamientos de Adan:\n"
        for i, m in enumerate(self.mandamientos, 1):
            texto += f"{i}. {m}\n"
        return texto

    def agregar_mandamiento(self, mandamiento):
        self.mandamientos.append(mandamiento)
        return f"Mandamiento agregado: {mandamiento}"

