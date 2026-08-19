class Cafetera:
    def __init__(self, cantidad_cafe):
        self.cantidad_cafe = cantidad_cafe

    def obtener_cantidad_cafe(self):
        return self.cantidad_cafe

    def cambiar_cantidad_cafe(self, cantidad):
        self.cantidad_cafe = cantidad

    def hay_cafe(self, cantidad):
        return self.cantidad_cafe >= cantidad

    def dar_cafe(self, cantidad):
        if self.hay_cafe(cantidad):
            self.cantidad_cafe -= cantidad
            return True
        return False
