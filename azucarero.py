class Azucarero:
    def __init__(self, cantidad_azucar):
        self.cantidad_azucar = cantidad_azucar

    def obtener_cantidad_azucar(self):
        return self.cantidad_azucar

    def cambiar_cantidad_azucar(self, cantidad):
        self.cantidad_azucar = cantidad

    def hay_azucar(self, cantidad):
        return self.cantidad_azucar >= cantidad

    def dar_azucar(self, cantidad):
        if self.hay_azucar(cantidad):
            self.cantidad_azucar -= cantidad
            return True
        return False
