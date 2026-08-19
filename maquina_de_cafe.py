from vaso import Vaso
from cafetera import Cafetera
from azucarero import Azucarero


class MaquinaDeCafe:
    def __init__(
        self,
        cafetera=None,
        vasos_pequenos=None,
        vasos_medianos=None,
        vasos_grandes=None,
        azucarero=None,
    ):
        # Valores sencillos por defecto basados en los tamaños indicados
        # en la práctica: pequeño 3 Oz, mediano 5 Oz y grande 7 Oz.
        self.cafetera = cafetera or Cafetera(100)
        self.vasos_pequenos = vasos_pequenos or Vaso(10, 3)
        self.vasos_medianos = vasos_medianos or Vaso(10, 5)
        self.vasos_grandes = vasos_grandes or Vaso(10, 7)
        self.azucarero = azucarero or Azucarero(50)

    def cambiar_cafetera(self, cafetera):
        self.cafetera = cafetera

    def cambiar_vasos_pequenos(self, vasos):
        self.vasos_pequenos = vasos

    def cambiar_vasos_medianos(self, vasos):
        self.vasos_medianos = vasos

    def cambiar_vasos_grandes(self, vasos):
        self.vasos_grandes = vasos

    def cambiar_azucarero(self, azucarero):
        self.azucarero = azucarero

    def obtener_cafetera(self):
        return self.cafetera

    def obtener_vasos_pequenos(self):
        return self.vasos_pequenos

    def obtener_vasos_medianos(self):
        return self.vasos_medianos

    def obtener_vasos_grandes(self):
        return self.vasos_grandes

    def obtener_azucarero(self):
        return self.azucarero

    def obtener_tipo_de_vaso(self, tipo):
        tipo = tipo.strip().lower()

        if tipo in ("pequeno", "pequeño"):
            return self.vasos_pequenos
        if tipo == "mediano":
            return self.vasos_medianos
        if tipo == "grande":
            return self.vasos_grandes

        return None

    def obtener_vaso_de_cafe(self, vaso, cantidad_vasos, cantidad_azucar):
        if vaso is None or not vaso.hay_vasos(cantidad_vasos):
            return "No hay Vasos"

        cantidad_cafe_necesaria = vaso.obtener_contenido() * cantidad_vasos

        if not self.cafetera.hay_cafe(cantidad_cafe_necesaria):
            return "No hay Cafe"

        if not self.azucarero.hay_azucar(cantidad_azucar):
            return "No hay Azucar"

        vaso.dar_vasos(cantidad_vasos)
        self.cafetera.dar_cafe(cantidad_cafe_necesaria)
        self.azucarero.dar_azucar(cantidad_azucar)

        return "Felicitaciones"
