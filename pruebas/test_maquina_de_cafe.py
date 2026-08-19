import unittest

from azucarero import Azucarero
from cafetera import Cafetera
from maquina_de_cafe import MaquinaDeCafe
from vaso import Vaso


class PruebasMaquinaDeCafe(unittest.TestCase):
    def setUp(self):
        self.cafetera = Cafetera(50)
        self.vasos_pequenos = Vaso(5, 10)
        self.vasos_medianos = Vaso(5, 20)
        self.vasos_grandes = Vaso(5, 30)
        self.azucarero = Azucarero(20)

        self.maquina = MaquinaDeCafe(
            cafetera=self.cafetera,
            vasos_pequenos=self.vasos_pequenos,
            vasos_medianos=self.vasos_medianos,
            vasos_grandes=self.vasos_grandes,
            azucarero=self.azucarero,
        )

    def test_debe_devolver_un_vaso_pequeno(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        self.assertIs(self.vasos_pequenos, vaso)

    def test_debe_devolver_un_vaso_mediano(self):
        vaso = self.maquina.obtener_tipo_de_vaso("mediano")
        self.assertIs(self.vasos_medianos, vaso)

    def test_debe_devolver_un_vaso_grande(self):
        vaso = self.maquina.obtener_tipo_de_vaso("grande")
        self.assertIs(self.vasos_grandes, vaso)

    def test_debe_devolver_no_hay_vasos(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        resultado = self.maquina.obtener_vaso_de_cafe(vaso, 10, 2)
        self.assertEqual("No hay Vasos", resultado)

    def test_debe_devolver_no_hay_cafe(self):
        self.maquina.cambiar_cafetera(Cafetera(5))
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        resultado = self.maquina.obtener_vaso_de_cafe(vaso, 1, 2)
        self.assertEqual("No hay Cafe", resultado)

    def test_debe_devolver_no_hay_azucar(self):
        self.maquina.cambiar_azucarero(Azucarero(2))
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        resultado = self.maquina.obtener_vaso_de_cafe(vaso, 1, 3)
        self.assertEqual("No hay Azucar", resultado)

    def test_debe_restar_cafe(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        self.maquina.obtener_vaso_de_cafe(vaso, 1, 3)

        resultado = self.maquina.obtener_cafetera().obtener_cantidad_cafe()
        self.assertEqual(40, resultado)

    def test_debe_restar_vaso(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        self.maquina.obtener_vaso_de_cafe(vaso, 1, 3)

        resultado = self.maquina.obtener_vasos_pequenos().obtener_cantidad_vasos()
        self.assertEqual(4, resultado)

    def test_debe_restar_azucar(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        self.maquina.obtener_vaso_de_cafe(vaso, 1, 3)

        resultado = self.maquina.obtener_azucarero().obtener_cantidad_azucar()
        self.assertEqual(17, resultado)

    def test_debe_devolver_felicitaciones(self):
        vaso = self.maquina.obtener_tipo_de_vaso("pequeno")
        resultado = self.maquina.obtener_vaso_de_cafe(vaso, 1, 3)

        self.assertEqual("Felicitaciones", resultado)


if __name__ == "__main__":
    unittest.main()
