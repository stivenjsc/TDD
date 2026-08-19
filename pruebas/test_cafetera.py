import unittest

from cafetera import Cafetera


class PruebasCafetera(unittest.TestCase):
    def test_debe_decir_verdadero_si_hay_cafe(self):
        cafetera = Cafetera(10)
        self.assertTrue(cafetera.hay_cafe(5))

    def test_debe_decir_falso_si_no_hay_cafe(self):
        cafetera = Cafetera(10)
        self.assertFalse(cafetera.hay_cafe(11))

    def test_debe_restar_cafe(self):
        cafetera = Cafetera(10)
        cafetera.dar_cafe(7)
        self.assertEqual(3, cafetera.obtener_cantidad_cafe())


if __name__ == "__main__":
    unittest.main()
