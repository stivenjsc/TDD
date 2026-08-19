class Vaso:
    def __init__(self, cantidad_vasos, contenido):
        self.cantidad_vasos = cantidad_vasos
        self.contenido = contenido

    def obtener_cantidad_vasos(self):
        return self.cantidad_vasos

    def cambiar_cantidad_vasos(self, cantidad):
        self.cantidad_vasos = cantidad

    def obtener_contenido(self):
        return self.contenido

    def cambiar_contenido(self, contenido):
        self.contenido = contenido

    def hay_vasos(self, cantidad):
        return self.cantidad_vasos >= cantidad

    def dar_vasos(self, cantidad):
        if self.hay_vasos(cantidad):
            self.cantidad_vasos -= cantidad
            return True
        return False
